from jinja2 import pass_context

from brena.currency import money_formatter
from brena.i18n import get_translation


# IMPORTANT: every registered filter must start with the phrase 'jinja_'
@pass_context
def jinja_currency(context: dict, value: str, *args) -> str:
    """
    Formats to a currency standard. TODO: add getting currency from context and stuff
    """
    return money_formatter(value)


@pass_context
def jinja_i18n(context: dict, value: str, *args):
    if context["secondary_language"] == context["primary_language"]:
        return value
    translated_value: str = get_translation(value, context["secondary_language"])
    return f"{value} / {translated_value}"
