def income_tax(inc):
    if inc <= 10000:
        tax = 0
    elif inc <= 30000:
        tax = (inc - 10000) * 0.10
    elif inc <= 60000:
        tax = (20000 * 0.10) + (inc - 30000) * 0.20
    else:
        tax = (20000 * 0.10) + (30000 * 0.20) + (inc - 60000) * 0.30
    return tax 

try:
    annual_income = float(input("Enter your annual income in Rupees: "))
    if annual_income < 0:
        print("Income cannot be negative.")
    else:
        tax_due = income_tax(annual_income)
        print("Your calculated tax is: Rs",tax_due)
except ValueError:
    print("Invalid input. Please enter a numeric value.")