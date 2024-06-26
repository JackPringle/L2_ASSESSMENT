import math


# Functions...

# Gets calculated answer and rounds depending on float / integer
def rounder(ans):
    # For integer answers, remove any trailing 0's from decimals
    if isinstance(ans, int) or ans.is_integer():
        ans = int(ans)

    # For float answers, round to 3dp
    else:

        # Add decimals places to the answer so that we can't be 'out of index range'
        ans = f"{ans:.4f}"

        # This 'if' needed, otherwise python won't round up for a 5 in some specific cases like (1.0005)
        # Split the number from the decimal point, then check if the thousandths place is '5'
        if str(ans).split('.')[1][3] == "5":

            # If it's 5, treat it like a 6 so that python will round it properly (up)!
            if float(ans) > 0:
                ans = round((float(ans) + 0.0001), 3)

            # For negative cases, subtract the amount (due to the nature of negative subtraction)
            else:
                ans = round((float(ans) - 0.0001), 3)

        else:

            # Round normally for all other cases
            ans = round(float(ans), 3)

        # Set it to a string, so any trailing 0's / decimal points can be removed
        ans = str(ans).rstrip('0').rstrip('.')

    # If the rounded answer is -0, remove the negative sign
    if ans == -0 or ans == "-0":
        ans = int(ans)

    # Return the rounded answer
    return ans


# Returns formula, working, and answer for a wanted calculation using the coordinates
def calculator(x1, y1, x2, y2, to_solve):
    # Set variables so they can always be returned
    form = None
    ans = None
    work = None

    # CALCULATE DISTANCE
    if "distance" in to_solve:

        # Formula string
        form = f"FORMULA = √(𝑥₁ - 𝑥₂)² + (𝑦₁ - 𝑦₂)²"

        # Answer float
        ans = rounder(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)))

        # Working string
        work = f'''WORKING:
        
D = √({x1} - {x2})² + ({y1} - {y2})²     
  = √({rounder(x1 - x2)})² + ({rounder(y1 - y2)})²
  = √{rounder(math.pow((x1 - x2), 2))} + {rounder(math.pow((y1 - y2), 2))}
  = √{rounder(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))}
  = {math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))}'''

    # CALCULATE MIDPOINT
    elif "midpoint" in to_solve:

        # Formula string
        form = f"FORMULA = ((𝑥₁ + 𝑥₂)/2) , ((𝑦₁ + 𝑦₂)/2)"

        # Answer string
        ans = f"({rounder((x1 + x2) / 2)}, {rounder((y1 + y2) / 2)})"

        # Working string
        work = f'''WORKING:

M = (({x1} + {x2})/2), (({y1} + {y2})/2)
  = ({rounder(x1 + x2)}/2), ({rounder(y1 + y2)}/2)
  = ({rounder((x1 + x2) / 2)}, {rounder((y1 + y2) / 2)})'''

    # CALCULATE GRADIENT
    elif "gradient" in to_solve:

        # Formula string
        form = f"FORMULA = (𝑦₂ - 𝑦₁) / (𝑥₂ - 𝑥₁)"

        try:

            # Answer
            ans = rounder((y2 - y1) / (x2 - x1))

            # Working string
            work = f'''WORKING:

            G = ({y2} - {y1}) / ({x2} - {x1})
              = {rounder(y2 - y1)} / {rounder(x2 - x1)}
              = {(y2 - y1) / (x2 - x1)}'''

        # If x1 and x2 are equal, we get a maths error
        except ZeroDivisionError:

            # Answer string
            ans = "Undefined"

            # Working string
            work = '''In this case, the denominator equals to 0.
It is not possible to divide a number by 0,
Therefore....'''

    # CALCULATE EQUATION
    elif "equation" in to_solve:

        # Formula string
        form = f"FORMULA: 𝑦 = 𝑚𝑥 + 𝑐"

        # Find the substitution coordinate
        if x1 == 0 and y1 == 0:
            non_zero_point = x2, y2

        else:
            non_zero_point = x1, y1

        try:

            # Calculate the gradient
            gradient = rounder((y2 - y1) / (x2 - x1))

            # Working string
            work = f'''WORKING:

First, find gradient (𝑚).
𝑚 = ({y2} - {y1}) / ({x2} - {x1})
  = {rounder(y2 - y1)} / {rounder(x2 - x1)}
  = {(y2 - y1) / (x2 - x1)}

Substitute 𝑚 into the equation.
𝑦 = {gradient}𝑥 + 𝑐 

Substitute any non-zero point on the line to find the 𝑦-intercept (𝑐)
The point ({non_zero_point[0]}, {non_zero_point[1]}):
{non_zero_point[1]} = {gradient}({non_zero_point[0]}) + 𝑐
{non_zero_point[1]} = {gradient * non_zero_point[0]} + 𝑐
{non_zero_point[1] - (gradient * non_zero_point[0])} = 𝑐

Finally, combine all variables to form the equation...'''

            # If c is 0, don't include it in the answer
            if non_zero_point[1] - (gradient * non_zero_point[0]) == 0:
                ans = f"𝑦 = {gradient}𝑥"

            # If c is negative, output the equation with a negative sign (and remove the numbers original negative sign)
            elif non_zero_point[1] - (gradient * non_zero_point[0]) < 0:
                ans = f"𝑦 = {gradient}𝑥 - {rounder(non_zero_point[1] - (gradient * non_zero_point[0])) * -1}"

            # If c has a positive value, add it to the equation with a plus sign
            else:
                ans = f"𝑦 = {gradient}𝑥 + {rounder(non_zero_point[1] - (gradient * non_zero_point[0]))}"

        # If x1 and x2 are equal, we get a maths error
        except ZeroDivisionError:

            # Answer string
            ans = "Undefined"

            # Working string
            work = '''In this case, the denominator equals to 0.
It is not possible to divide a number by 0,
Therefore the gradient is undefined.'''

    return form, ans, work


