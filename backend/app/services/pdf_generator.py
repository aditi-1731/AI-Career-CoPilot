from io import BytesIO
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib import colors

def generate_resume_pdf(
    full_name: str,
    target_role: str,
    original_resume_text: str,
    recommended_bullets: list[str],
) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=LETTER, topMargin=0.75 * inch, bottomMargin=0.75 * inch)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("TitleStyle", parent=styles["Title"], textColor=colors.HexColor("#1a1a2e"))
    heading_style = ParagraphStyle(
        "SectionHeading", parent=styles["Heading2"],
        textColor=colors.HexColor("#16213e"), spaceBefore=14, spaceAfter=6,
    )
    body_style = styles["BodyText"]

    story = [
        Paragraph(full_name, title_style),
        Paragraph(f"Target Role: {target_role}", styles["Italic"]),
        Spacer(1, 0.2 * inch),
        Paragraph("Suggested Additions (ATS-Optimized)", heading_style),
        ListFlowable(
            [ListItem(Paragraph(bullet, body_style)) for bullet in recommended_bullets],
            bulletType="bullet",
        ),
        Spacer(1, 0.2 * inch),
        Paragraph("Original Resume Content", heading_style),
    ]

    for paragraph_text in original_resume_text.split("\n"):
        if paragraph_text.strip():
            story.append(Paragraph(paragraph_text, body_style))
            story.append(Spacer(1, 0.08 * inch))

    doc.build(story)
    buffer.seek(0)
    return buffer