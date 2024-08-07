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


# Main Routine...

# Lists of valid responses
yes_no_list = ["yes", "no"]
dmgea_list = ["distance", "midpoint", "gradient", "equation", ""]
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

    if another_calculation == "yes":

        if number_of_calculations == 0:

            initial_calculation_wanted = string_checker(
                "What would you like to calculate? (d / m / g / e) or press <enter> for "
                "ALL: ", dmgea_list,
                "Please enter "
                "either distance /"
                " midpoint / "
                "gradient / "
                "equation / or <enter> for ALL.")

            if initial_calculation_wanted == "":
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
                print(f"** {item} calculation here **\n")

            another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list,
                                                 "Please "
                                                 "enter "
                                                 "either "
                                                 "yes / no")
            if another_calculation == "no":
                break

            to_solve_list = []

            # Ask what they want to calculate next
            next_calculation = string_checker("What would you like to calculate? (d / m / g / e): ", dmge_list,
                                              "Please enter "
                                              "either distance /"
                                              " midpoint / "
                                              "gradient / "
                                              "equation.")
            to_solve_list.append(next_calculation)

    if to_solve == "all":

        to_solve_list = ["Distance", "Midpoint", "Gradient", "Line equation"]

        print("**** ALL MODE ****\n")

        # Loop headings in order for each calculation to solve
        for item in to_solve_list:
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
