from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    InvalidRefreshTokenException,
)


async def user_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException,
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": "User already exists."
        },
    )


async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException,
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail": "Invalid email or password."
        },
    )


async def invalid_refresh_token_handler(
    request: Request,
    exc: InvalidRefreshTokenException,
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail": "Invalid or expired refresh token."
        },
    )