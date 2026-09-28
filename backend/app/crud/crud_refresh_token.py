from datetime import datetime, UTC
import uuid

from sqlalchemy.orm import Session

from app.models.refresh_token import RefreshToken


def store_refresh_token(
    db: Session,
    user_id: uuid.UUID,
    token: str,
    expires_at: datetime,
) -> RefreshToken:
    db_obj = RefreshToken(
        token=token,
        user_id=user_id,
        expires_at=expires_at,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_valid_refresh_token(db: Session, token: str) -> RefreshToken | None:
    db_token = (
        db.query(RefreshToken)
        .filter(RefreshToken.token == token, RefreshToken.revoked.is_(False))
        .first()
    )
    if db_token and db_token.expires_at > datetime.now(UTC):
        return db_token
    return None


def revoke_refresh_token(db: Session, token: str) -> None:
    db.query(RefreshToken).filter(RefreshToken.token == token).update({"revoked": True})
    db.commit()