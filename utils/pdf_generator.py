from fpdf import FPDF
import os

def generate_invoice_pdf(data):
    pdf = FPDF()
    pdf.add_page()

    # Load Unicode font
    font_path = os.path.join(os.path.dirname(__file__), "..", "fonts", "DejaVuSans.ttf")
    print(f"Loading font from: {font_path}")
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    # Header
    pdf.set_font("DejaVu", "", 16)
    pdf.cell(200, 10, txt="INVOICE", ln=True, align="C")
    pdf.set_font("DejaVu", size=12)

    # Sender and Client Info
    pdf.ln(10)
    pdf.cell(100, 10, f"From: {data['sender']['name']}")
    pdf.cell(100, 10, f"To: {data['client']['name']}", ln=True)

    pdf.cell(100, 10, f"{data['sender']['address']}")
    pdf.cell(100, 10, f"{data['client']['address']}", ln=True)

    pdf.cell(100, 10, f"{data['sender']['email']}")
    pdf.cell(100, 10, f"{data['client']['email']}", ln=True)

    pdf.ln(5)
    pdf.cell(100, 10, f"Invoice #: {data['invoice_number']}")
    pdf.cell(100, 10, f"Issue Date: {data['issue_date']}", ln=True)
    pdf.cell(100, 10, f"Due Date: {data['due_date']}", ln=True)

    # Items table
    pdf.ln(10)
    pdf.set_font("DejaVu", "", 12)
    pdf.cell(100, 10, "Description")
    pdf.cell(30, 10, "Qty")
    pdf.cell(30, 10, "Price")
    pdf.cell(30, 10, "Total", ln=True)

    subtotal = 0
    for item in data['items']:
        total = item['quantity'] * item['price']
        subtotal += total
        pdf.cell(100, 10, item['description'])
        pdf.cell(30, 10, str(item['quantity']))
        pdf.cell(30, 10, f"€{item['price']:.2f}")
        pdf.cell(30, 10, f"€{total:.2f}", ln=True)

    tax = subtotal * data['tax_rate'] / 100
    total = subtotal + tax

    pdf.ln(5)
    pdf.cell(160, 10, "Subtotal", align='R')
    pdf.cell(30, 10, f"€{subtotal:.2f}", ln=True)
    pdf.cell(160, 10, f"Tax ({data['tax_rate']}%)", align='R')
    pdf.cell(30, 10, f"€{tax:.2f}", ln=True)
    pdf.cell(160, 10, "Total", align='R')
    pdf.cell(30, 10, f"€{total:.2f}", ln=True)

    if data['notes']:
        pdf.ln(10)
        pdf.set_font("DejaVu", "", 11)
        pdf.multi_cell(0, 10, f"Notes:\n{data['notes']}")

    pdf.output("invoice.pdf")
