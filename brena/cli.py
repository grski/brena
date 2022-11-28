# todo: add cli handling mby api?
from typing import Optional

import typer

from brena.companies import ask_company_data
from brena.companies import app as companies
from brena.invoices import app as invoices
from brena.config import INVOICES
from brena.database import get_invoices, database
from brena.rendering import render_invoices

cli = typer.Typer()

cli.add_typer(companies, name="companies", help="Manage companies in the database.")
cli.add_typer(invoices, name="invoices", help="Manage invoices in the database.")

@cli.command()
def generate(invoice_codes: Optional[list[str]] = typer.Argument(None, help="Invoice codes separated by space")):
    """ Generate invoices with given codes. If no codes are provides, renders them all. """
    invoices_to_render: dict[str, dict] = get_invoices()
    if invoice_codes:
        invoices_to_render = {code: INVOICES[code] for code in invoice_codes}
    rendered_invoices = render_invoices(invoices_to_render)
    typer.echo("Rendered invoices:")
    typer.echo("\n".join(rendered_invoices))


@cli.command(help="Initialise brena config.")
def init():
    database["companies.default"] = ask_company_data(is_buyer=False)
    database.save()
    typer.echo("Default company information saved.")


def edit_clients():
    pass

def add_invoice(entity_id: str = typer.Argument(None)):
    return entity_id

def edit_invoice():
    pass

def delete_invoice():
    pass
