from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app import models

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login")
def login(

    username: str,

    password: str,

    db: Session = Depends(get_db)

):

    user = (

        db.query(models.User)

        .filter(models.User.username == username)

        .first()

    )

    if user is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid Username"

        )

    if user.password != password:

        raise HTTPException(

            status_code=401,

            detail="Invalid Password"

        )

    if user.status != "Active":

        raise HTTPException(

            status_code=401,

            detail="User Inactive"

        )

    return {

        "message": "Login Successful",

        "role": user.role,

        "username": user.username

    }