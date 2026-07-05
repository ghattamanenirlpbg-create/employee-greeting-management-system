from datetime import datetime

from pydantic import BaseModel, EmailStr


# =====================================================
# EMPLOYEE SCHEMAS
# =====================================================

class EmployeeBase(BaseModel):
    emp_id: str
    name: str
    designation: str
    role: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# USER SCHEMAS
# =====================================================

class UserBase(BaseModel):
    username: str
    password: str
    role: str
    status: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# GREETING SCHEMAS
# =====================================================

class GreetingBase(BaseModel):
    employee_id: int
    employee_name: str
    designation: str
    boss_name: str
    boss_designation: str
    message: str
    photo_path: str
    greeting_path: str
    token: str
    expires_on: datetime
    downloaded: str


class GreetingCreate(GreetingBase):
    pass


class GreetingUpdate(GreetingBase):
    pass


class Greeting(GreetingBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class GreetingLinkBase(BaseModel):

    employee_id: int

    employee_email: EmailStr

    token: str

    expires_on: datetime

    used: str


class GreetingLinkCreate(GreetingLinkBase):
    pass


class GreetingLink(GreetingLinkBase):

    id: int

    class Config:
        from_attributes = True