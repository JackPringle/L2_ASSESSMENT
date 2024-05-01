# Functions...

# Ordinate Checker Function
# Checks the ordinate entered by the user is a float
def ordinate_checker(the_ordinate):
    while True:

        try:

            # Ask for the ordinate as a float
            ordinate = float(input(f"{the_ordinate}: "))

            # Check if coordinates are integers, return them individually
            if ordinate.is_integer():
                return int(ordinate)

            else:

                # If ordinate is not an integer, return it as a string
                return ordinate

        # Ordinate is invalid if it's not a float
        except ValueError:
            print("The ordinate must be a float.\n")


# Main Routine...

# Get ordinate values, call ordinate checker
print("Enter the coordinates of an end point... (x,y)")
x1 = ordinate_checker("X")
y1 = ordinate_checker("Y")
print()
print("Enter the other end... (x,y)")
x2 = ordinate_checker("X")
y2 = ordinate_checker("Y")

# If ordinates are equal to eachother, keep asking for ordinates
while x1 == x2 == y1 == y2:
    print("Error: Coordinates can not be equal!\n")

    print("Enter the coordinates of an end point... (x,y)")
    x1 = ordinate_checker("X")
    y1 = ordinate_checker("Y")
    print()
    print("Enter the other end... (x,y)")
    x2 = ordinate_checker("X")
    y2 = ordinate_checker("Y")

# Print out the coordinates
print()
print(f"The coordinates are ({x1}, {y1}) and ({x2}, {y2})")
