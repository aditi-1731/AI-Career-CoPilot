from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)

from app.core.enums import UserRole


class UserRegisterRequest(BaseModel):
    """Schema used to register a new user."""

    name: str = Field(
        min_length=2,
        max_length=100,
        description="Full name of the user",
        examples=["Aditi Tripathi"],
    )

    email: EmailStr = Field(
        examples=["aditi@gmail.com"],
    )

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password",
        examples=["StrongPassword@123"],
    )

    role: UserRole = Field(
        default=UserRole.STUDENT,
        description="Role assigned to the user",
    )


class UserLoginRequest(BaseModel):
    """Schema used for user login."""

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password",
    )


class UserResponse(BaseModel):
    """Schema returned after fetching user details."""

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    is_verified: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class MessageResponse(BaseModel):
    message: str