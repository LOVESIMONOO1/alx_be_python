#User financial details
monthly_income = int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your total monthly expenses"))

#Monthly savings calculations
monthly_savings = monthly_income - monthly_expenses
print("your monthly savings are",monthly_savings,)

#Annual savings
projected_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected_savings after one year, with interest, is :",projected_saving,)

