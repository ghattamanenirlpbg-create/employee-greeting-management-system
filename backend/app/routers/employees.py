from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app import schemas

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/", response_model=list[schemas.Employee])
def get_employees(
    db: Session = Depends(get_db)
):
    return crud.get_employees(db)

@router.get("/empid/{emp_id}", response_model=schemas.Employee)
def get_employee_by_empid(
    emp_id: str,
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

    return employee

@router.get("/{employee_id}", response_model=schemas.Employee)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = crud.get_employee(db, employee_id)

    if employee is None:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee



@router.post("/", response_model=schemas.Employee)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(
        db,
        employee
    )


@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):

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


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_employee(
        db,
        employee_id
    )

    if deleted is None:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }