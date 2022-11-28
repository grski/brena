from datetime import datetime, timedelta
# TODO: fetch exchange rates from NBP
from decimal import Decimal

today: datetime = datetime.today()
shift: timedelta = timedelta(max(1, (today.weekday() + 6) % 7 - 3))
previous_business_day: datetime = today - shift


def money_formatter(value, places=2, curr="", sep=" ", dp=",", pos="", neg="-", trailneg=""):
    """Convert Decimal to money formatted string.
    Source: Python docs

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (maywbe blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank
    """
    q = Decimal(10) ** -places  # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next_digit = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next_digit() if digits else "0")
    if places:
        build(dp)
    if not digits:
        build("0")
    i = 0
    while digits:
        build(next_digit())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return "".join(reversed(result))
