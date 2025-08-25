from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.models.token import Token
from .authenticate_user import authenticate_user
from .jwt_token import create_access_token, create_refresh_token

auth = FastAPI()

oauth2 = OAuth2PasswordBearer("token")


@auth.post("/token")
async def get_token(user: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user.model_dump())
    refresh_token = create_refresh_token(user.model_dump())
    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )
