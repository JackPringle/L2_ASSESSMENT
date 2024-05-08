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

# Set problem values
problem_number = 0
another_problem = "yes"

# Set calculations values
number_of_calculations = 0
another_calculation = "yes"

to_solve = "d"

# Keep looping until user does not want another problem
while another_problem == "yes" and to_solve != "all":

    problem_number += 1

    # Create / reset a list of calculations that have already been asked for
    already_calculated = []

    # Keep looping if the user wants another calculation
    while another_calculation == "yes":
        another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list,
                                             "Please "
                                             "enter "
                                             "either "
                                             "yes / no")

        # Ask user what calculation they want, and print working
        if another_calculation == "yes":
            print("** Calculation here **\n")
            number_of_calculations += 1

    # After they say 'no' to another calculation, ask if they want to solve another problem
    another_problem = string_checker("Would you like to solve a different problem / line? (y/n): ", yes_no_list,
                                     "Please enter either "
                                     "yes / no")
    another_calculation = "yes"

if to_solve == "all":

    problem_number += 1

    print("**** ALL MODE ****\n")
    input("Press any key to continue: ")
    print()
    number_of_calculations += 1
    print("** distance calculation here **\n")
    input("Press any key to continue: ")
    print()
    number_of_calculations += 1
    print("** midpoint calculation here **\n")
    input("Press any key to continue: ")
    print()
    number_of_calculations += 1
    print("** gradient calculation here **\n")
    input("Press any key to continue: ")
    print()
    number_of_calculations += 1
    print("** Line equation calculation here **\n")
    print()
    print("END")

# Output the tally of calculations and problems
print()
print(f"Total number of calculations = {number_of_calculations}")
print(f"Total number of problems = {problem_number}")
