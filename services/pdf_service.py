from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


# ===========================
# Resume Analyzer PDF
# ===========================

def create_resume_report(report_text, filename="Resume_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):

        if line.strip():
            story.append(
                Paragraph(line, styles["BodyText"])
            )

    doc.build(story)

    return filename


# ===========================
# Job Match Report PDF
# ===========================

def generate_match_report_pdf(data, filename="Resume_Match_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # Title
    story.append(
        Paragraph(
            "<b>Resume Match Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Match Score:</b> {data.get('score',0)}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    # Matching Skills
    story.append(
        Paragraph(
            "<b>Matching Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in data.get("matching_skills", []):

        story.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    # Missing Skills
    story.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in data.get("missing_skills", []):

        story.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    # Suggestions
    story.append(
        Paragraph(
            "<b>Suggestions</b>",
            styles["Heading2"]
        )
    )

    for suggestion in data.get("suggestions", []):

        story.append(
            Paragraph(
                f"• {suggestion}",
                styles["BodyText"]
            )
        )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    # Recommendation
    story.append(
        Paragraph(
            "<b>Final Recommendation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            data.get("recommendation", ""),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename