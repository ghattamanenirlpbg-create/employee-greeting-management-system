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

from sqlalchemy import DateTime
from sqlalchemy import Text
from datetime import datetime


class Greeting(Base):
    __tablename__ = "greetings"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, nullable=False)

    employee_name = Column(String(150), nullable=False)

    designation = Column(String(150), nullable=False)

    boss_name = Column(String(150), nullable=False)

    boss_designation = Column(String(150), nullable=False)

    message = Column(Text, nullable=False)

    photo_path = Column(String(300), nullable=False)

    greeting_path = Column(String(300), nullable=False)

    token = Column(String(200), unique=True, nullable=False)

    expires_on = Column(DateTime, nullable=False)

    downloaded = Column(String(20), default="No")

    created_at = Column(DateTime, default=datetime.utcnow)

class GreetingLink(Base):
    __tablename__ = "greeting_links"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, nullable=False)

    employee_email = Column(String(150), nullable=False)

    token = Column(String(255), unique=True, nullable=False)

    expires_on = Column(DateTime, nullable=False)

    used = Column(String(10), default="No")