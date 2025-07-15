from decimal import Decimal
# 練習撰寫自己的模組
class IncomeIsNotNumber(ValueError):
    pass
TAX_RATE = {
    0 : Decimal('0.1'),
    10000 : Decimal('0.2'),
    50000 : Decimal('0.3'),
    100000 : Decimal('0.4'),
    500000 : Decimal('0.5')
}
def find_tax_rate(amount):
    result = Decimal('0.0')
    for income, rate in TAX_RATE.items():
        if amount >= income:
            result = rate
    return result
def caculate_tax(amount):
    if not (isinstance(amount, int) or isinstance(amount, float)):
        raise IncomeIsNotNumber('Parameter "amount" has to be a number')
    return float(Decimal(str(amount)) * find_tax_rate(amount))

