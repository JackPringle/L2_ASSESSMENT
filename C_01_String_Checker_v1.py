# Functions...
# String checker function
def string_checker(question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(question).lower()

        # Check the string is in the valid list
        for item in valid_list:

            # Check if the response matches the entire item or just the first character
            # of the item (if it's not empty)
            if response == item or (len(item) > 0 and response == item[0]):
                return item

        # If not in valid list, print error
        print(error)
        print()


# Main Routine...

# Lists of valid responses
yes_no_list = ["yes", "no"]
dmge_list = ["distance", "midpoint", "gradient", "equation"]

# Get users y / n response and call string checker function
yes_no = string_checker("(y / n): ", yes_no_list, "Please enter yes / no.")

# If user enter yes
if yes_no == "yes" or yes_no == "y":
    print("You said yes")
    print()

# If user enters no
elif yes_no == "no" or yes_no == "n":
    print("You said no")
    print()

# Get user response and call string checker function
next_calculation = string_checker("What would you like to calculate? (d / m / g / e): ", dmge_list,
                                  "Please enter "
                                  "either distance /"
                                  " midpoint / "
                                  "gradient / "
                                  "equation.")

# If user wants distance
if next_calculation == "distance" or next_calculation == "d":
    to_solve = "distance"
    print("Calculate distance")

# If user wants midpoint
elif next_calculation == "midpoint" or next_calculation == "m":
    to_solve = "midpoint"
    print("Calculate midpoint")

# If user wants gradient
elif next_calculation == "gradient" or next_calculation == "g":
    to_solve = "gradient"
    print("Calculate gradient")

# If user wants equation
elif next_calculation == "equation" or next_calculation == "e":
    to_solve = "equation"
    print("Calculate equation")
