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