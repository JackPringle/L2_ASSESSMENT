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

# Heading
print("*" * 42)
print("***** COORDINATE GEOMETRY CALCULATOR *****")
print("*" * 42)
print()

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

    # Add to tally of problem numbers
    problem_number += 1

    # Reset the number of calculations for each problem
    number_of_calculations = 0

    # Automatically want to calculate something
    another_calculation = "yes"

    # Create lists
    to_solve_list = []
    already_calculated = []

    # Start of programme

    # For the first calculation only
    if number_of_calculations == 0:

        # For first calculation, ask what they want to calculate (includes all mode option)
        initial_calculation_wanted = int_checker(
            "What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], "
            "Equation [4], or ALL [5]: ", 5)

        # Set to solve to 'all' if chosen
        if initial_calculation_wanted == 5:
            to_solve = "all"

        # If they chose dmge, add what they want to both lists, for solving and remembering what's been calculated
        else:
            already_calculated.append(initial_calculation_wanted)
            to_solve_list.append(initial_calculation_wanted)
            to_solve = "one by one"

    # If they didn't request 'all' calculations for the problem
    if to_solve != "all":

        # Loop for each calculation
        while another_calculation == "yes":

            # Print the heading and calculation for requested calculations
            for item in to_solve_list:
                number_of_calculations += 1

                print()
                print(f"** {dmge_list[int(item) - 1]} calculation here **\n")

            # After printing the last calculation wanted, ask if they'd like another one
            another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list,
                                                 "Please "
                                                 "enter "
                                                 "either "
                                                 "yes / no")

            # If they don't, break out, they will then be asked if they want another line/problem
            if another_calculation == "no":
                break

            # Remove past calculations from the list
            to_solve_list = []

            # Ask what they want to calculate next (does not include all mode this time since it's not the first
            # calculation)
            next_calculation = int_checker(
                "What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], "
                "Equation [4]: ", 4)

            # If they already calculated that, tell them, then go back to top of loop, so they can re-enter
            if next_calculation in already_calculated:
                print()
                print(f"You have already calculated the {dmge_list[int(next_calculation) - 1]} for this problem!\n")

            # If it has not already been calculated, add it to the lists, then go back to top of loop
            else:
                already_calculated.append(next_calculation)
                to_solve_list.append(next_calculation)

    # If they want 'all' calculations for the problem
    if to_solve == "all":

        # Heading
        print("**** ALL MODE ****\n")

        # For all of dmge, break up the calculations by getting user to press <enter> to continue
        for item in dmge_list:
            number_of_calculations += 1

            input("Press <enter> to continue: ")
            print()
            print(f"** {item} calculation here **\n")

    # After they say 'no' to another calculation, ask if they want to solve another problem
    # If they choose yes, program will go back to the top of the main loop
    # If they choose no, program will end the main loop and start printing summaries
    another_problem = string_checker("Would you like to solve a different problem / line? (y/n): ", yes_no_list,
                                     "Please enter either "
                                     "yes / no")

    # Once the user is done calculating, add together the number of calculations completed
    TOTAL_calculations += number_of_calculations

# Output the tally of total calculations and problems
print()
print(f"Total number of calculations = {TOTAL_calculations}")
print(f"Total number of problems = {problem_number}")
