from brena.config import I18N, SELLER


def get_translation(text: str, language: str) -> str:
    # TODO: handle failing gracefully?
    return I18N[text][language]


def get_secondary_language(invoice: dict, buyer: dict) -> str:
    return invoice.get("language") or buyer["language"] or SELLER.language
