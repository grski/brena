from decimal import Decimal


def calculate_position(position):
    quantity = Decimal(position["quantity"])
    amount = Decimal(position["amount"])
    vat_stake = Decimal(f"0.{position['vat_stake']}")
    net = quantity * amount
    vat = net * vat_stake
    gross = net + vat
    return {**position, "quantity": quantity, "amount": amount, "gross": gross, "net": net, "vat": vat}


def calculate_total(positions: list):
    net, vat, gross = 0, 0, 0
    for position in positions:
        net += position["net"]
        vat += position["vat"]
        gross += position["gross"]
    return {"net": net, "vat": vat, "gross": gross}


def calculate_positions(invoice: dict):
    extend_postions = [calculate_position(position) for position in invoice["positions"]]
    invoice["positions"] = extend_postions
    invoice["total"] = calculate_total(invoice["positions"])
    return invoice
