annual_income = float(input("Enter your annual income in Rupees: "))
if annual_income < 0:
    print("Income cannot be negative.")
else:
    if annual_income <= 250000:
        tax_due = 0
    elif annual_income <= 500000:
        tax_due = (annual_income - 250000) * 0.05
    elif annual_income <= 1000000:
        tax_due = (250000 * 0.05) + (annual_income - 500000) * 0.20
    else:
        tax_due = (250000 * 0.05) + (500000 * 0.20) + (annual_income - 1000000) * 0.30
    
    print("Your calculated tax is: Rs", tax_due)
