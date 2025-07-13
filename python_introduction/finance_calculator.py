#getting an input from the user

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculating user monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculating the annual savings
annual_interest = 0.05
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#printing the output
print("Your monthly savings are:", monthly_savings)
print("projected savings after one year, with interest, is:", Projected_Savings)