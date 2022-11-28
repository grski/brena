import os
from pathlib import Path

import toml
from yamldb import YamlDB

CONFIG_PATH: str = "brena.toml"
config: dict = toml.load(CONFIG_PATH)

PACKAGE_LOCATION: str = os.path.split(os.path.realpath(__file__))[0]
TEMPLATE_DIR: str = os.path.join(PACKAGE_LOCATION, "invoice_templates")

COMPANIES = config["companies"]
SELLER = COMPANIES["default"]
INVOICES = {invoice["code"]: invoice for invoice in config["invoices"]}

USER_DIRECTORY: Path = Path.home()
BRENA_DIRECTORY_NAME: str = ".brena"
BRENA_DIRECTORY: Path = USER_DIRECTORY / BRENA_DIRECTORY_NAME
BRENA_CONFIG: Path = BRENA_DIRECTORY / "brena.toml"

def create_config_directory() -> Path:
    """ Creates config directory where we will store all brena-related files. """
    try:
        Path.mkdir(BRENA_DIRECTORY, exist_ok=True)
        return BRENA_DIRECTORY
    except PermissionError as e:
        print(f"Permission error, can't reach {BRENA_DIRECTORY}, details: {e}")
        raise e


db = YamlDB
DEFAULT_COMPANY_SLUG = "default"
