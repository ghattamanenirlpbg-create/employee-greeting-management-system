from pathlib import Path
from uuid import uuid4

from fastapi import File
from fastapi import Form
from fastapi import UploadFile

from app.services.card_generator import create_appreciation_card

from app.services.appreciation_service import (
    get_boss_details,
    get_appreciation_message
)
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app import schemas


router = APIRouter(
    prefix="/greetings",
    tags=["Greetings"]
)


# =====================================================
# GET ALL GREETINGS
# =====================================================

@router.get("/", response_model=list[schemas.Greeting])
def get_all_greetings(
    db: Session = Depends(get_db)
):
    return crud.get_greetings(db)


# =====================================================
# GET SINGLE GREETING
# =====================================================

@router.get("/{greeting_id}", response_model=schemas.Greeting)
def get_greeting(
    greeting_id: int,
    db: Session = Depends(get_db)
):

    greeting = crud.get_greeting(
        db,
        greeting_id
    )

    if greeting is None:
        raise HTTPException(
            status_code=404,
            detail="Greeting not found"
        )

    return greeting


# =====================================================
# CREATE GREETING
# =====================================================

@router.post("/", response_model=schemas.Greeting)
def create_greeting(
    greeting: schemas.GreetingCreate,
    db: Session = Depends(get_db)
):
    return crud.create_greeting(
        db,
        greeting
    )


# =====================================================
# UPDATE GREETING
# =====================================================

@router.put("/{greeting_id}", response_model=schemas.Greeting)
def update_greeting(
    greeting_id: int,
    greeting: schemas.GreetingUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_greeting(
        db,
        greeting_id,
        greeting
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Greeting not found"
        )

    return updated


# =====================================================
# DELETE GREETING
# =====================================================

@router.delete("/{greeting_id}")
def delete_greeting(
    greeting_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_greeting(
        db,
        greeting_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Greeting not found"
        )

    return {
        "message": "Greeting deleted successfully"
    }

# =====================================================
# ADMIN GENERATE GREETING
# =====================================================

UPLOAD_FOLDER = Path("uploads")

UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/generate")
async def generate_greeting(

    emp_id: str = Form(...),

    file: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    employee = crud.get_employee_by_empid(
        db,
        emp_id
    )

    if employee is None:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    extension = file.filename.split(".")[-1]

    filename = f"{uuid4()}.{extension}"

    photo_path = UPLOAD_FOLDER / filename

    with open(photo_path, "wb") as buffer:

        buffer.write(await file.read())

    boss = get_boss_details()

    message = get_appreciation_message(
        employee.name
    )

    greeting_path = create_appreciation_card(

        employee_name=employee.name,

        designation=employee.designation,

        message=message,

        boss_name=boss["name"],

        boss_designation=boss["designation"],

        boss_photo=boss["photo"],

        employee_photo=str(photo_path),

        output_name=f"{uuid4()}.png"

    )

    return {

        "status": "success",

        "image": greeting_path

    }