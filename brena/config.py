import os

import toml

CONFIG_PATH: str = "brena.toml"
config: dict = toml.load(CONFIG_PATH)

PACKAGE_LOCATION: str = os.path.split(os.path.realpath(__file__))[0]
TEMPLATE_DIR: str = os.path.join(PACKAGE_LOCATION, "invoice_templates")

COMPANIES = config["companies"]
SELLER = COMPANIES["default"]
INVOICES = {invoice["code"]: invoice for invoice in config["invoices"]}
