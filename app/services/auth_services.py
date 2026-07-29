from sqlalchemy.orm import Session

from app.crud.user import (
    create_user,
    get_user_by_email,
)

from app.models.user import User

from app.schemas.user import (
    UserRegisterRequest,
    UserLoginRequest,
    UserResponse,
    TokenResponse,
)

from app.security.hashing import (
    hash_password,
    verify_password,
)

from app.security.jwt import create_access_token

from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
)

def register_user(
    db: Session,
    user_data: UserRegisterRequest,
) -> UserResponse:
    """
    Register a new user.
    """

    existing_user = get_user_by_email(
        db,
        user_data.email,
    )

    if existing_user:
        raise UserAlreadyExistsException

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hash_password(
            user_data.password
        ),
        role=user_data.role,
    )

    created_user = create_user(
        db,
        user,
    )

    return UserResponse.model_validate(
        created_user
    )

def login_user(
    db: Session,
    credentials: UserLoginRequest,
) -> TokenResponse:
    """
    Authenticate a user.
    """

    user = get_user_by_email(
        db,
        credentials.email,
    )

    if user is None:
        raise InvalidCredentialsException

    if not verify_password(
        credentials.password,
        user.password_hash,
    ):
        raise InvalidCredentialsException

    token = create_access_token(
        subject=user.email,
    )

    return TokenResponse(
        access_token=token,
    )