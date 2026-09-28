import io
import pdfplumber
from docx import Document
from fastapi import UploadFile, HTTPException

SUPPORTED_TYPES = {
    "application/pdf": "pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    "text/plain": "txt",
}

async def extract_text_from_upload(file: UploadFile) -> str:
    if file.content_type not in SUPPORTED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{file.content_type}'. Use PDF, DOCX, or TXT, or paste text instead.",
        )

    raw = await file.read()
    file_type = SUPPORTED_TYPES[file.content_type]

    if file_type == "pdf":
        return _extract_pdf_text(raw)
    elif file_type == "docx":
        return _extract_docx_text(raw)
    else:
        return raw.decode("utf-8", errors="ignore")

def _extract_pdf_text(raw: bytes) -> str:
    text_chunks = []
    with pdfplumber.open(io.BytesIO(raw)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_chunks.append(page_text)
    text = "\n".join(text_chunks).strip()
    if not text:
        raise HTTPException(
            status_code=422,
            detail="Could not extract text from PDF — it may be a scanned image. Try pasting the text instead.",
        )
    return text

def _extract_docx_text(raw: bytes) -> str:
    doc = Document(io.BytesIO(raw))
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())