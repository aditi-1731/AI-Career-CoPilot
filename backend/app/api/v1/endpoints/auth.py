from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserRegisterRequest, UserLoginRequest, UserResponse, TokenResponse
from app.schemas.auth import TokenPair, RefreshRequest
from app.crud.user import get_user_by_email
from app.services.auth_services import (
    register_user,
    login_user,
    issue_token_pair,
    refresh_access_token,
    logout_user,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenPair, status_code=status.HTTP_201_CREATED)
def register(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    register_user(db, payload)
    user = get_user_by_email(db, payload.email)
    return issue_token_pair(db, user)


@router.post("/login", response_model=TokenPair)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    credentials = UserLoginRequest(email=form_data.username, password=form_data.password)
    login_user(db, credentials)  # raises InvalidCredentialsException on failure
    user = get_user_by_email(db, form_data.username)
    return issue_token_pair(db, user)


@router.post("/refresh", response_model=TokenResponse)
def refresh(payload: RefreshRequest, db: Session = Depends(get_db)):
    return refresh_access_token(db, payload.refresh_token)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(payload: RefreshRequest, db: Session = Depends(get_db)):
    logout_user(db, payload.refresh_token)