import tax_bracket as tb


class LongTermCapitalGainsTax:
    def __init__(self, year, standard_deduction, niit_tax_cutoff, niit_rate):
        self.year = year
        self.standard_deduction = standard_deduction
        self.niit_tax_cutoff = niit_tax_cutoff
        self.niit_rate = niit_rate / 100
        self.tax_brackets = []

    def print_tax_info(self, gross_salary):
        print('Taxes Paid for ' + str(self.year) + ', on a LTCG Sale of ' + '${:,.2f}'.format(
            gross_salary) + ' : ' + '${:,.2f}'.format(
            self.get_taxes_paid(gross_salary)) + ', Effective Rate = ' + '{:.2f}%'.format(
            self.get_effective_tax_rate(gross_salary)))

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

        if salary > self.niit_tax_cutoff:
            taxes_paid = taxes_paid + (salary - self.niit_tax_cutoff) * self.niit_rate

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


# Standard Deduction of 13850 for 2023
ltcg_2023 = LongTermCapitalGainsTax(2023, 13850, 200000, 3.8)
ltcg_2023.tax_brackets.append(tb.TaxBracket(0, 0, 44625))
ltcg_2023.tax_brackets.append(tb.TaxBracket(15, 44625, 492300))
ltcg_2023.tax_brackets.append(tb.TaxBracket(20, 492300, None))
