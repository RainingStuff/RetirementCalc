import tax_bracket as tb


class SocialSecurityTax:
    def __init__(self, year):
        self.year = year
        self.tax_brackets = []

    def get_taxable_income(self, provisional_income):

        taxable_income = 0

        if provisional_income <= 0:
            return taxable_income

        for bracket in self.tax_brackets:
            if bracket.end_income is not None and provisional_income > bracket.end_income:
                taxable_income = taxable_income + ((bracket.end_income - bracket.start_income) * (bracket.percent / 100))
            elif bracket.end_income is None or provisional_income <= bracket.end_income:
                taxable_income = taxable_income + ((provisional_income - bracket.start_income) * (bracket.percent / 100))
                break
            else:
                print("We should never be here!!!!!!!!")
                break

        return taxable_income


ss_2023 = SocialSecurityTax(2023)
ss_2023.tax_brackets.append(tb.TaxBracket(0, 0, 25000))
ss_2023.tax_brackets.append(tb.TaxBracket(50, 25000, 34000))
ss_2023.tax_brackets.append(tb.TaxBracket(85, 34000, None))


def get_provisional_income(social_security_monthly_benefit, trad_401k_yearly_withdrawal, trad_ira_yearly_withdrawal):
    social_security_yearly_benefit = social_security_monthly_benefit * 12
    provisional_income = (social_security_yearly_benefit / 2) + trad_401k_yearly_withdrawal + trad_ira_yearly_withdrawal
    return provisional_income


def get_social_security_taxable_income(social_security_monthly_benefit, provisional_income):
    social_security_yearly_benefit = social_security_monthly_benefit * 12

    if provisional_income <= 25000:
        return 0
    elif provisional_income <= 34000:
        return (provisional_income - 25000) * .5
    else:
        taxable_income = (provisional_income - 34000) * .85 + 4500
        if taxable_income > social_security_yearly_benefit * .85:
            return social_security_yearly_benefit * .85
        else:
            return (provisional_income - 34000) * .85 + 4500


