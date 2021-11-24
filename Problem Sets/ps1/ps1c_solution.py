# user input
annual_salary = float(input("Enter your annual salary: "))
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
steps = 0
current_savings = 0
low = 0
high = 10000
guess_rate = (high + low) // 2
# Use a while loop since we check UNTIL something happens.
while abs(current_savings - total_cost * portion_down_payment) >= 100:
    # Reset current_savings at the beginning of the loop
    current_savings = 0
    # Create a new variable for use within the for loop.
    for_annual_salary = annual_salary
    # convert guess_rate into a float
    rate = guess_rate / 10000
    # Since we have a finite number of months, use a for loop to calculate
    # amount saved in that time.`enter code here`
    for month in range(36):
        # With indexing starting a zero, we need to calculate at the beginning
        # of the loop.
        if month % 6 == 0 and month > 0:
            for_annual_salary += for_annual_salary * semi_annual_raise
        # Set monthly_salary inside loop where annual_salary is modified
        monthly_salary = for_annual_salary / 12
        # Calculate current savings
        current_savings += monthly_salary * rate + current_savings * r / 12
    # The statement that makes this a bisection search
    if current_savings < total_cost * portion_down_payment:
        low = guess_rate
    else:
        high = guess_rate
    guess_rate = (high + low) // 2
    steps += 1
    # The max amount of guesses needed is log base 2 of 10000 which is slightly
    # above 13. Once it gets to the 14th guess it breaks out of the while loop.
    if steps > 13:
        break

# output
if steps > 13:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", rate)
    print("Steps in bisection search:", steps)
