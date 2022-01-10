from cs50 import get_float


def main():
    # Get the number of cents owed
    cents = get_cent()

    # Calculate the number of quarters
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies 
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Count the total number of coins
    coins = quarters + dimes + nickels + pennies
    print(int(coins))


def get_cent():
    # Loop while prompting the user for the change 
    while True:
        cents = get_float("Change Owed: ")
        # Break the loop when the cents is non-negative
        if (cents > 0):
            break
    # multiple by 100 to account for more changes
    return cents * 100


def calculate_quarters(cents):
    # Calculate the number of quarters
    return cents // 25


def calculate_dimes(cents): 
    # Calculate the number of dimes
    return cents // 10


def calculate_nickels(cents):
    # Calculate the number of nickels
    return cents // 5


def calculate_pennies(cents):
    # Calculate the number of pennies
    return cents


main()
