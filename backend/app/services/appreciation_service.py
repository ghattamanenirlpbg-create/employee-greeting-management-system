from sqlalchemy.orm import Session

from app import models


def get_employee_details(
    db: Session,
    employee_id: int
):

    return (
        db.query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )


def get_boss_details():

    return {

        "name": "Dr. Damodharen M",

        "designation": "Chief Digital Officer",

        "photo": "app/assets/boss_photo.png"

    }


def get_appreciation_message(
    employee_name
):

    return f"""

Dear {employee_name},

Your dedication, commitment, professionalism and continuous pursuit of excellence have made a significant contribution to our organization.

Your positive attitude, ownership and passion inspire everyone around you.

Thank you for being a valued member of our team.

We sincerely appreciate your efforts and wish you continued success in your professional journey.

"""