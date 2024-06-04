# Functions...

# Checks user response to next_calc question is valid
def int_checker(question, mode):
    while True:

        # Get user response
        response = (input(question))
        error = "This must be an integer!\n"

        try:

            # Set response to an integer
            response = int(response)

            # For dmge questions, check that 1 <= response <= 4
            if mode == "dmge" and (response < 1 or response > 4):
                error = "Please enter either [1], [2], [3], [4]\n"
                print(error)

            # For dmgea questions, check that 1<= response <= 5
            elif mode == "dmgea" and (response < 1 or response > 5):
                error = "Please enter either [1], [2], [3], [4], [5]\n"
                print(error)

            else:
                return response

        # print the error if there is a value error
        except ValueError:
            print(error)


# Main Routine...

# call int checker function to check dmgea question
next_calculation = int_checker("What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], Equation "
                               "[4], or ALL [5]: ", "dmgea")
print(f"You want {next_calculation}")
print()
print("Programme continues")
print()

# call int checker function to check dmge question
next_calculation = int_checker("What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], Equation "
                               "[4]: ", "dmge")
print(f"You want {next_calculation}")
print()
print("program continues")
