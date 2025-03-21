def solve(meal_cost, tip_percent, tax_percent):
    """
    Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
    and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total
    cost. Round the result to the nearest integer.
    solve has the following parameters:

    int meal_cost: the cost of food before tip and tax
    int tip_percent: the tip percentage
    int tax_percent: the tax percentage
    Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.
    >>> solve(100, 15, 8)
    123
    """    
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    total_cost = meal_cost + tip + tax
    rounded_cost = round(total_cost)
    print(rounded_cost)


    