# Checks the ordinate entered by the user is a float or integer
def ordinate_checker(the_ordinate):
    while True:

        try:

            # Ask for the ordinate as a float
            ordinate = float(input(f"{the_ordinate}: "))

            # Check if coordinates are integers, return them individually
            if ordinate.is_integer():
                return int(ordinate)

            else:

                # If ordinate is not an integer, return it as a float
                return float(ordinate)

        # Ordinate is invalid if it's not a float
        except ValueError:
            print("The ordinate must be a float.\n")


# Main Routine...

# Loop for testing purposes
while True:

    # Get ordinate values, call ordinate checker
    x1_var = ordinate_checker("X1")
    y1_var = ordinate_checker("Y1")
    x2_var = ordinate_checker("X2")
    y2_var = ordinate_checker("Y2")

    # Output coordinates for testing
    print("Coordinates:")
    print(f'''({x1_var}, {y1_var})
({x2_var}, {y2_var})
''')

    # Ask user what mode, not checking for any boundary cases in this component...
    mode = input("What mode? (all or one): ")

    # Create the to solve list
    to_solve_list = []

    # Set the list of what can be calculated
    dmge_list = ["distance", "midpoint", "gradient", "equation"]

    # Calculating during 'one by one' mode
    while mode == "one":

        # Ask for the next calculation, not checking for any boundary cases in this component...
        next_calculation = input("What would you like to calculate? ")

        # Add the response to the to solve list
        if next_calculation in dmge_list:
            to_solve_list.append(next_calculation)

        else:
            print("Not a valid option")

        # Call the calculator function, and use the to solve list
        answer_and_working = calculator(float(x1_var), float(y1_var), float(x2_var), float(y2_var), to_solve_list[0])

        # Separate the formula, answer and working
        formula = answer_and_working[0]
        answer = answer_and_working[1]
        working = answer_and_working[2]

        # Print the answer and working separately
        for item in to_solve_list:

            # Formatting
            print()
            print("-" * 45)
            print(f"{item.upper()}")
            print(f"For line ({x1_var}, {y1_var}) to ({x2_var}, {y2_var}):")
            print("-" * 45)
            print(formula)
            print(working)
            print("-" * 20)

            # For equation calculations, output the answer differently
            if item == "equation":
                print(f"  {answer}")

            # Otherwise don't
            else:
                print(f"{item.upper()} = {answer}")

            print("-" * 20)
            print()

        # Reset the list so it doesn't reprint every equation
        to_solve_list = []

    # Calculating during all mode
    if mode == "all":

        # For all each item in the list
        for item in dmge_list:

            # Call calculator function, use the next item in the dmge list
            answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, item)

            # Separate the formula, answer and working
            formula = answer_and_working[0]
            answer = answer_and_working[1]
            working = answer_and_working[2]

            # Break up the calculations by getting user to press <enter> to continue
            input("Press <enter> to continue: ")
            print()

            # Formatting
            print()
            print("-" * 45)
            print(f"{item.upper()}")
            print(f"For line ({x1_var}, {y1_var}) to ({x2_var}, {y2_var}):")
            print("-" * 45)
            print(formula)
            print(working)
            print("-" * 20)

            # For equation calculations, output the answer differently
            if item == "equation" and answer != "Undefined":
                print(f"  {answer}")

            # Otherwise don't
            else:
                print(f"{item.upper()} = {answer}")

            print("-" * 20)
            print()
