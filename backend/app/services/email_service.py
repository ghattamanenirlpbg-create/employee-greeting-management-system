import smtplib
import os

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


SMTP_SERVER = "smtp.gmail.com"

SMTP_PORT = 587

EMAIL = os.getenv("EMAIL_USERNAME")

PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_greeting_email(

    employee_name,

    employee_email,

    link

):

    subject = "Appreciation Greeting Awaiting You"

    html = f"""
    <html>

    <body style="font-family:Arial;">

        <h2>Congratulations {employee_name}!</h2>

        <p>

        You have received an Appreciation Greeting.

        </p>

        <p>

        Please click the button below to upload your photograph and generate your appreciation card.

        </p>

        <br>

        <a
        href="{link}"
        style="
        background:#1976d2;
        color:white;
        padding:14px 24px;
        text-decoration:none;
        border-radius:8px;
        ">

        Generate My Appreciation Card

        </a>

        <br><br>

        <p>

        <b>Note:</b>

        This link will expire automatically after 5 days.

        </p>

        <br>

        Regards,

        <br>

        <b>Dr. Damodharen M</b>

        <br>

        Chief Digital Officer

    </body>

    </html>
    """

    msg = MIMEMultipart("alternative")

    msg["Subject"] = subject

    msg["From"] = EMAIL

    msg["To"] = employee_email

    msg.attach(
        MIMEText(
            html,
            "html"
        )
    )
    
    print("EMAIL =", EMAIL)
    print("PASSWORD FOUND =", PASSWORD is not None)

    server = smtplib.SMTP(
        SMTP_SERVER,
        SMTP_PORT
    )

    server.starttls()

    server.login(
        EMAIL,
        PASSWORD
    )

    server.sendmail(
        EMAIL,
        employee_email,
        msg.as_string()
    )
    print("Email successfully sent to:", employee_email)

    server.quit()
    print("SMTP connection closed.")

    return True