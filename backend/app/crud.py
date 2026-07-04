from sqlalchemy.orm import Session
from .security import hash_password
from . import models, schemas


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, employee_id: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def update_employee(
    db: Session,
    employee_id: int,
    employee: schemas.EmployeeUpdate
):
    db_employee = get_employee(db, employee_id)

    if not db_employee:
        return None

    for key, value in employee.model_dump().items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)

    if not db_employee:
        return None

    db.delete(db_employee)
    db.commit()

    return db_employee

def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )


def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(
        username=user.username,
        password=user.password,
        role=user.role,
        status=user.status
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user: schemas.UserUpdate
):
    db_user = get_user(db, user_id)

    if not db_user:
        return None

    for key, value in user.model_dump().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user