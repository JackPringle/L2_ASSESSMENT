# Functions...

def int_checker(question, mode):
    while True:
        response = (input(question))
        error = "This must be an integer!\n"

        try:

            response = int(response)

            if mode == "dmge" and (response < 1 or response > 4):
                error = "Please enter either [1], [2], [3], [4]\n"
                print(error)

            elif mode == "dmgea" and (response < 1 or response > 5):
                error = "Please enter either [1], [2], [3], [4], [5]\n"
                print(error)

            else:

                return response

        except ValueError:
            print(error)


# Main Routine...

next_calculation = int_checker("What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], Equation "
                               "[4], or ALL [5]: ", "dmgea")
print(f"You want {next_calculation}")
print()
print("Programme continues")
print()

next_calculation = int_checker("What would you like to calculate? Distance [1], Midpoint [2], Gradient [3], Equation "
                               "[4]: ", "dmge")
print(f"You want {next_calculation}")
print()
print("program continues")
