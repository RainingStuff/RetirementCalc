current_year = 2023
data_start_year = 1913
data = (1, 1.013, 1.009, 1.077, 1.178, 1.173, 1.152, 1.156, 0.891, 0.938, 1.018, 1.004, 1.024, 1.009, 0.981, 0.988,
        1.0, 0.973, 0.911, 0.897, 0.948, 1.035, 1.026, 1.01, 1.037, 0.98, 0.987, 1.007, 1.051, 1.109, 1.06, 1.016,
        1.023, 1.085, 1.144, 1.077, 0.99, 1.011, 1.079, 1.023, 1.008, 1.003, 0.997, 1.015, 1.033, 1.027, 1.0108,
        1.015, 1.011, 1.012, 1.012, 1.013, 1.016, 1.03, 1.028, 1.043, 1.055, 1.058, 1.043, 1.033, 1.062, 1.111,
        1.091, 1.057, 1.065, 1.076, 1.113, 1.135, 1.103, 1.061, 1.032, 1.043, 1.035, 1.019, 1.037, 1.041, 1.048,
        1.054, 1.042, 1.03, 1.03, 1.026, 1.028, 1.029, 1.023, 1.016, 1.022, 1.034, 1.028, 1.016, 1.023, 1.027,
        1.034, 1.032, 1.029, 1.038, 0.996, 1.016, 1.032, 1.021, 1.015, 1.016, 1.001, 1.013, 1.021, 1.024, 1.018,
        1.012, 1.047, 1.08, 1.049)


def get_inflation_adjusted_salary(current_salary, year):
    inflation_adjusted_salary = current_salary

    if year > current_year or year < 1913:
        return 0

    for index in data[current_year - data_start_year:year - data_start_year:-1]:
        inflation_adjusted_salary = inflation_adjusted_salary / index

    return inflation_adjusted_salary


def print_inflation_adjusted_salary(current_salary, year):
    print('${:,.2f} in '.format(current_salary) + str(current_year) + ' is equivalent to ${:,.2f} in '.format(get_inflation_adjusted_salary(current_salary, year)) + str(year))
