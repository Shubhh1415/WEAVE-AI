from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_resume_report(report_text, filename="Resume_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):

        if line.strip():

            story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    return filename