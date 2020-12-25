from jinja2 import Environment, FileSystemLoader

from brena.config import TEMPLATE_DIR
from brena.jinja import filters


def add_additional_filters_to_environment(environment: Environment) -> Environment:
    """ Adding additional filters that begin with jinja_ prefix and are defined in filters.py file"""
    additional_filters: dict = {
        jinja_filter: getattr(filters, jinja_filter)
        for jinja_filter in dir(filters)
        if jinja_filter.startswith("jinja_")
    }
    for filter_name, filter_function in additional_filters.items():
        environment.filters[filter_name.replace("jinja_", "")] = filter_function
    return environment


jinja_environment: Environment = add_additional_filters_to_environment(
    Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=False)  # nosec
)
