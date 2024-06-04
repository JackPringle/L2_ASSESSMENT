# Functions...

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
                error = "Please enter a valid option\n"
                print(error)

            else:
                return response

        # print the error if there is a value error
        except ValueError:
            print(error)


# Main Routine...

# call int checker function to check dmgea question
next_calculation = int_checker("What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], "
                               "Equation"
                               "[4], or ALL [5]: ", 5)
print(f"You want {next_calculation}")
print()
print("Programme continues")
print()


# call int checker function to check dmge question
next_calculation = int_checker("What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], "
                               "Equation"
                               "[4]: ", 4)
print(f"You want {next_calculation}")
print()
print("program continues")
