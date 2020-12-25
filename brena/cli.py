# todo: add cli handling mby api?
from typing import Optional

import typer

from brena.config import INVOICES
from brena.rendering import render_invoices

cli = typer.Typer()


# TODO: add statistics generation?
@cli.command()
def generate(invoice_codes: Optional[list[str]] = typer.Argument(None, help="Invoice codes separated by space")):
    """ Generate invoices with given codes. If no codes are provides, renders them all. """
    invoices_to_render = INVOICES
    if invoice_codes:
        invoices_to_render = {code: INVOICES[code] for code in invoice_codes}
    rendered_invoices = render_invoices(invoices_to_render)
    typer.echo("Rendered invoices:")
    typer.echo("\n".join(rendered_invoices))
