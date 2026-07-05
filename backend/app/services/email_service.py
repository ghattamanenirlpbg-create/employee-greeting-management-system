import os
import requests

from dotenv import load_dotenv

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
FROM_EMAIL = os.getenv("EMAIL_ADDRESS")


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
        <b>Note:</b> This link will expire automatically after 5 days.
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

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json",
    }
    
    print("FROM_EMAIL =", FROM_EMAIL)
    print("TO_EMAIL =", employee_email)
    
    payload = {
        "from": FROM_EMAIL,
        "to": [employee_email],
        "subject": subject,
        "html": html,
    }

    response = requests.post(
        "https://api.resend.com/emails",
        headers=headers,
        json=payload,
        timeout=30,
    )

    print("Resend Status:", response.status_code)
    print("Resend Response:", response.text)

    response.raise_for_status()

    return True