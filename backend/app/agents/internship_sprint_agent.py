import json

from app.schemas.agent1 import StrategyRequest, SkillGapResult
from app.services.llm_client import get_llm_client
from app.utils.prompts import strategy_agent_prompt


class StrategyAgent:
    def __init__(self):
        self.llm = get_llm_client()

    def run(self, request: StrategyRequest) -> SkillGapResult:
        user_prompt = self._build_prompt(request)

        raw_response = self.llm.complete_json(
            system=strategy_agent_prompt,
            user=user_prompt,
        )

        parsed = self._safe_parse(raw_response)
        return SkillGapResult(**parsed)

    def _build_prompt(self, request: StrategyRequest) -> str:
        skills_line = (
            ", ".join(request.additional_skills)
            if request.additional_skills
            else "None provided — infer entirely from resume"
        )
        return f"""Target Role: {request.target_role}
Timeframe: {request.target_timeframe_weeks} weeks
Additional Self-Reported Skills: {skills_line}

--- JOB DESCRIPTION ---
{request.job_description}

--- CANDIDATE RESUME ---
{request.resume_text}
"""

    def _safe_parse(self, raw_response: str) -> dict:
        try:
            return json.loads(raw_response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Agent returned malformed JSON: {e}\nRaw: {raw_response[:500]}")