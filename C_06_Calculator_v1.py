import math


# Functions...

# Returns answer and working for a wanted calculation using the ordinates
def calculator(x1, y1, x2, y2, to_solve):
    # Set variables so they can always be returned
    form = None
    ans = None
    work = None

    # Calculate distance
    if "distance" in to_solve:

        # Formula string
        form = f"FORMULA = √(𝑥₁ - 𝑥₂)² + (𝑦₁ - 𝑦₂)²"

        # Answer float
        ans = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

        # Working string
        work = f'''WORKING:
        
D = √({x1} - {x2})² + ({y1} - {y2})²     
  = √({x1 - x2})² + ({y1 - y2})²
  = √{math.pow((x1 - x2), 2)} + {math.pow((y1 - y2), 2)}
  = √{math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)}
  = {math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))}
  '''

    # Calculate midpoint
    elif "midpoint" in to_solve:

        # Formula string
        form = f"FORMULA = ((𝑥₁ + 𝑥₂)/2) , ((𝑦₁ + 𝑦₂)/2)"

        # Answer string
        ans = f"({(x1 + x2)/2}, {(y1 + y2)/2})"

        # Working string
        work = f'''WORKING:

M = (({x1} + {x2})/2), (({y1} + {y2})/2)
  = ({x1 + x2}/2), ({y1 + y2}/2)
  = ({(x1 + x2)/2}), ({(y1 + y2)/2})
  '''

    # Calculate gradient
    elif "gradient" in to_solve:

        # Formula string
        form = f"FORMULA = (𝑦₂ - 𝑦₁) / (𝑥₂ - 𝑥₁)"

        # Answer float
        ans = (y2 - y1) / (x2 - x1)

        # Working string
        work = f'''WORKING:

G = ({y2} - {y1}) / ({x2} - {x1})
  = {y2 - y1} / {x2 - x1}
  = {(y2 - y1) / (x2 - x1)}
  '''

    # Calculate equation of the line
    elif "equation" in to_solve:

        # Formula string
        form = f"FORMULA: 𝑦 = 𝑚𝑥 + 𝑐"

        # Find the substitution coordinate
        if x1 == 0 and y1 == 0:
            non_zero_point = x2, y2

        else:
            non_zero_point = x1, y1

        # Answer string
        gradient = (y2 - y1) / (x2 - x1)
        if non_zero_point[1] - (gradient * non_zero_point[0]) == 0:
            ans = f"𝑦 = {gradient}𝑥"

        else:
            ans = f"𝑦 = {gradient}𝑥 + {non_zero_point[1] - (gradient * non_zero_point[0])}"

        # Working string
        work = f'''WORKING:

First, find gradient (𝑚).
𝑚 = ({y2} - {y1}) / ({x2} - {x1})
  = {y2 - y1} / {x2 - x1}
  = {(y2 - y1) / (x2 - x1)}
   
Substitute 𝑚 into the equation.
𝑦 = {gradient}𝑥 + 𝑐 

Substitute any non-zero point on the line to find the 𝑦-intercept (𝑐)
The point ({non_zero_point[0]}, {non_zero_point[1]}):
{non_zero_point[1]} = {gradient}({non_zero_point[0]}) + 𝑐
{non_zero_point[1]} = {gradient * non_zero_point[0]} + 𝑐
{non_zero_point[1] - (gradient * non_zero_point[0])} = 𝑐

Finally, combine all variables to form the equation...
'''

    return form, ans, work


# Main Routine...

# Hard coded coordinates for testing
x1_var = 0
y1_var = 0
x2_var = 1
y2_var = 10

# Output coordinates for testing
print("Coordinates:")
print(f'''({x1_var}, {y1_var})
({x2_var}, {y2_var})
''')

mode = input("What mode? (all or one): ")

to_solve_list = []

# Calculating during 'one by one' mode
if mode == "one by one":

    # Ask for the next calculation
    next_calculation = input("What would you like to calculate? ")

    # Add the response to the to solve list
    to_solve_list.append(next_calculation)
    print()

    # Call the calculator function, and use the to solve list
    answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, to_solve_list[0])

    # Separate the formula, answer and working
    formula = answer_and_working[0]
    answer = answer_and_working[1]
    working = answer_and_working[2]

    # Print the answer and working separately
    for item in to_solve_list:
        print(f"** {item} calculation here **\n")
        print(formula)
        print(f"Answer = {answer}")
        print(working)
        print()

# Calculating during all mode
if mode == "all":

    # Set the list of what needs to be calculated
    dmge_list = ["distance", "midpoint", "gradient", "equation"]

    # For all of dmge, break up the calculations by getting user to press <enter> to continue
    for item in dmge_list:
        # Call claculator function, use the next item in the dmge list
        answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, item)

        # Separate the formula, answer and working
        formula = answer_and_working[0]
        answer = answer_and_working[1]
        working = answer_and_working[2]

        input("Press <enter> to continue: ")
        print()

        # Print the answer and working separately
        print("-" * 45)
        print(f"{item.upper()}")
        print(f"For line ({x1_var}, {y1_var}) to ({x2_var}, {y2_var}):")
        print("-" * 45)
        print(formula)
        print(working)
        print("-" * 20)
        if item == "equation":
            print(f"  {answer}")
        else:
            print(f"{item.upper()} = {answer}")
        print("-" * 20)
        print()
