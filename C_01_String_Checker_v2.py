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
dmgea_list = ["distance", "midpoint", "gradient", "equation", ""]
dmge_list = ["distance", "midpoint", "gradient", "equation"]

# Loops to make testing faster...
for item in range(0, 6):
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

# Loops to make testing faster...
for item in range(0, 6):
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
        print()

    # If user wants midpoint
    elif next_calculation == "midpoint" or next_calculation == "m":
        to_solve = "midpoint"
        print("Calculate midpoint")
        print()

    # If user wants gradient
    elif next_calculation == "gradient" or next_calculation == "g":
        to_solve = "gradient"
        print("Calculate gradient")
        print()

    # If user wants equation
    elif next_calculation == "equation" or next_calculation == "e":
        to_solve = "equation"
        print("Calculate equation")
        print()

# Loops to make testing faster...
for item in range(0, 6):
    # Find out if the user wants to calculate things one at a time, or all at once
    initial_calculation_wanted = string_checker("What would you like to calculate? (d / m / g / e) or press <enter> for"
                                                "ALL: ", dmgea_list,
                                                "Please enter "
                                                "either distance /"
                                                " midpoint / "
                                                "gradient / "
                                                "equation / or <enter> for ALL.")

    # If user wants distance
    if initial_calculation_wanted == "distance" or initial_calculation_wanted == "d":
        to_solve = "distance"
        print("Calculate distance")
        print()

    # If user wants midpoint
    elif initial_calculation_wanted == "midpoint" or initial_calculation_wanted == "m":
        to_solve = "midpoint"
        print("Calculate midpoint")
        print()

    # If user wants gradient
    elif initial_calculation_wanted == "gradient" or initial_calculation_wanted == "g":
        to_solve = "gradient"
        print("Calculate gradient")
        print()

    # If user wants equation
    elif initial_calculation_wanted == "equation" or initial_calculation_wanted == "e":
        to_solve = "equation"
        print("Calculate equation")
        print()

    elif initial_calculation_wanted == "":
        to_solve = "all"
        print("Calculate all")
        print()
