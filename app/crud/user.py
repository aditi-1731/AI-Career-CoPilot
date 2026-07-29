from uuid import UUID
from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy.exc import IntegrityError

def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    """
    Fetch a user by email.
    """

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

def get_user_by_id(
    db: Session,
    user_id: UUID,
) -> User | None:
    """
    Fetch user by UUID.
    """

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

def create_user(
    db: Session,
    user: User,
) -> User:
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        raise