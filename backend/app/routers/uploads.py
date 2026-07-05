from pathlib import Path
print(">>> Upload Router Loaded <<<")
from uuid import uuid4

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app import schemas

from app.services.card_generator import create_appreciation_card

from app.services.appreciation_service import (
    get_employee_details,
    get_boss_details,
    get_appreciation_message
)

router = APIRouter(
    prefix="/uploads",
    tags=["Uploads"]
)

UPLOAD_FOLDER = Path("uploads")

UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/photo")
async def upload_photo(

    token: str = Form(...),

    file: UploadFile = File(...),

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
            detail="This link has already been used."
        )

    employee = get_employee_details(
        db,
        greeting_link.employee_id
    )

    if employee is None:

        raise HTTPException(
            status_code=404,
            detail="Employee not found."
        )

    extension = file.filename.split(".")[-1]

    filename = f"{uuid4()}.{extension}"

    file_path = UPLOAD_FOLDER / filename

    with open(file_path, "wb") as buffer:

        buffer.write(await file.read())

    boss = get_boss_details()

    message = get_appreciation_message(
        employee.name
    )

    card_path = create_appreciation_card(

        employee_name=employee.name,

        designation=employee.designation,

        message=message,

        boss_name=boss["name"],

        boss_designation=boss["designation"],

        boss_photo=boss["photo"],

        employee_photo=str(file_path),

        output_name=f"{uuid4()}.png"

    )

    greeting = crud.create_greeting(

        db,

        schemas.GreetingCreate(

            employee_id=employee.id,

            employee_name=employee.name,

            designation=employee.designation,

            boss_name=boss["name"],

            boss_designation=boss["designation"],

            message=message,

            photo_path=str(file_path),

            greeting_path=card_path,

            token=token,

            expires_on=greeting_link.expires_on,

            downloaded="No"

        )

    )

    greeting_link.used = "Yes"

    db.commit()

    return {

        "status": "success",

        "message": "Greeting generated successfully.",

        "greeting_id": greeting.id,

        "image": card_path

    }