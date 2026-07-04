from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from . import models

from .routers import employees
from .routers import users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Greeting Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(employees.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {
        "message": "Employee Greeting Management System API is running"
    }