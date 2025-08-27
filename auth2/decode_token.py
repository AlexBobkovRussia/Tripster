import os
from datetime import datetime
from typing import Annotated

import jwt
from dotenv import load_dotenv, find_dotenv
from fastapi import HTTPException, status, Depends
from jwt.exceptions import InvalidTokenError
from typing_extensions import Doc

load_dotenv(find_dotenv())


def check_token_validity(token: Annotated[
    str,
    Doc("Raw token")
],
                         secret_key: Annotated[
                             str,
                             Doc("A secret key, that was used to create a token")
                         ],
                         algorithm: Annotated[
                             str,
                             Doc("An algorithm, that was used to create a token")
                         ]) -> str:
    """This function check the validity of the token

    Args:

    Returns:

    Raises:

    """
    # TODO: Write a doc
    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    if payload.get("exp") is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Required parameter (exp) was not provided",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    if datetime.now() < payload.get("exp"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Token is expired",
                            headers={"WWW-Authentication": "Bearer"}
                            )
    if jwt.encode(payload, secret_key, algorithm=algorithm) == token:
        raise InvalidTokenError
    return True


def decode_token(token: Annotated[str, Depends(check_token_validity)]) -> dict:
    """THis function decodes jwt token

    Args:
        token (str) : token

    Returns:
        dict : a payload of token

    Raises:
        HTTPException : When program can not decode jwt token
    """
    payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
    # TODO: do it with a DB
    # username = payload.get("sub")
    # if username is None:
    #     raise credentials_exception
    return payload
