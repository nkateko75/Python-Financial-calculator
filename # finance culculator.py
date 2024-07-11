#This a finacial calculator

import math #Imports the math function

# Investment calculator
def investment_calculator():  #defining the investment fumction
    while True:
        try:
            P = float(input("Please enter the amount of money that you want to deposit / invest: ")) #Prompting the user for the amount to be invested.
            break
        except ValueError:
            print("Invalid input! Please enter a numerical value for the amount.")  # Error handling

    while True:
        try:
            rate = float(input("Please enter the interest rate (as percentage. NB! only enter the number): "))  #Prompting the user for the rate.
            break
        except ValueError:
            print("Invalid input! Please enter a numerical value for the interest rate.")  #Error handling

    while True:
        try:
            t = int(input("Please enter the number of years you plan on investing for: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer value for the number of years.")

    while True:
        interest = input('Do you want either "simple" or "compound" interest? ').lower()  #prompt for intrest type
        if interest in ["simple", "compound"]:
            break
        else:
            print("The option selected is invalid, please enter either 'compound' or 'simple'") #  throws and error when invalid option is selected

    r = rate / 100  # Converting the rate to %
    if interest == "simple":
        A = P * (1 + r * t) # Calculating the acumulated amount
    elif interest == "compound":
        A = P * math.pow((1 + r), t) # Calculating the acumulated amount

    print(f"The total amount that you will receive after {t} years is: {A}")

# Bond calculator
def bond_calculator(): #defining the bond function
    while True:
        try:
            P = float(input("Please enter the current value of the house: "))
            break
        except ValueError:  # Error handling
            print("Invalid input! Please enter a numerical value for the house value.")

    while True:
        try:
            i = float(input("Please enter the interest rate: "))
            break
        except ValueError: # Error handling
            print("Invalid input! Please enter a numerical value for the interest rate.") # Error Handling

    while True:
        try:
            n = int(input("Please enter the number of months over which you will repay the bond: ")) #prompt user for the number of months that they gonna repay the bond
            break
        except ValueError:
            print("Invalid input! Please enter an integer value for the number of months.") #Error handling

    i = (i / 100) / 12 #converting the interest
    repayment = (i * P) / (1 - math.pow((1 + i), -n))  # calculating the repayment amount
    print(f"The total amount that you will pay monthly will be: {repayment}")

# Main function
def main_func():
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of money you will earn on interest.")
    print("bond - to calculate the amount of money you will have to repay on a home loan.")

    while True:
        choice = input().lower()
        if choice == 'investment':
            investment_calculator()
            break
        elif choice == 'bond':
            bond_calculator()
            break
        else:
            print("The option selected is invalid, enter either 'investment' or 'bond'")

# Start the program
main_func()  #ccalls the main function to start the program
