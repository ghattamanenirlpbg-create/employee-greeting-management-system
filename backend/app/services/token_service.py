from datetime import datetime
from datetime import timedelta

import secrets


def generate_token():

    return secrets.token_urlsafe(32)


def get_expiry_date():

    return datetime.utcnow() + timedelta(days=5)