def ps1a():
    # retrive user input
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(
        input("Enter the percent of your salary to save, as decimal: ")
    )
    total_cost = int(input("Enter the cost of your dream home:"))

    # initialize some state variables
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    month = 0
    # main body
    while current_savings < total_cost * portion_down_payment:
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * portion_saved
        month += 1

    print("Number of months:", month)

ps1a()