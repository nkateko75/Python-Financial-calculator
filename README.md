# Python-Financial-calculator
#This program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
# Importing Math
import math

# Investment calculator
def investment_calculator():
    P = float(input("Please enter the amount of money that you want to deposit / invest: "))  # ‘P’ is the amount that the user deposits.
    rate = float(input("Please enter the interest rate (as percentage. NB! only enter the number): "))  # ‘rate’ is the interest entered divided by 100, e.g. if 8% is entered, then r is 0.08.
    t = int(input("Please enter the number of years you plan on investing for: "))  # ‘t’ is the number of years that the money is being invested for.
    interest = str(input('Do you want either “simple” or “compound" interest? ')).lower()

    r = rate / 100 #interest converted to percentages
    if interest == "simple":  # calculates simple interest
        A = P * (1 + r * t)
    elif interest == "compound":  # calculates compound interest
        A = P * math.pow((1 + r), t)
    else:
        print("The option selected is invalid, please enter either 'compound' or 'simple'")
        return  # Exit the function if an invalid option is entered

    print(f"The total amount that you will receive after {t} years is: {A}")  # The variables in {} will be formatted and read as strings

# Bond calculator
def bond_calculator():
    P = float(input("Please enter the current value of the house: "))
    i = float(input("Please enter the interest rate: "))
    n = int(input("Please enter the number of months over which you will repay the bond: "))
   
    i = (i / 100) / 12  # Yearly interest rate divided into months

    repayment = (i * P) / (1 - math.pow((1 + i), -n))  # calculates the monthly repayment
    print(f"The total amount that you will pay monthly will be: {repayment}")  # The variables in {} will be formatted and read as strings

# This is the Main Function
def main_func():
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")  # Prompt user to choose between the two options
    print("investment - to calculate the amount of money you will earn on interest.")  # Explains what is investment
    print("bond - to calculate the amount of money you will have to repay on a home loan.")  # Explains what is a bond

    choice = input().lower()  # Changes cases to lowercase

    if choice == 'investment':  # Checks if choice is investment
        investment_calculator()  # calls the investment_calculator function
    elif choice == 'bond':  # Check if choice is bond
        bond_calculator()  # calls the bond_calculator function
    else:
        print("The option selected is invalid, enter either 'investment' or 'bond'")  # Return this message if choice entered is invalid

# Start the program
main_func()
