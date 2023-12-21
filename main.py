import federal_tax_brackets as fed
import state_tax_brackets as state
import long_term_capital_gains as ltcg
import inflation
import retirement


def get_paycheck_income(gross_salary, federal_tax_bracket, state_tax_bracket, _401k_percent):
    if gross_salary == 0:
        return

    yearly_401k_contribution = (_401k_percent / 100) * gross_salary

    federal_taxes_paid = federal_tax_bracket.get_taxes_paid(gross_salary - yearly_401k_contribution)

    state_taxes_paid = state_tax_bracket.get_taxes_paid(gross_salary - yearly_401k_contribution)

    social_security_tax = gross_salary * .062

    medicare_tax = gross_salary * .0145

    net_salary = gross_salary - state_taxes_paid - federal_taxes_paid - social_security_tax - medicare_tax - yearly_401k_contribution

    print("Paycheck Gross Income is: ", '${:,.2f}'.format(gross_salary / 26))
    print("Paycheck 401k Contribution is: ", '${:,.2f}'.format(yearly_401k_contribution / 26))
    print("Paycheck Net Income is: ", '${:,.2f}'.format(net_salary / 26))
    print(" ")
    print("Paycheck Federal Taxes Paid is: ", '${:,.2f}'.format(federal_taxes_paid / 26))
    print("Paycheck Social Security Taxes Paid is: ", '${:,.2f}'.format(social_security_tax / 26))
    print("Paycheck Medicare Taxes Paid is: ", '${:,.2f}'.format(medicare_tax / 26))
    print("Paycheck State Taxes Paid is: ", '${:,.2f}'.format(state_taxes_paid / 26))


def get_yearly_ordinary_income(gross_salary, federal_tax_bracket, state_tax_bracket):
    if gross_salary == 0:
        return

    federal_taxes_paid = federal_tax_bracket.get_taxes_paid(gross_salary)

    state_taxes_paid = state_tax_bracket.get_taxes_paid(gross_salary)

    net_salary = gross_salary - state_taxes_paid - federal_taxes_paid

    print(" ")
    print("Yearly Gross Ordinary Income is: ", '${:,.2f}'.format(gross_salary))
    print("Yearly Net Ordinary Income is: ", '${:,.2f}'.format(net_salary))
    print("Yearly Ordinary Income Effective Tax Rate: ",
          '{:.2f}%'.format(((federal_taxes_paid + state_taxes_paid) / gross_salary) * 100))
    print(" ")
    print("Yearly Federal Taxes Paid is: ", '${:,.2f}'.format(federal_taxes_paid))
    print("Yearly State Taxes Paid is: ", '${:,.2f}'.format(state_taxes_paid))


if __name__ == '__main__':
    working_years = 32
    gross_salary = 125000
    yearly_trad_401k_contribution = 22500
    yearly_roth_401k_contribution = 0
    yearly_roth_ira_contribution = 0  # 6500
    yearly_trad_ira_contribution = 0
    expected_market_growth_rate = 5
    working_federal_tax_bracket = fed.fed_2023
    working_state_tax_bracket = state.state_2023
    retirement_federal_tax_bracket = fed.fed_2023
    retirement_state_tax_bracket = state.state_2023
    withdrawal_rate = 4
    yearly_brokerage_contribution = 0
    social_security_monthly_benefit = 2390
    state = retirement.State.GEORGIA

    print('${:,.2f}'.format(gross_salary) + ", Working in GA, contributing " + '${:,.2f}'.format(
        yearly_trad_401k_contribution) + " to Trad 401k, and Retiring in GA with a monthly SS income of " + '${:,.2f}'.format(
        social_security_monthly_benefit))
    my_life_example_1 = retirement.MyLife(working_years, gross_salary, yearly_trad_401k_contribution,
                                          yearly_roth_401k_contribution, yearly_trad_ira_contribution,
                                          yearly_roth_ira_contribution, expected_market_growth_rate,
                                          working_federal_tax_bracket, working_state_tax_bracket,
                                          retirement_federal_tax_bracket, retirement_state_tax_bracket, withdrawal_rate,
                                          yearly_brokerage_contribution, social_security_monthly_benefit, state)

    my_life_example_1.print_my_life(retirement.RetirementPrintType.PRINT_TAKE_HOME)

    print(" ")

    yearly_trad_401k_contribution = 0
    yearly_roth_401k_contribution = 15940.75
    print('${:,.2f}'.format(gross_salary) + ", Working in GA, contributing " + '${:,.2f}'.format(
        yearly_roth_401k_contribution) + " to Roth 401k, and Retiring in GA with a monthly SS income of " + '${:,.2f}'.format(
        social_security_monthly_benefit))
    my_life_example_2 = retirement.MyLife(working_years, gross_salary, yearly_trad_401k_contribution,
                                          yearly_roth_401k_contribution, yearly_trad_ira_contribution,
                                          yearly_roth_ira_contribution, expected_market_growth_rate,
                                          working_federal_tax_bracket, working_state_tax_bracket,
                                          retirement_federal_tax_bracket, retirement_state_tax_bracket, withdrawal_rate,
                                          yearly_brokerage_contribution, social_security_monthly_benefit, state)

    my_life_example_2.print_my_life(retirement.RetirementPrintType.PRINT_TAKE_HOME)









































    # local_gross_salary = 94500
    # local_401k_percent = 0

    # get_paycheck_income(local_gross_salary, fed.fed_2023, state.state_2023, local_401k_percent)
    # get_yearly_earned_income(local_gross_salary, fed.fed_2023, state.state_2023, local_401k_percent)
    # get_yearly_ordinary_income(89264.70, fed.fed_2023, state.state_2023)
    # get_yearly_ordinary_income(80268.17, fed.fed_2023, state.state_2023)

    # for tax in fed.federal_tax_bracket_list:
        # tax.print_effective_tax_info(inflation.get_inflation_adjusted_salary(89264.70, tax.year))
        # tax.print_effective_tax_info(inflation.get_inflation_adjusted_salary(3411677.78, tax.year))

    # fed.fed_2023.print_tax_info(gross_salary)
    # state.state_2023.print_tax_info(gross_salary)
    # fed.fed_2023.print_tax_info(gross_salary)
    # fed.fed_2023.print_tax_info(93500)
    # ltcg.ltcg_2023.print_tax_info(64611.16)

    # print_monthly_compound_interest(5, 100, 100, 10)
    # print_yearly_compound_interest(5, 100, 100, 10)
