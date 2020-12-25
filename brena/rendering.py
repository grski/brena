from jinja2 import Template
from weasyprint import HTML

from brena.calculation import calculate_positions
from brena.config import COMPANIES, SELLER, config
from brena.i18n import get_secondary_language
from brena.jinja.utils import jinja_environment


def render_html_to_pdf(context: dict, template: str = "invoice.html"):
    template: Template = jinja_environment.get_template(template)
    invoice = context["invoice"]
    html_template = template.render(context)
    invoice_name = f"{''.join(char for char in invoice['code'] if char.isalnum())}.pdf"
    # Todo: add proper directory creation
    HTML(string=html_template).write_pdf(invoice_name)
    return invoice_name


def render_invoice(invoice):
    buyer = COMPANIES[invoice["company"]]
    context = {
        "seller": SELLER,
        "buyer": buyer,
        "invoice": calculate_positions(invoice),
        "primary_language": SELLER["language"],
        "secondary_language": get_secondary_language(invoice, buyer),
    }
    return render_html_to_pdf(context=context)


def render_all_invoices():
    invoices = config["invoices"]
    rendered_invoices = tuple(render_invoice(invoice) for invoice in invoices)
    return rendered_invoices
