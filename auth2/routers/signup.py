from string import ascii_letters, digits
from typing import Annotated

from fastapi import APIRouter, Depends, Body, HTTPException, status

from ..authenticate_user import hash_password
from ..jwt_token import create_access_token, create_refresh_token
from ...src.database.auth_db import AuthDB
from ...src.models.user import User

signup = APIRouter()


def is_password_strength(password: str):
    if len(password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The password length must be greater, than 8 digits"
            )
    if not all([any(i in password for i in ascii_letters), any(i in password for i in digits)]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "The password must contain BOTH letters and digits"
        )
    return password


@signup.post("/signup")
async def signup(
        username: Annotated[str, Body()],
        password: Annotated[str, Depends(is_password_strength), Body(description="Plaintext password")],
        email: Annotated[str, Body()]
):
    user = User(username=username, hashed_password=hash_password(password), email=email)
    result = AuthDB(
        user=,
        port=,
        host=,
        password=,
        database=,
    ).signup(username=user.username, password=user.hashed_password, email=user.email)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with the same username, password or email already exists"
        )
    access_token = create_access_token(
        payload_data={
            "username": user.username,
            "hashed_password": user.hashed_password,
        }
    )
    refresh_token = create_refresh_token(
        payload_data={
            "username": user.username,
            "hashed_password": user.hashed_password,
        }
    )
    return access_token, refresh_token
