from sqlalchemy import Column, Integer, String

from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    emp_id = Column(String(20), unique=True, nullable=False)

    name = Column(String(100), nullable=False)

    designation = Column(String(100), nullable=False)

    role = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)

    password = Column(String(100), nullable=False)

    role = Column(String(50), nullable=False)

    status = Column(String(20), nullable=False)