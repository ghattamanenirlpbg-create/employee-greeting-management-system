from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud
from .. import schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[schemas.User])
def get_all_users(
    db: Session = Depends(get_db)
):

    return crud.get_users(db)


@router.post("/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    try:

        return crud.create_user(
            db,
            user
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
):

    try:

        updated = crud.update_user(
            db,
            user_id,
            user
        )

        if updated is None:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return updated

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_user(
        db,
        user_id
    )

    if deleted is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }