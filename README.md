# Brena
Nerdy CLI invoice generator. Brena generates invoices based on a .toml file you define.
You can do everything in the terminal. No need to open your browser and trouble yourself. Add a few lines and be done! 

Why you might ask? Because I hate to leave the terminal - that's it!

## Installation
To install it type:
```bash
pip install brena
```
and you are done. Brena depends on [weasyprint](https://github.com/Kozea/WeasyPrint/), so you might be required to install additional requirements. Look at [weasyprint docs](https://weasyprint.readthedocs.io/en/stable/).
You probably may need to run (ubuntu)
```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0
```
just to be sure check out the page linked above.
If you don't want to do that - check out the docker option.

## Usage
If you have defined your `brena.toml` file (how to do it is shown below), then you can just:
```bash
brena
```
To generate all the invoices or
```bash
brena invoicecode1 invoicecode2
```
To generate only invoices with specific codes.

You can read a bit more about available commands after typing
```bash
brena --help
```
## Usage
First of all you need to initialise the application by running 
```bash
brena init
```
This will create your local database and prompt you to enter your company's details.
You will be prompted to answer the following questions:
```
brena init
------
Enter the company name: The Engineers Ltd
Enter first address line: Magic Street 4/10
Enter second address line: 01-100 Warsaw
Enter tax identification number: PL9831234008
Enter default language: pl
Enter the bank account number: PL42 1111 0000 2222 0000 2222 0000
Would you like to add another bank account? (yes/no): yes
Enter your bank account: PL41 1111 0000 2222 0000 2222 0000
Would you like to add another bank account? (yes/no): no
Default company information saved, thank you.
```
This will set up the database and save your company's information. All the records are stored locally.
No information leaves your machine.

Now you might want to add some clients to be able to create an invoice. You can do that with
```bash
brena client add
```
Which will prompt:
```
brena client add
------
Enter the slug that will identify the client: some-corp
Enter the company name: Some Corp sp. z o. o.
Enter first address line: Magic Street 4/10
Enter second address line: 01-100 Warsaw
Enter tax identification number: PL9831234008
Enter default language: pl
Enter the bank account number: PL42 1111 0000 2222 0000 2222 0000
Would you like to add another bank account? (yes/no): yes
Enter your bank account: PL41 1111 0000 2222 0000 2222 0000
Would you like to add another bank account? (yes/no): no
```

Now you are all set up. You can add an invoice with:
```bash
brena invoice add
```
Which will result in you getting prompted:

```
brena invoice add
----
Seller slug (leave empty to use default):
Buyer slug: some-corp
Language - currently supported are [pl, en] (leave empty to use default): en
Code: A1/10/2022
Issue date: 2022-10-10
Sold date: 2022-10-10
Due to date (leave empty to not include): 2022-10-30
Currency: PLN
Invoice position name: Software development
Quantity: 10
Amount: 150
Vat stake: 23
--
Added entry. To stop adding entries hit ctrl-c
(...)
Entry added to db.
```
Now you can generate all the invoices with `brena generate` or a list of invoices with `brena generate code1 code2`


## Config: brena.toml
Below you can see an example of the required `brena.toml` file.
Brena expects this file to be found in current working directory.

``` toml
[companies.default]  # important to keep it as default 
  name = "Name Of Your Company"
  address_line_1 = "Some streeet 8/10"
  address_line_2 = "11-111 Some City"
  nip = "Your tax id number here if any"
  language = "pl"
  bank_accounts = { PLN = "PL11 1111 1111 1111 1111", EUR = "PL11 1111 1111 1111 1111" }

[companies.someclient]
  name = "Some Client Sp. z o. o."
  address_line_1 = "Another street"
  address_line_2 = "01-111 Warsaw"
  nip = "Your clients tax id if any"


[[invoices]]
  code = "01/12/2020"
  company = "someclient"
  currency = "PLN" # this value needs to be found in bank_accounts keys
  language = "pl"  # for now we only support pl and en
  dates = { issued = "2020-12-25", sold = "2020-12-31", due_to = "2021-01-15"}

  [[invoices.positions]]
    name = "IT service"
    quantity = 1
    amount = 15000
    vat_stake = 23


[[invoices]]
  code = "02/12/2020"
  company = "someclient"
  currency = "EUR"
  language = "en"
  dates = { issued = "2020-12-25", sold = "2020-12-31", due_to = "2021-01-10"}

  [[invoices.positions]] 
    name = "IT services"
    quantity = 172.5
    amount = 85.2
    vat_stake = 23
  
  [[invoices.positions]] 
    name = "Additional invoice position"
    quantity = 1
    amount = 82
    vat_stake = 23
```
For now I only support toml, maybe yaml in the future. Why toml over yaml? No reason, just my preference in this case.

# Technology
This bases on
[toml](https://github.com/uiri/toml), [weasyprint](https://github.com/Kozea/WeasyPrint/) and [jinja2](https://github.com/pallets/jinja).

Toml is used for configuration.
weasyprint gets the html template rendered to pdf.
Lastly jinja2 to add some contexts here and there.

Formatting of the code is done using [black](https://github.com/psf/black), [isort](https://github.com/timothycrosley/isort).
[flake8](https://gitlab.com/pycqa/flake8), [autoflake](https://github.com/myint/autoflake) and [bandit](https://github.com/PyCQA/bandit/) to check for potential vulns.

Versioning is done with [bumpversion](https://github.com/peritus/bumpversion).
Patch for merges to develop, minor for merged to master. Merge to master means release to pypi.

And wonderful [poetry](https://github.com/python-poetry/poetry) as dependency manager.

CLI is done with [typer](https://github.com/tiangolo/typer) <- wonderful CLI library.

I use type hinting where it's possible.

To start developing you need to install poetry
`pip install poetry` and then just `poetry install`. 

## Docker 
This application is fully dockerized. If you do not wish to download all the deps and install it, you can use the docker image provided.
[Brena docker image](https://hub.docker.com/r/grski/brena)

If you have readlink and are on Linux, then, assuming `brena.toml` is in current working dir, just go with:
```bash
docker run -v `readlink -f .`:/app/ grski/brena
```
otherwise:

```bash
docker run -v /home/grski/directorywherebrenatomlis/:/app/ grski/brena
```

or if you want to customize the command a bit and maybe generate only selected invoices with given codes:
```bash
docker run -v /home/grski/directorywherebrenatomlis/:/app/ grski/brena sh -c "python -m brena somecode1 somecode2"
```

TODO: describe precedence language

## Known make commands
```bash
flake
isort
isort-inplace
bandit
black
linters
bumpversion
black-inplace
autoflake-inplace
format-inplace
```
Most important ones are `make linters` and `make format-inplace`. Before each commit it's required to run these checks.

## License
MIT

