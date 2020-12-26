from brena.config import SELLER


def get_translation(text: str, language: str) -> str:
    # TODO: handle failing gracefully?
    return I18N[text][language]


def get_secondary_language(invoice: dict, buyer: dict) -> str:
    return invoice.get("language") or buyer["language"] or SELLER.language


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
