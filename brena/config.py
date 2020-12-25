import os

import toml

CONFIG_PATH: str = "brena.toml"
config: dict = toml.load(CONFIG_PATH)

PACKAGE_LOCATION: str = os.path.split(os.path.realpath(__file__))[0]
TEMPLATE_DIR: str = os.path.join(PACKAGE_LOCATION, "invoice_templates")

COMPANIES = config["companies"]
SELLER = COMPANIES["default"]
INVOICES = {invoice["code"]: invoice for invoice in config["invoices"]}

# TODO: think if you should change the keys to slugs and move "pl" to the dict
I18N: dict = {
    "Sprzedawca": {"en": "Seller"},
    "Nabywca": {"en": "Buyer"},
    "Faktura nr": {"en": "Invoice No."},
    "Data wystawienia": {"en": "Created at"},
    "Data sprzedaży": {"en": "Sold at"},
    "Termin płatności": {"en": "Payment due by"},
    "Metoda płatności": {"en": "Payment type"},
    "Przelew": {"en": "Wire"},
    "Lp.": {"en": "Pos."},
    "Nazwa": {"en": "Description"},
    "Stawka VAT": {"en": "VAT stake"},
    "Ilość": {"en": "Quantity"},
    "Cena jedn. netto": {"en": "Netto price"},
    "Wartość netto": {"en": "Total netto"},
    "Wartość VAT": {"en": "VAT amount"},
    "Wartość brutto": {"en": "Total gross"},
    "Razem": {"en": "Total"},
    "Łącznie do zapłaty": {"en": "Total due:"},
}
