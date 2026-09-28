from pydantic import BaseModel

from app.schemas.user import TokenResponse


class TokenPair(TokenResponse):
    """Extends TokenResponse with a refresh token for login/register flows."""
    refresh_token: str


class RefreshRequest(BaseModel):
    refresh_token: str