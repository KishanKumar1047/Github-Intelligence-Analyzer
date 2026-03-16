from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(report):

    file = "developer_report.pdf"

    c = canvas.Canvas(file, pagesize=letter)

    y = 750

    for key,value in report.items():

        c.drawString(50,y,f"{key}: {value}")

        y -= 30

    c.save()

    return file