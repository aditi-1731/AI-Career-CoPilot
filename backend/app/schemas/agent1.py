from pydantic import BaseModel, Field
from typing import Literal


class StrategyRequest(BaseModel):
    target_role: str
    target_timeframe_weeks: int = Field(ge=1, le=52)
    additional_skills: list[str] = Field(default_factory=list)
    job_description: str
    resume_text: str


class KeywordMatch(BaseModel):
    keyword: str
    category: Literal["hard_skill", "soft_skill"]
    present_in_resume: bool


class SkillGapResult(BaseModel):
    match_percentage: float = Field(ge=0, le=100)
    present_keywords: list[KeywordMatch]
    missing_keywords: list[KeywordMatch]
    strategy_summary: str
    recommended_resume_bullets: list[str]

class ResumePdfRequest(BaseModel):
    target_role: str
    resume_text: str
    recommended_resume_bullets: list[str]