from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)

from app.core.enums import UserRole

class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
class UserRegisterRequest(BaseSchema):
    """Schema used to register a new user."""
    name: str = Field(
        min_length=2,
        max_length=100,
        description="Full name of the user",
        json_schema_extra={
            "example": "Aditi Tripathi"
        },
    )

    email: EmailStr = Field(
        json_schema_extra={
            "example": "aditi@gmail.com"
        }
    )

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password",
        json_schema_extra={
            "example": "StrongPassword@123"
        },
    )

    role: UserRole = Field(
        default=UserRole.STUDENT,
        description="Role assigned to the user",
    )
    
class UserLoginRequest(BaseSchema):
    """Schema used for user login."""
    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password",
    )

class UserResponse(BaseSchema):
    """Schema returned after fetching user details."""
    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    is_verified: bool

class TokenResponse(BaseSchema):
    access_token: str
    token_type: str = Field(default="bearer")

class MessageResponse(BaseSchema):
    message: str
