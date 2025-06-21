from utils.pdf_generator import generate_invoice_pdf

def get_invoice_data():
    print("\n🧾 Welcome to Your Invoice Generator\n")

    sender_name = input("Your name or company: ")
    sender_address = input("Your address: ")
    sender_email = input("Your email: ")

    client_name = input("Client's name: ")
    client_address = input("Client's address: ")
    client_email = input("Client's email: ")

    invoice_number = input("Invoice number (e.g. 0001): ")
    issue_date = input("Issue date (YYYY-MM-DD): ")
    due_date = input("Due date (YYYY-MM-DD): ")

    items = []
    print("Enter invoice items (type 'done' to finish):")
    while True:
        description = input("  Description: ")
        if description.lower() == 'done':
            break
        quantity = int(input("  Quantity: "))
        price = float(input("  Unit price (EUR): "))
        items.append({
            "description": description,
            "quantity": quantity,
            "price": price
        })

    tax_rate = float(input("Tax rate (e.g. 19 for 19%): "))

    notes = input("Optional notes (press Enter to skip): ")

    return {
        "sender": {
            "name": sender_name,
            "address": sender_address,
            "email": sender_email
        },
        "client": {
            "name": client_name,
            "address": client_address,
            "email": client_email
        },
        "invoice_number": invoice_number,
        "issue_date": issue_date,
        "due_date": due_date,
        "items": items,
        "tax_rate": tax_rate,
        "notes": notes
    }

if __name__ == "__main__":
    invoice_data = get_invoice_data()
    generate_invoice_pdf(invoice_data)
    print("✅ Invoice generated successfully as invoice.pdf!")
