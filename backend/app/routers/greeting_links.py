from datetime import datetime
print(">>> Greeting Links Router Loaded <<<")

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app import schemas

from app.services.token_service import (
    generate_token,
    get_expiry_date
)

from app.services.email_service import (
    send_greeting_email
)


router = APIRouter(
    prefix="/greeting-links",
    tags=["Greeting Links"]
)


# =====================================================
# CREATE SECURE LINK + SEND EMAIL
# =====================================================

@router.post("/")
def create_link(

    employee_id: int,

    employee_email: str,

    db: Session = Depends(get_db)

):

    token = generate_token()

    expires = get_expiry_date()

    link = f"http://localhost:5173/greeting/{token}"

    crud.create_greeting_link(

        db,

        schemas.GreetingLinkCreate(

            employee_id=employee_id,

            employee_email=employee_email,

            token=token,

            expires_on=expires,

            used="No"

        )

    )

    send_greeting_email(

        employee_name="Employee",

        employee_email=employee_email,

        link=link

    )

    return {

        "message": "Email sent successfully.",

        "token": token,

        "url": link,

        "expires_on": expires

    }

# =====================================================
# GENERATE SECURE LINKS (MULTIPLE EMPLOYEES)
# =====================================================

@router.post("/generate")
def generate_links(

    employee_ids: list[int],

    db: Session = Depends(get_db)

):

    generated = []

    sent = 0

    for employee_id in employee_ids:

        employee = crud.get_employee(

            db,

            employee_id

        )

        if employee is None:

            continue

        token = generate_token()

        expires = get_expiry_date()

        crud.create_greeting_link(

            db,

            schemas.GreetingLinkCreate(

                employee_id=employee.id,

                employee_email=employee.email,

                token=token,

                expires_on=expires,

                used="No"

            )

        )

        link = f"http://localhost:5173/greeting/{token}"

        send_greeting_email(

            employee_name=employee.name,

            employee_email=employee.email,

            link=link

        )

        sent += 1

        generated.append(

            {

                "employee_id": employee.id,

                "employee_name": employee.name,

                "email": employee.email,

                "token": token,

                "link": link

            }

        )

    return {

        "message": f"{sent} email(s) sent successfully.",

        "links": generated

    }


# =====================================================
# VALIDATE TOKEN
# =====================================================

@router.get("/{token}")
def validate_token(

    token: str,

    db: Session = Depends(get_db)

):

    greeting_link = crud.validate_greeting_token(

        db,

        token

    )

    if greeting_link is None:

        raise HTTPException(

            status_code=404,

            detail="Invalid Link"

        )

    if greeting_link.used == "Yes":

        raise HTTPException(

            status_code=400,

            detail="Link Already Used"

        )

    if datetime.utcnow() > greeting_link.expires_on:

        raise HTTPException(

            status_code=400,

            detail="Link Expired"

        )

    return {

        "status": "Valid",

        "employee_id": greeting_link.employee_id,

        "employee_email": greeting_link.employee_email,

        "expires_on": greeting_link.expires_on

    }