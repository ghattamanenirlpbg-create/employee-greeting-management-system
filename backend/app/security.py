from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext


# ===========================
# Password Hashing
# ===========================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ===========================
# JWT Settings
# ===========================

SECRET_KEY = "change_this_to_a_long_random_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ===========================
# Hash Password
# ===========================

def hash_password(password: str):

    return pwd_context.hash(password)


# ===========================
# Verify Password
# ===========================

def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ===========================
# Create JWT Token
# ===========================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt