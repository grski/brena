from decimal import Decimal

import typer

from brena.database import database

app = typer.Typer()

def ask_invoice_data() -> dict:
    code: str = input("Enter invoice code: ")
    buyer: str = input("Enter buyer slug: ")
    issued_at: str = input("Issued at: ")
    sold_at: str = input("Sold at: ")
    due_to: str = input("Due to: ")
    notes: str = input("Notes: ")

    name: str = input("Position name: ")
    quantity: Decimal = Decimal(input("Quantity: "))
    amount: Decimal = Decimal(input("Amount: "))
    vat_stake: str = input("VAT: ")
    if code in database.get("invoices", {}):
        raise Exception  # no duplicate codes for invoices allowed
    invoice: dict = {
        "code": code,
        "buyer": buyer,
        "issued_at": issued_at,
        "sold_at": sold_at,
        "due_to": due_to,
        "notes": notes,
        "positions": [
            {"name": name, "quantity": quantity, "amount": amount, "vat_stake": vat_stake},
        ]
    }
    return invoice

@app.command(help="Add new invoice data.")
def add():
    """ Add new invoice to the database."""
    new_invoice: dict = ask_invoice_data()
    database[f"invoices.{new_invoice['code']}"] = new_invoice
    database.save()
