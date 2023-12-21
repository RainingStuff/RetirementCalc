Leave yearly_brokerage_contribution as 0, it is not implemented yet.
22500 Trad has the same usable income compared to 15940.75 Roth, that is why this Roth number is used.
I expect the gap between Roth and Trad would shrink a bit if we were to compare the following:
22500 Trad + 6,559.25? Brokerage to 22500 Roth
But again, brokerage is not implemented yet so I can't test this example.

social_security_monthly_benefit was calculated using https://www.ssa.gov/OACT/quickcalc/, use today's dollars checkbox.
If you think SS will be reduced then reduce this number as you please. Note that in GA, SS is not taxed.
If SS was taxed, the Roth example would improve a little. Or rather the Trad example would be worse.
If you want to see what it would be like to retire in a state that does tax SS, uncomment "state = retirement.State.NOT_GEORGIA"
Note that SS is still taxed federally.

There are no checks and balances around contribution limits or income limits for 401k's or IRA's so it is on you to make sure the combo you are testing is possible.

Inflation is accounted for in the expected_market_growth_rate. The number you use here should be the actual market expected returns minus what you think inflation is.
In the code i use 5% because I think the market will be 8% and inflation will be 3%.

If you want to see what the effective federal tax rate is for gross_salary throught history then change print_historical_effective_federal_tax_rate to True.
This will adjust the gross_salary for inflation and print the effective federal tax rate for that year.
The point of this is to show that even though the highest marginal tax bracket in history got pretty high, the salary needed to get taxed at that rate is insanely high.
An example would be 94% in 1945 started at 200,000 but in 1945, 200k would be worth ~3.4 Million in 2023's dollars.

If you think future taxes will be higher then feel free to make a custom state and/or federal tax bracket and assign those to retirement_federal_tax_bracket and retirement_state_tax_bracket

Same thing for withdrawal rate, if you think it should be lower or higher you can play around with that number.
