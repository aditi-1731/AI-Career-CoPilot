import uuid
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Integer,
    Text,
    Enum,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base_model import BaseModel

from app.core.enums import (
    ExperienceLevel,
    JobType,
    WorkMode
)

if TYPE_CHECKING:
    from app.models.user import User
    
class UserProfile(BaseModel):
    __tablename__ = "user_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    current_status: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    target_role: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    experience_level: Mapped[ExperienceLevel] = mapped_column(
        Enum(
            ExperienceLevel,
            name="experience_level_enum",
        ),
        nullable=False,
    )

    preferred_location: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    work_mode: Mapped[WorkMode] = mapped_column(
        Enum(
            WorkMode,
            name="work_mode_enum",
        ),
        nullable=False,
    )

    preferred_job_type: Mapped[JobType] = mapped_column(
        Enum(
            JobType,
            name="job_type_enum",
        ),
        nullable=False,
    )

    min_salary: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    max_salary: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    timeframe_days: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    portfolio_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    career_goal: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    skills: Mapped[list[str] | None] = mapped_column(
        ARRAY(String),
        nullable=True,
    )
    # One-to-one relationship with User
    user: Mapped["User"] = relationship(
        back_populates="profile",
        lazy="selectin",
    )

