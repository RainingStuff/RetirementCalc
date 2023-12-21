import tax_bracket as tb


class StateIncomeTax:
    def __init__(self, year, standard_deduction):
        self.year = year
        self.standard_deduction = standard_deduction
        self.tax_brackets = []

    def print_tax_info(self, gross_salary):
        print('State Taxes Paid for ' + str(self.year) + ', on a Gross Salary of ' + '${:,.2f}'.format(
            gross_salary) + ' : ' + '${:,.2f}'.format(
            self.get_taxes_paid(gross_salary)) + ', Effective Rate = ' + '{:.2f}%'.format(
            self.get_effective_tax_rate(gross_salary)) + ', Marginal Rate = ' + '{:.2f}%'.format(
            self.get_marginal_tax_rate(gross_salary)))

    def get_taxes_paid(self, gross_salary):

        taxes_paid = 0

        salary = gross_salary - self.standard_deduction

        if salary <= 0:
            return taxes_paid

        for bracket in self.tax_brackets:
            if bracket.end_income is not None and salary > bracket.end_income:
                taxes_paid = taxes_paid + ((bracket.end_income - bracket.start_income) * (bracket.percent / 100))
            elif bracket.end_income is None or salary <= bracket.end_income:
                taxes_paid = taxes_paid + ((salary - bracket.start_income) * (bracket.percent / 100))
                break
            else:
                print("We should never be here!!!!!!!!")
                break

        return taxes_paid

    def get_effective_tax_rate(self, gross_salary):

        return (self.get_taxes_paid(gross_salary) / gross_salary) * 100

    def get_marginal_tax_rate(self, gross_salary):

        salary = gross_salary - self.standard_deduction

        if salary <= 0:
            return 0

        for bracket in self.tax_brackets:
            if bracket.end_income is None or salary <= bracket.end_income:
                return bracket.percent

        return 0


state_2023 = StateIncomeTax(2023, 5400)
state_2023.tax_brackets.append(tb.TaxBracket(1, 0, 750))
state_2023.tax_brackets.append(tb.TaxBracket(2, 750, 2250))
state_2023.tax_brackets.append(tb.TaxBracket(3, 2250, 3750))
state_2023.tax_brackets.append(tb.TaxBracket(4, 3750, 5250))
state_2023.tax_brackets.append(tb.TaxBracket(5, 5250, 7000))
state_2023.tax_brackets.append(tb.TaxBracket(5.75, 7000, None))

state_2023_up_5 = StateIncomeTax(2023, 5400)
state_2023_up_5.tax_brackets.append(tb.TaxBracket(6, 0, 750))
state_2023_up_5.tax_brackets.append(tb.TaxBracket(7, 750, 2250))
state_2023_up_5.tax_brackets.append(tb.TaxBracket(8, 2250, 3750))
state_2023_up_5.tax_brackets.append(tb.TaxBracket(9, 3750, 5250))
state_2023_up_5.tax_brackets.append(tb.TaxBracket(10, 5250, 7000))
state_2023_up_5.tax_brackets.append(tb.TaxBracket(10.75, 7000, None))

state_2024 = StateIncomeTax(2024, 5400)
state_2024.tax_brackets.append(tb.TaxBracket(5.49, 0, None))
