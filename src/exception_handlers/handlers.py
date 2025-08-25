from fastapi import Request
from fastapi.responses import PlainTextResponse
from jwt.exceptions import InvalidTokenError

from src.app.main import app


@app.exception_handler(TypeError)
async def typeerror_handler(req: Request, exc: TypeError):
    return PlainTextResponse(str(exc))


@app.exception_handler(InvalidTokenError)
async def invalidtokenerror_handler(req: Request, exc: InvalidTokenError):
    return PlainTextResponse(str(exc))