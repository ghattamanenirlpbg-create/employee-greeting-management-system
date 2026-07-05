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

def get_employee_by_empid(
    db: Session,
    emp_id: str
):

    return (

        db.query(models.Employee)

        .filter(models.Employee.emp_id == emp_id)

        .first()

    )

def create_employee(db: Session, employee: schemas.EmployeeCreate):

    errors = []

    if db.query(models.Employee).filter(
        models.Employee.emp_id == employee.emp_id
    ).first():
        errors.append("Employee ID already exists.")

    if db.query(models.Employee).filter(
        models.Employee.name == employee.name
    ).first():
        errors.append("Employee Name already exists.")

    if db.query(models.Employee).filter(
        models.Employee.designation == employee.designation
    ).first():
        errors.append("Designation already exists.")

    if db.query(models.Employee).filter(
        models.Employee.role == employee.role
    ).first():
        errors.append("Role already exists.")

    if db.query(models.Employee).filter(
        models.Employee.email == employee.email
    ).first():
        errors.append("Email ID already exists.")

    if errors:

        raise ValueError("\n".join(errors))

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

    errors = []

    if db.query(models.Employee).filter(
        models.Employee.emp_id == employee.emp_id,
        models.Employee.id != employee_id
    ).first():

        errors.append("Employee ID already exists.")

    if db.query(models.Employee).filter(
        models.Employee.name == employee.name,
        models.Employee.id != employee_id
    ).first():

        errors.append("Employee Name already exists.")

    if db.query(models.Employee).filter(
        models.Employee.designation == employee.designation,
        models.Employee.id != employee_id
    ).first():

        errors.append("Designation already exists.")

    if db.query(models.Employee).filter(
        models.Employee.role == employee.role,
        models.Employee.id != employee_id
    ).first():

        errors.append("Role already exists.")

    if db.query(models.Employee).filter(
        models.Employee.email == employee.email,
        models.Employee.id != employee_id
    ).first():

        errors.append("Email ID already exists.")

    if errors:

        raise ValueError("\n".join(errors))

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

    errors = []

    if db.query(models.User).filter(
        models.User.username == user.username
    ).first():
        errors.append("Username already exists.")

    if errors:

        raise ValueError("\n".join(errors))

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

    errors = []

    if db.query(models.User).filter(
        models.User.username == user.username,
        models.User.id != user_id
    ).first():

        errors.append("Username already exists.")

    if errors:

        raise ValueError("\n".join(errors))

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

# =====================================================
# GREETINGS
# =====================================================

def get_greetings(db: Session):

    return db.query(models.Greeting).all()


def get_greeting(db: Session, greeting_id: int):

    return (
        db.query(models.Greeting)
        .filter(models.Greeting.id == greeting_id)
        .first()
    )


def create_greeting(
    db: Session,
    greeting: schemas.GreetingCreate
):

    db_greeting = models.Greeting(**greeting.model_dump())

    db.add(db_greeting)

    db.commit()

    db.refresh(db_greeting)

    return db_greeting


def update_greeting(
    db: Session,
    greeting_id: int,
    greeting: schemas.GreetingUpdate
):

    db_greeting = get_greeting(db, greeting_id)

    if not db_greeting:
        return None

    for key, value in greeting.model_dump().items():

        setattr(db_greeting, key, value)

    db.commit()

    db.refresh(db_greeting)

    return db_greeting


def delete_greeting(
    db: Session,
    greeting_id: int
):

    db_greeting = get_greeting(db, greeting_id)

    if not db_greeting:
        return None

    db.delete(db_greeting)

    db.commit()

    return True

# =====================================================
# GREETING LINKS
# =====================================================

def create_greeting_link(
    db: Session,
    link: schemas.GreetingLinkCreate
):

    db_link = models.GreetingLink(
        **link.model_dump()
    )

    db.add(db_link)

    db.commit()

    db.refresh(db_link)

    return db_link


def get_greeting_link(
    db: Session,
    token: str
):

    return (
        db.query(models.GreetingLink)
        .filter(models.GreetingLink.token == token)
        .first()
    )

def validate_greeting_token(
    db: Session,
    token: str
):

    return (
        db.query(models.GreetingLink)
        .filter(models.GreetingLink.token == token)
        .first()
    )