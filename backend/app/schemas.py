from pydantic import BaseModel, EmailStr


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

from pydantic import BaseModel, EmailStr


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