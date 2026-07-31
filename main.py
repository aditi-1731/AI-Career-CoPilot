from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router

from app.core.exception_handlers import (
    user_exists_handler,
    invalid_credentials_handler,
)

from app.core.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
)

tags_metadata = [
    {
        "name": "Authentication",
        "description": "Register and login users.",
    }
]

app = FastAPI(
    title="AI Career Copilot API",
    version="0.1.0",
    description="Backend API for AI Career Copilot",
    openapi_tags=tags_metadata,
)

app.add_exception_handler(
    UserAlreadyExistsException,
    user_exists_handler,
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler,
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Career Copilot API 🚀"
    }

app.include_router(
    auth_router,
    prefix="/api/v1",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )