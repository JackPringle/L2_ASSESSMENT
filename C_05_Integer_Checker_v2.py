# Functions...

# Checks user response to next_calc question is valid
def int_checker(question, high):
    while True:

        # Corresponding dmgea options
        dmgea = {1: "distance", 2: "midpoint", 3: "gradient", 4: "equation", 5: "all"}

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

                # Return the string value
                return dmgea[response]

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
