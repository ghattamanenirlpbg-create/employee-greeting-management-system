from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud, schemas

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/", response_model=list[schemas.Employee])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@router.post("/", response_model=schemas.Employee)
@router.post("/", response_model=schemas.Employee)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):

    try:

        return crud.create_employee(db, employee)

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):

    try:

        updated = crud.update_employee(
            db,
            employee_id,
            employee
        )

        if updated is None:

            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return updated

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_employee(db, employee_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}