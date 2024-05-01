# Functions...

# Ordinate Checker Function
# Checks the (co)ordinates entered by user are unequal, and is a float
def ordinate_checker():
    while True:

        try:

            # In order, ask user for each ordinate
            x1_ordinate = float(input("X1: "))
            y1_ordinate = float(input("Y1: "))
            x2_ordinate = float(input("X1: "))
            y2_ordinate = float(input("Y2: "))

            # If coordinates are equal, print error
            if x1_ordinate == x2_ordinate and y1_ordinate == y2_ordinate:
                print("Coordinates must be different!\n")

            else:

                # Check if coordinates are integers, return them individually
                if x1_ordinate.is_integer():
                    return int(x1_ordinate)

                elif y1_ordinate.is_integer():
                    return int(y1_ordinate)

                elif x2_ordinate.is_integer():
                    int(x2_ordinate)

                elif y2_ordinate.is_integer():
                    int(y2_ordinate)

                else:

                    # Otherwise return the float ordinates
                    return x1_ordinate, y1_ordinate, x2_ordinate, y2_ordinate

        # Ordinate is invalid if it's not a float
        except ValueError:
            print("The ordinate must be a float.\n")


# Main Routine...

# Get ordinate values, call ordinate checker
x1, y1, x2, y2 = ordinate_checker()
print(f"The coordinates are ({x1}, {y1}) and ({x2}, {y2})")
