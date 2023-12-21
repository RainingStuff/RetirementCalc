import interest
import federal_tax_brackets as fed
import state_tax_brackets as state
from enum import Enum
import social_security_taxes as ss


class RetirementPrintType(Enum):
    PRINT_ALL = 1
    PRINT_TAKE_HOME = 2
    PRINT_NONE = 3


class State(Enum):
    GEORGIA = 1
    NOT_GEORGIA = 2


class MyLife:
    def __init__(self, working_years, gross_salary, yearly_trad_401k_contribution, yearly_roth_401k_contribution,
                 yearly_trad_ira_contribution, yearly_roth_ira_contribution, expected_market_growth_rate,
                 working_federal_tax_bracket, working_state_tax_bracket, retirement_federal_tax_bracket,
                 retirement_state_tax_bracket, withdrawal_rate, yearly_brokerage_contribution,
                 social_security_monthly_benefit, state):
        self.working_years = working_years
        self.gross_salary = gross_salary
        self.yearly_trad_401k_contribution = yearly_trad_401k_contribution
        self.yearly_roth_401k_contribution = yearly_roth_401k_contribution
        self.yearly_trad_ira_contribution = yearly_trad_ira_contribution
        self.yearly_roth_ira_contribution = yearly_roth_ira_contribution
        self.expected_market_growth_rate = expected_market_growth_rate
        self.working_federal_tax_bracket = working_federal_tax_bracket
        self.working_state_tax_bracket = working_state_tax_bracket
        self.retirement_federal_tax_bracket = retirement_federal_tax_bracket
        self.retirement_state_tax_bracket = retirement_state_tax_bracket
        self.withdrawal_rate = withdrawal_rate
        self.yearly_brokerage_contribution = yearly_brokerage_contribution
        self.social_security_monthly_benefit = social_security_monthly_benefit
        self.state = state

    def get_working_yearly_usable_income(self, print_type):
        if self.gross_salary == 0:
            return 0

        federal_taxes_paid = self.working_federal_tax_bracket.get_taxes_paid(self.gross_salary - self.yearly_trad_401k_contribution - self.yearly_trad_ira_contribution)

        state_taxes_paid = self.working_state_tax_bracket.get_taxes_paid(self.gross_salary - self.yearly_trad_401k_contribution - self.yearly_trad_ira_contribution)

        social_security_tax = self.gross_salary * .062

        medicare_tax = self.gross_salary * .0145

        net_salary = self.gross_salary - state_taxes_paid - federal_taxes_paid - social_security_tax - medicare_tax - self.yearly_trad_401k_contribution - self.yearly_trad_ira_contribution

        usable_pay = net_salary - self.yearly_roth_401k_contribution - self.yearly_roth_ira_contribution

        if print_type == RetirementPrintType.PRINT_ALL:
            print(" ")
            print("Yearly Gross Pay is: ", '${:,.2f}'.format(self.gross_salary))
            print("Yearly Net Pay is: ", '${:,.2f}'.format(net_salary))
            print("Yearly Usable Pay is: ", '${:,.2f}'.format(usable_pay))
            print(" ")
            print("Yearly Trad 401k Contribution is: ", '${:,.2f}'.format(self.yearly_trad_401k_contribution))
            print("Yearly Trad IRA Contribution is: ", '${:,.2f}'.format(self.yearly_trad_ira_contribution))
            print("Yearly Roth 401k Contribution is: ", '${:,.2f}'.format(self.yearly_roth_401k_contribution))
            print("Yearly Roth IRA Contribution is: ", '${:,.2f}'.format(self.yearly_roth_ira_contribution))
            print("Effective Tax Rate: ", '{:.2f}%'.format(((federal_taxes_paid + state_taxes_paid + social_security_tax + medicare_tax) / self.gross_salary) * 100))
            print(" ")
            print("Yearly Federal Taxes Paid is: ", '${:,.2f}'.format(federal_taxes_paid))
            print("Yearly Social Security Taxes Paid is: ", '${:,.2f}'.format(social_security_tax))
            print("Yearly Medicare Taxes Paid is: ", '${:,.2f}'.format(medicare_tax))
            print("Yearly State Taxes Paid is: ", '${:,.2f}'.format(state_taxes_paid))
        elif print_type == RetirementPrintType.PRINT_TAKE_HOME:
            print("Yearly Gross Pay is: ", '${:,.2f}'.format(self.gross_salary))
            print("Yearly Net Pay is: ", '${:,.2f}'.format(net_salary))
            print("Yearly Usable Pay is: ", '${:,.2f}'.format(usable_pay))

        return usable_pay

    def print_my_life(self, print_type):

        working_usable_pay = self.get_working_yearly_usable_income(RetirementPrintType.PRINT_NONE)

        trad_401k_balance = interest.get_yearly_compound_interest(self.expected_market_growth_rate, 0,
                                                                  self.yearly_trad_401k_contribution / 12,
                                                                  self.working_years
                                                                  )

        trad_ira_balance = interest.get_yearly_compound_interest(self.expected_market_growth_rate, 0,
                                                                 self.yearly_trad_ira_contribution / 12,
                                                                 self.working_years
                                                                 )

        roth_401k_balance = interest.get_yearly_compound_interest(self.expected_market_growth_rate, 0,
                                                                  self.yearly_roth_401k_contribution / 12,
                                                                  self.working_years
                                                                  )

        roth_ira_balance = interest.get_yearly_compound_interest(self.expected_market_growth_rate, 0,
                                                                 self.yearly_roth_ira_contribution / 12,
                                                                 self.working_years
                                                                 )

        trad_401k_yearly_withdrawal = trad_401k_balance * (self.withdrawal_rate / 100)
        trad_ira_yearly_withdrawal = trad_ira_balance * (self.withdrawal_rate / 100)

        roth_401k_yearly_withdrawal = roth_401k_balance * (self.withdrawal_rate / 100)
        roth_ira_yearly_withdrawal = roth_ira_balance * (self.withdrawal_rate / 100)

        provisional_income = ss.get_provisional_income(self.social_security_monthly_benefit,
                                                       trad_401k_yearly_withdrawal, trad_ira_yearly_withdrawal)

        ss_taxable_income = ss.get_social_security_taxable_income(self.social_security_monthly_benefit,
                                                                  provisional_income)

        # Calculate Usable Pay from Traditional Retirement Accounts (401k + IRA)
        ret_federal_taxes_paid = self.retirement_federal_tax_bracket.get_taxes_paid(
            trad_401k_yearly_withdrawal + trad_ira_yearly_withdrawal + ss_taxable_income)

        if self.state == State.GEORGIA:
            ret_state_taxes_paid = self.retirement_state_tax_bracket.get_taxes_paid(
                trad_401k_yearly_withdrawal + trad_ira_yearly_withdrawal)
        else:
            ret_state_taxes_paid = self.retirement_state_tax_bracket.get_taxes_paid(
                trad_401k_yearly_withdrawal + trad_ira_yearly_withdrawal + ss_taxable_income)

        after_tax_pay = trad_401k_yearly_withdrawal + trad_ira_yearly_withdrawal + (self.social_security_monthly_benefit * 12) - ret_federal_taxes_paid - ret_state_taxes_paid

        # Calculate Income that is Usable in Retirement
        retirement_usable_pay = after_tax_pay + roth_401k_yearly_withdrawal + roth_ira_yearly_withdrawal

        if print_type == RetirementPrintType.PRINT_ALL:
            print("SS Income = ", '${:,.2f}'.format(self.social_security_monthly_benefit * 12 + 0))
            print("SS Taxable Income = ", '${:,.2f}'.format(ss_taxable_income + 0))
            print(" ")
            print("Trad 401k Balance = ", '${:,.2f}'.format(trad_401k_balance + 0))
            print("Trad IRA Balance = ", '${:,.2f}'.format(trad_ira_balance + 0))
            print("Roth 401k Balance = ", '${:,.2f}'.format(roth_401k_balance + 0))
            print("Roth IRA Balance = ", '${:,.2f}'.format(roth_ira_balance + 0))
            print(" ")
            print("Trad 401k Yearly Withdrawal = ", '${:,.2f}'.format(trad_401k_yearly_withdrawal + 0))
            print("Trad IRA Yearly Withdrawal = ", '${:,.2f}'.format(trad_ira_yearly_withdrawal + 0))
            print(" ")
            print("After Tax Pay of Taxable Income (Trad IRA + Trad 401k + SS) = ", '${:,.2f}'.format(after_tax_pay + 0))
            print("Roth 401k Take Home Pay = ", '${:,.2f}'.format(roth_401k_yearly_withdrawal + 0))
            print("Roth IRA Take Home Pay = ", '${:,.2f}'.format(roth_ira_yearly_withdrawal + 0))
            print(" ")
            print("Working Usable Pay = ", '${:,.2f}'.format(working_usable_pay + 0))
            print("Retirement Usable Pay = ", '${:,.2f}'.format(retirement_usable_pay + 0))
        elif print_type == RetirementPrintType.PRINT_TAKE_HOME:
            print("Working Usable Pay = ", '${:,.2f}'.format(working_usable_pay + 0))
            print("Retirement Usable Pay = ", '${:,.2f}'.format(retirement_usable_pay + 0))
        else:
            print("Error")
