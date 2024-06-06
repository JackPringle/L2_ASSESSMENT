# Functions...

# String checker function
def string_checker(question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(question).lower()

        # Check the string is in the valid list
        for var_item in valid_list:

            # Check if the response matches the entire item or just the first character
            # of the item (if it's not empty)
            if response == var_item or (len(var_item) > 0 and response == var_item[0]):
                return var_item

        # If not in valid list, print error
        print(error)
        print()


# Checks user response to next_calc question is valid
def int_checker(question, high):
    while True:

        # Get user response
        response = (input(question))
        error = "This must be an integer!\n"

        try:

            # Set response to an integer
            response = int(response)

            # checks the valid range, if it's not then print an error
            if response < 1 or response > high:
                error = f"Please enter an integer from 1-{high}\n"
                print(error)

            else:
                return response

        # print the error if there is a value error
        except ValueError:
            print(error)


# Main Routine...

# Lists of valid responses
yes_no_list = ["yes", "no"]
dmge_list = ["distance", "midpoint", "gradient", "equation"]

# Set problem values
problem_number = 0
another_problem = "yes"

# Set calculations values
TOTAL_calculations = 0
to_solve = None

# Keep looping until user does not want another problem
while another_problem == "yes":

    problem_number += 1
    number_of_calculations = 0
    another_calculation = "yes"
    to_solve_list = []
    already_calculated = []

    if another_calculation == "yes":

        if number_of_calculations == 0:

            initial_calculation_wanted = int_checker(
                "What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], "
                "Equation [4], or ALL [5]: ", 5)

            already_calculated.append(initial_calculation_wanted)

            if initial_calculation_wanted == 5:
                to_solve = "all"

            else:
                to_solve_list.append(initial_calculation_wanted)
                to_solve = "one by one"

    if to_solve != "all":

        # Ask user what calculation they want, and print working
        while another_calculation == "yes":

            # Loop headings in order for each calculation to solve
            for item in to_solve_list:
                number_of_calculations += 1

                print()
                print(f"** {dmge_list[int(item) - 1]} calculation here **\n")

            another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list,
                                                 "Please "
                                                 "enter "
                                                 "either "
                                                 "yes / no")

            if another_calculation == "no":
                break

            to_solve_list = []

            # Ask what they want to calculate next
            next_calculation = int_checker(
                "What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], "
                "Equation [4]: ", 4)

            if next_calculation in already_calculated:
                print()
                print(f"You have already calculated the {dmge_list[int(next_calculation) - 1]} for this problem!\n")

            else:
                already_calculated.append(next_calculation)
                to_solve_list.append(next_calculation)

    if to_solve == "all":

        print("**** ALL MODE ****\n")

        # Loop headings in order for each calculation to solve
        for item in dmge_list:
            number_of_calculations += 1

            input("Press <enter> to continue: ")
            print()
            print(f"** {item} calculation here **\n")

    # After they say 'no' to another calculation, ask if they want to solve another problem
    another_problem = string_checker("Would you like to solve a different problem / line? (y/n): ", yes_no_list,
                                     "Please enter either "
                                     "yes / no")

    TOTAL_calculations += number_of_calculations

# Output the tally of calculations and problems
print()
print(f"Total number of calculations = {TOTAL_calculations}")
print(f"Total number of problems = {problem_number}")
