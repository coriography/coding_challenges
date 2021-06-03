
####** TAX BRACKETS **####

# TODO: The tax bracket breaks at $86,375 - incomes >= $86,376 are taxed 24%, and incomes <= $86,375 are taxed 22%.
#?? what is the lowest salary in the 24% tax bracket where the take-home pay is higher than the top of the 22% tax bracket?
#?? return the total salary, the total amount of tax per year on that salary, and the take-home pay.

def find_lowest_in_bracket(lo_tax_rate, max_lo_salary, hi_tax_rate, min_hi_salary):
    """Finds the lowest salary in given tax bracket where the take-home pay is higher than the top of the lower tax bracket"""

    # find max take-home pay of lower bracket
    max_take_home_lower_bracket = max_lo_salary - (lo_tax_rate/100) * max_lo_salary
    
    # iterative solution: loop through int starting at min_hi_salary until take-home pay is higher than max_take_home_lower_bracket
    # "binary search"/logn solution: requires additional input of max_hi_salary

    optimal_min_salary = min_hi_salary
    optimal_min_take_home_pay = 0
    optimal_min_tax = 0

    while optimal_min_take_home_pay < max_take_home_lower_bracket:
        
        optimal_min_tax = (hi_tax_rate/100) * optimal_min_salary
        optimal_min_take_home_pay = optimal_min_salary - optimal_min_tax

        optimal_min_salary += 1
    
    return print(f"total minimum salary with highest take-home pay: {optimal_min_salary}\ntotal tax: {optimal_min_tax}\ntotal take-home pay: {optimal_min_take_home_pay}")

find_lowest_in_bracket(22, 86375, 24, 86376)