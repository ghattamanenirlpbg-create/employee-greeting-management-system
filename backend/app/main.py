from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from . import models

from .routers import employees
from .routers import users
from .routers import greetings
from .routers import uploads
from .routers import greeting_links
from .routers import auth
from fastapi.staticfiles import StaticFiles

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Greeting Management System", debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://employee-greeting-management-system.vercel.app",
        "https://employee-greeting-management-system-hg9fl2yv8-rlprasad.vercel.app",
        
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/generated", StaticFiles(directory="app/generated"), name="generated")

app.mount("/uploaded-files", StaticFiles(directory="uploads"), name="uploaded-files")
app.include_router(employees.router)
app.include_router(users.router)
app.include_router(greetings.router)
app.include_router(uploads.router)
app.include_router(greeting_links.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Employee Greeting Management System API is running"}
