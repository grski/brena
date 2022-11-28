from pathlib import Path

import typer
from yamldb import YamlDB

from brena.config import BRENA_CONFIG, create_config_directory


def create_database_file_if_doesnt_exist() -> Path:
    """ Create the database file if it doesn't exist. """
    try:
        Path.touch(BRENA_CONFIG, exist_ok=True)
        return BRENA_CONFIG
    except PermissionError as e:
        print(f"Permission error, can't reach {BRENA_CONFIG}, details: {e}")
        raise e


create_config_directory()
create_database_file_if_doesnt_exist()

database: YamlDB = YamlDB(filename=create_database_file_if_doesnt_exist())

companies: list[dict] = database.search("companies")
def get_invoices(company_name: str = None) -> dict[str: dict]:
    """ Returns list of all invoices. """
    invoices: dict = database["invoices"]
    if company_name:
        return {invoice["code"]: invoice for invoice in invoices if invoice["buyer-slug"] == company_name}
    return invoices

def get_default_seller() -> dict:
    try:
        return database["companies.default"]
    except KeyError:
        typer.echo("""
        Invoice has no seller and no default company is provided, please define it first.
        You can do that by either defining a seller on the invoice or running brena init
        """)
