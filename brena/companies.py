import typer

from brena.config import DEFAULT_COMPANY_SLUG
from brena.database import database

app = typer.Typer()




def ask_company_data(is_buyer: bool = False) -> dict:
    company_name: str = input("Enter the company name: ")
    first_address_line: str = input("Enter first address line: ")
    second_address_line: str = input("Enter second address line: ")
    tax_id: str = input("Enter tax id: ")
    language: str = input("Enter default language: ")
    company_data: dict[str, str] = {
        "company_name": company_name,
        "first_address_line": first_address_line,
        "second_address_line": second_address_line,
        "tax_id": tax_id,
        "language": language,
        "bank_account": None,
        "slug": DEFAULT_COMPANY_SLUG,
    }
    if not is_buyer:
        company_data["bank_account"] = input("Enter bank account: ")
        return company_data
    company_data["slug"] = input("Enter company slug: ")
    return company_data

@app.command(help="Adds new company to the database.")
def add():
    """ Add new company to the database. """
    new_company: dict[str, str] = ask_company_data(is_buyer=True)
    database[f"companies.{new_company['slug']}"] = new_company
    database.save()
