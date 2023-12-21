import numpy_financial as npf


def get_monthly_compound_interest(rate, present_value, monthly_contribution, years):
    return npf.fv((rate / 100) / 12, years * 12, monthly_contribution * -1, present_value * -1)


def get_yearly_compound_interest(rate, present_value, monthly_contribution, years):
    return npf.fv((rate / 100), years, monthly_contribution * 12 * -1, present_value * -1)


def print_monthly_compound_interest(rate, present_value, monthly_contribution, years):
    print('${:,.2f}'.format(get_monthly_compound_interest(rate, present_value, monthly_contribution, years)))


def print_yearly_compound_interest(rate, present_value, monthly_contribution, years):
    print('${:,.2f}'.format(get_yearly_compound_interest(rate, present_value, monthly_contribution, years)))
