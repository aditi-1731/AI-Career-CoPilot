class UserAlreadyExistsException(Exception):
    """Raised when the email is already registered."""
    pass


class InvalidCredentialsException(Exception):
    """Raised when login credentials are invalid."""
    pass


class InvalidRefreshTokenException(Exception):
    """Raised when a refresh token is missing, expired, or revoked."""
    pass