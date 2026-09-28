from datetime import datetime, timedelta, UTC
from sqlalchemy.orm import Session

from app.crud.user import (
    create_user,
    get_user_by_email,
)
from app.crud.crud_refresh_token import (
    store_refresh_token,
    get_valid_refresh_token,
    revoke_refresh_token,
)

from app.models.user import User

from app.schemas.user import (
    UserRegisterRequest,
    UserLoginRequest,
    UserResponse,
    TokenResponse,
)
from app.schemas.auth import TokenPair

from app.security.hashing import (
    hash_password,
    verify_password,
)

from app.security.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
)

from app.core.config import settings
from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    InvalidRefreshTokenException,
)


def register_user(db: Session, user_data: UserRegisterRequest) -> UserResponse:
    """Register a new user."""
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise UserAlreadyExistsException

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        role=user_data.role,
    )
    created_user = create_user(db, user)
    return UserResponse.model_validate(created_user)


def login_user(db: Session, credentials: UserLoginRequest) -> TokenResponse:
    """Authenticate a user."""
    user = get_user_by_email(db, credentials.email)
    if user is None:
        raise InvalidCredentialsException

    if not verify_password(credentials.password, user.password_hash):
        raise InvalidCredentialsException

    token = create_access_token(subject=user.email)
    return TokenResponse(access_token=token)


# --- New: refresh-token issuance, used by /login and /register ---

def issue_token_pair(db: Session, user: User) -> TokenPair:
    """Issue an access + refresh token pair for an authenticated user."""
    access = create_access_token(subject=user.email)
    refresh = create_refresh_token(subject=user.email)

    expires_at = datetime.now(UTC) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    store_refresh_token(db, user_id=user.id, token=refresh, expires_at=expires_at)

    return TokenPair(access_token=access, refresh_token=refresh)


def refresh_access_token(db: Session, refresh_token: str) -> TokenResponse:
    """Issue a new access token given a valid, unrevoked refresh token."""
    db_token = get_valid_refresh_token(db, refresh_token)
    if db_token is None:
        raise InvalidRefreshTokenException

    decoded = decode_token(refresh_token)
    if not decoded or decoded.get("type") != "refresh":
        raise InvalidRefreshTokenException

    new_access = create_access_token(subject=decoded["sub"])
    return TokenResponse(access_token=new_access)


def logout_user(db: Session, refresh_token: str) -> None:
    """Revoke a refresh token, ending the session."""
    revoke_refresh_token(db, refresh_token)