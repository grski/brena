from jinja2 import Template
from weasyprint import HTML

from brena.calculation import calculate_positions
from brena.config import COMPANIES, SELLER
from brena.i18n import get_secondary_language
from brena.jinja.utils import jinja_environment


def render_html_to_pdf(context: dict, template: str = "invoice.html"):
    template: Template = jinja_environment.get_template(template)
    invoice = context["invoice"]
    html_template = template.render(context)
    invoice_name = f"{''.join(char for char in invoice['code'] if char.isalnum())}.pdf"
    HTML(string=html_template).write_pdf(invoice_name)
    return invoice_name


def render_single_invoice(invoice):
    buyer: dict = COMPANIES[invoice["buyer"]]
    seller: dict = invoice.get("seller", )
    context = {
        "seller": SELLER,
        "buyer": buyer,
        "invoice": calculate_positions(invoice),
        "primary_language": SELLER["language"],
        "secondary_language": get_secondary_language(invoice, buyer),
    }
    return render_html_to_pdf(context=context)


def render_invoices(invoices: dict[str, dict]) -> tuple[str, ...]:
    rendered_invoices = tuple(render_single_invoice(invoice) for _, invoice in invoices.items())
    return rendered_invoices
