#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

styles = getSampleStyleSheet()

def generate_report (attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_content = Paragraph(paragraph, styles["h5"])
    report.build([report_title, report_content])
