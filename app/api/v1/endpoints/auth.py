from sqlalchemy.orm import Session

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.database.database import get_db

from app.schemas.user import (
    UserRegisterRequest,
    UserLoginRequest,
    UserResponse,
    TokenResponse,
)

from app.services.auth_services import (
    register_user,
    login_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    responses={
        201: {
            "description": "User registered successfully",
        },
        409: {
            "description": "User already exists",
        },
    },
)
def register(
    user_data: UserRegisterRequest,
    db: Session = Depends(get_db),
):
    """
    Register a new user.
    """
    return register_user(
        db,
        user_data,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Login user",
    responses={
        200: {
            "description": "Login successful",
        },
        401: {
            "description": "Invalid email or password",
        },
    },
)
def login(
    credentials: UserLoginRequest,
    db: Session = Depends(get_db),
):
    """
    Authenticate user and return JWT.
    """
    return login_user(
        db,
        credentials,
    )