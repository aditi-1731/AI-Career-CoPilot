from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse

from fastapi.concurrency import run_in_threadpool
from app.services.llm_client import LLMUnavailableError

from app.api.v1.dependencies.auth import CurrentUser
from app.schemas.agent1 import StrategyRequest, SkillGapResult, ResumePdfRequest
from app.agents.internship_sprint_agent import StrategyAgent
from app.services.pdf_generator import generate_resume_pdf
from app.utils.resume_parser import extract_text_from_upload

router = APIRouter(prefix="/agents/strategy", tags=["agent1-strategy"])
agent = StrategyAgent()


@router.post("/analyze", response_model=SkillGapResult)
async def analyze_resume_gap(
    user: CurrentUser,
    target_role: str = Form(...),
    target_timeframe_weeks: int = Form(...),
    additional_skills: str = Form(""),
    job_description: str = Form(...),
    resume_text_pasted: str | None = Form(None),
    resume_file: UploadFile | None = File(None),
):
    if resume_file is not None:
        resume_text = await extract_text_from_upload(resume_file)
    elif resume_text_pasted:
        resume_text = resume_text_pasted
    else:
        raise HTTPException(status_code=400, detail="Provide either resume_file or resume_text_pasted.")

    request = StrategyRequest(
        target_role=target_role,
        target_timeframe_weeks=target_timeframe_weeks,
        additional_skills=[s.strip() for s in additional_skills.split(",") if s.strip()],
        job_description=job_description,
        resume_text=resume_text,
    )

    try:
        return await run_in_threadpool(agent.run, request)
    except LLMUnavailableError:
        raise HTTPException(
            status_code=503,
            detail="The AI service is busy right now. Please try again in a minute.",
        )
    except ValueError as e:
        raise HTTPException(status_code=502, detail=f"Strategy generation failed: {e}")

@router.post("/resume-pdf")
def download_strategy_pdf(payload: ResumePdfRequest, user: CurrentUser):
    pdf_buffer = generate_resume_pdf(
        full_name=user.name,
        target_role=payload.target_role,
        original_resume_text=payload.resume_text,
        recommended_bullets=payload.recommended_resume_bullets,
    )

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{user.name}_resume_strategy.pdf"'},
    )