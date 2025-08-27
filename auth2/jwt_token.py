import os
from datetime import datetime, timezone, timedelta

import jwt
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def create_access_token(
        payload_data: dict,
        expire_time: timedelta | None = None
) -> str:
    """This function create a jwt ACCESS token.

    Args:
        payload_data (dict) : what will be encoded in jwt token
        expire_time (timedelta | None) : a life time of token, e.g. 5 min, 10 min
            If expire_time is provided, provided value will be used, else 15 minutes

    Returns:
        str : a jwt token

    Raises:
        TypeError : if payload is not a dict
        TypeError : if expire_time is not a timedelta or None
    """
    if not isinstance(payload_data, dict):
        raise TypeError("A payload_data must be a User")
    if not isinstance(expire_time, timedelta) and expire_time is not None:
        raise TypeError("An expire_time must be timedelta or None")
    if expire_time is not None:
        payload_data.update(
            {"exp": datetime.now(timezone.utc) + expire_time}
        )
    else:
        payload_data.update(
            {"exp": datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))}
        )
    token = jwt.encode(
        payload_data,
        os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )
    return token


def create_refresh_token(
        payload_data: dict,
        expire_time: timedelta | None = None
) -> str:
    """This function create a jwt REFRESH token.

    Args:
        payload_data (dict) : what will be encoded in jwt token
        expire_time (timedelta | None) : a life time of token, e.g. 5 min, 10 min
            If expire_time is provided, provided value will be used, else 15 minutes

    Returns:
        str : a jwt token

    Raises:
        TypeError : if payload is not a dict
        TypeError : if expire_time is not a timedelta or None
    """
    if not isinstance(payload_data, dict):
        raise TypeError("A payload_data must be a User")
    if not isinstance(expire_time, timedelta) and expire_time is not None:
        raise TypeError("An expire_time must be timedelta or None")
    if expire_time is not None:
        payload_data.update(
            {"exp": datetime.now(timezone.utc) + expire_time}
        )
    else:
        payload_data.update(
            {"exp": datetime.now(timezone.utc) + timedelta(days=int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")))}
        )
    token = jwt.encode(
        payload_data,
        os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )
    return token
