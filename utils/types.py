from behave import register_type

def parse_dollar(amount):
    """
    Convert parsed amount into a dollar value.
    """
    return round(float(amount.strip('$')), 2)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Dollar=parse_dollar)
