# collect input needed for app, input: principal, apr(annual interest rate), years
def main():
    print("This is a monthly payment calculator\n\nPlease enter the required fields to calculate your monthly interest payment.")

    principal = float(input("Enter principal amount: "))
    apr = float(input("Enter annual interest rate: "))
    years = int(input("Enter years: "))

# calculate monthly payment
monthly_interest_rate = apr / 1200
amount_of_months = years * 12
monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

# show user the result