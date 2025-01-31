from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_attendance_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    num_boxes = 152
    boxes_per_page = 4

    box_width = width / 2
    box_height = height / 2

    for i in range(0, num_boxes, boxes_per_page):
        for j in range(boxes_per_page):
            if i + j >= num_boxes:
                break
            x = (j % 2) * box_width
            y = height - (j // 2) * box_height - box_height

            # Draw the number in the center of the box
            c.setFont("Helvetica-Bold", 80)
            c.drawCentredString(x + box_width / 2, y + box_height / 2, str(i + j + 1))

            # Draw the labels for the small boxes
            c.setFont("Helvetica", 12)
            c.drawCentredString(x + box_width / 2 - 30, y + 60, "Judge One")
            c.drawCentredString(x + box_width / 2 + 40, y + 60, "Judge Two")

            # Draw the small boxes for attendance
            small_box_size = 30
            c.setLineWidth(1)
            c.rect(x + box_width / 2 - 40, y + 20, small_box_size, small_box_size, stroke=1, fill=0)
            c.rect(x + box_width / 2 + 20, y + 20, small_box_size, small_box_size, stroke=1, fill=0)
        
        c.showPage()

    c.save()

create_attendance_pdf("attendance_boxes.pdf")
