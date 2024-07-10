import math

# Investment calculator
def investment_calculator():
    try:
        P = float(input("Please enter the amount of money that you want to deposit / invest: "))
        rate = float(input("Please enter the interest rate (as percentage. NB! only enter the number): "))
        t = int(input("Please enter the number of years you plan on investing for: "))
        interest = input('Do you want either "simple" or "compound" interest? ').lower()

        r = rate / 100
        if interest == "simple":
            A = P * (1 + r * t)
        elif interest == "compound":
            A = P * math.pow((1 + r), t)
        else:
            print("The option selected is invalid, please enter either 'compound' or 'simple'")
            return investment_calculator()  # Recursive call to ensure it stays in the investment calculator until valid input

        print(f"The total amount that you will receive after {t} years is: {A}")

    except ValueError:
        print("Invalid input! Please enter numerical values for the amount, interest rate, and number of years.")
        investment_calculator()  # Recursive call to handle invalid inputs

# Bond calculator
def bond_calculator():
    try:
        P = float(input("Please enter the current value of the house: "))
        i = float(input("Please enter the interest rate: "))
        n = int(input("Please enter the number of months over which you will repay the bond: "))
        i = (i / 100) / 12

        repayment = (i * P) / (1 - math.pow((1 + i), -n))
        print(f"The total amount that you will pay monthly will be: {repayment}")

    except ValueError:
        print("Invalid input! Please enter numerical values for the house value, interest rate, and number of months.")
        bond_calculator()  # Recursive call to handle invalid inputs

# Main function
def main_func():
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of money you will earn on interest.")
    print("bond - to calculate the amount of money you will have to repay on a home loan.")

    choice = input().lower()

    if choice == 'investment':
        investment_calculator()
    elif choice == 'bond':
        bond_calculator()
    else:
        print("The option selected is invalid, enter either 'investment' or 'bond'")
        main_func()  # Recursive call to handle invalid inputs

# Start the program
main_func()
d
