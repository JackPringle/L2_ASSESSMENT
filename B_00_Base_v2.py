import math
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable


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


# Includes the instructions for the calculator
def instructions():

    print('''***** INSTRUCTIONS *****

Start by entering two coordinates

Feel free to enter a name for the problem so you can associate it with a
maths book question, e.g. "Page 8, question (a)".

For a visual understanding of the line, you may generate a line graph.
This graph can be saved to file if needed.

For the first calculation of a line, you can choose to calculate "one by one",
or calculate "all" in one go.

Formulas, step-by-step workings, and answers will be provided for each calculation!
You will get both the unrounded answers, and final answers rounded to 3dp.

Complete as many specific calculations for as many lines / problems you want!

Once ou are done, you will get a summary of all the lines and calculations you made.
A text file of this summary will also be generated to your files for you to save 
for revision :)

Let the calculations begin!!!

''')


# Checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # If the response is blank after stripping whitespace, output error
        if response == "":
            print("This can't be blank, please try again.")

        else:
            return response


# Uses the coordinates to generate a line graph for visualisation
def grapher(title, x1, y1, x2, y2):
    # Group the coordinates
    x_values_list = [x1, x2]
    y_values_list = [y1, y2]

    # Change the graphs filename
    plt.figure(num=f"{title} / Graph")

    # Set axis limits to ensure both x and y axes are visible
    plt.xlim(min(x1, x2) - 1, max(x1, x2) + 1)
    plt.ylim(min(y1, y2) - 1, max(y1, y2) + 1)

    # Set equal scaling for both axes
    plt.axis('equal')

    # Plot the line
    plt.plot(x_values_list, y_values_list, marker='o')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)

    # Show x and y-axis
    plt.grid(True)
    plt.axhline(0, color='red', linewidth=3)
    plt.axvline(0, color='red', linewidth=3)

    # Display the plot
    plt.show()


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

        # Convert it back to a float so no string answers are returned
        ans = float(ans)

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
  = √({rounder(math.pow((x1 - x2), 2))} + {rounder(math.pow((y1 - y2), 2))})
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

            # Calculate c value
            c_value = rounder(non_zero_point[1] - (gradient * non_zero_point[0]))

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
{non_zero_point[1]} = {rounder(gradient * non_zero_point[0])} + 𝑐
{non_zero_point[1] - (gradient * non_zero_point[0])} = 𝑐

Finally, combine all variables to form the equation...'''

            # Building the answer

            # If the gradient is 0, there is no x term, and leave y intercept alone
            x_term = ""
            y_int = c_value

            # When gradient is 1, leave it as x
            if gradient == 1:
                x_term = "𝑥"

            # When gradient is -1, leave it as -x
            elif gradient == -1:
                x_term = "-𝑥"

            # Otherwise just do the full x term
            elif gradient != 0:
                x_term = f"{gradient}𝑥"

            # If y intercept is positive, include plus sign
            if gradient != 0 and c_value > 0:
                y_int = f" + {c_value}"

            # If y intercept is negative, include minus sign (remove '-' from c)
            elif gradient != 0 and c_value < 0:
                y_int = f" - {(c_value * -1)}"

            # Don't include the c = 0, if gradient has a value
            elif gradient != 0 and c_value == 0:
                y_int = ""

            # Put the equation together
            ans = f"𝑦 = {x_term}{y_int}"

        # If x1 and x2 are equal, we get a maths error
        except ZeroDivisionError:

            # Answer string
            ans = f"𝑥 = {x1}"

            # Working string
            work = '''An undefined gradient means the line is vertical.
Therefore the equation is in terms of x, rather than y...'''

    # Return the values
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


# Formats the DataFrame
def table_formatting(dataframe):
    # Make the table using the pretty table library
    table = PrettyTable()

    # Add columns from the DataFrame
    table.field_names = dataframe.columns.tolist()

    # Add columns from the DataFrame
    for _, row_var in dataframe.iterrows():
        table.add_row(row_var.tolist())

    # Align the columns differently
    for col_var in ["Coordinates", "Question Name"]:
        table.align[col_var] = 'c'

    for col_var in ["Distance", "Midpoint", "Gradient", "Equation"]:
        table.align[col_var] = 'l'

    # Set style and border options
    table.header_style = "upper"
    table.horizontal_char = "_"
    table.junction_char = "+"
    table.vertical_char = "|"

    # Print the table
    print(table)


# Main Routine...

# Create a list for the calculation data to be stored in for the end summary
data = []

# Lists of valid responses
yes_no_list = ["yes", "no"]
dmge_list = ["distance", "midpoint", "gradient", "equation"]

# Set tally values
number_of_problems = 0
number_of_calculations = 0

# Heading
print("=" * 45)
print("====== COORDINATE GEOMETRY CALCULATOR =======")
print("=" * 45)
print()
print("_" * 45)

# Ask user if they want instructions
want_instructions = string_checker("Would you like instructions? (y/n): ", yes_no_list, "Please enter either yes "
                                                                                        "/ no")

# Print the instructions
if want_instructions == "yes":
    print()
    instructions()

# Start loop
another_problem = "yes"

# Keep looping until user does not want another problem
while another_problem == "yes":

    # Add to tally of problem numbers
    number_of_problems += 1

    # Automatically want to calculate something
    another_calculation = "yes"

    # Create lists
    to_solve_list = []
    already_calculated = []

    # START OF PROGRAMME

    # Get coordinates
    while True:

        # Get ordinate values, call ordinate checker
        print("_" * 45)
        print()
        print("Enter the coordinates of an end point... (x,y)")
        x1_var = ordinate_checker("X")
        y1_var = ordinate_checker("Y")
        print()
        print("Enter the other end... (x,y)")
        x2_var = ordinate_checker("X")
        y2_var = ordinate_checker("Y")
        print("_" * 70)

        # If ordinates are equal to each-other, keep asking for ordinates
        if x1_var == x2_var and y1_var == y2_var:
            print("Error: Coordinates can not be equal!\n")

        else:
            break

    # Points string for summary
    points = f"({x1_var}, {y1_var}) to ({x2_var}, {y2_var})"

    # Remember these coordinates for the summary
    data.append(points)

    # Define the coordinates for graphing
    x_values = [x1_var, x2_var]
    y_values = [y1_var, y2_var]

    # Ask user if they want to assign a name to the given problem
    want_name = string_checker("Would you like to assign a name to this question? (y/n): ", yes_no_list,
                               "Please enter either "
                               "yes / no")

    # If yes, call not blank function and get the name
    if want_name == "yes":
        name = not_blank("Name: ")
        print("_" * 70)
        print(f"***** {name} *****")
        print(f"The line {points}\n")

    # Otherwise, just use the line coordinates as the heading
    else:
        name = None
        print("_" * 70)
        print(f"***** Line ({x1_var}, {y1_var}) to ({x2_var}, {y2_var}) *****\n\n")

    # Remember the name (or None) for the summary
    data.append(f"{name}\n\n")

    want_graph = string_checker("Would you like a graph? (y/n): ", yes_no_list, "Please enter either "
                                                                                "yes / no")

    if want_graph == "yes":
        print("\nPlease delete / save the graph to continue...")

        # Generate graph with name
        grapher(f"{name}", x1_var, y1_var, x2_var, y2_var)

    # FIRST CALCULATIONS

    # For first calculation, ask what they want to calculate (includes all mode option)
    print("\nWhat would you like to calculate?")
    initial_calculation_wanted = int_checker(
        "Distance [1], Midpoint [2], Gradient [3], Equation [4], or ALL [5]: ", 5)

    # Set mode to 'all' if chosen
    if initial_calculation_wanted == "all":
        mode = "all"

    # If they chose dmge, add what they want to both lists, for solving and remembering what's been calculated
    else:
        already_calculated.append(initial_calculation_wanted)
        to_solve_list.append(initial_calculation_wanted)
        mode = "one by one"

    # If they didn't request 'all' calculations for the problem
    if mode == "one by one":

        first_append = ""
        second_append = ""
        third_append = ""
        fourth_append = ""

        # Loop for each calculation
        while another_calculation == "yes":

            # If there's an item to solve, call the calculator function
            if to_solve_list:

                # Call the calculator function, and use the to solve list
                answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, to_solve_list[0])

                # Separate the formula, answer and working
                formula = answer_and_working[0]
                answer = answer_and_working[1]
                working = answer_and_working[2]

                # Organise the strings within the loop so that they append in the correct order for pandas
                # This took me hours to come up with :(
                if to_solve_list[0] == "distance":
                    distance_string = f"Answer = {answer} \n{working}\n\n\n"
                    first_append = distance_string
                elif to_solve_list[0] == "midpoint":
                    midpoint_string = f"Answer = {answer} \n{working}\n\n\n"
                    second_append = midpoint_string
                elif to_solve_list[0] == "gradient":
                    gradient_string = f"Answer = {answer} \n{working}\n\n\n"
                    third_append = gradient_string
                elif to_solve_list[0] == "equation":
                    equation_string = f"Answer = {answer} \n{working}\n\n\n"
                    fourth_append = equation_string

                number_of_calculations += 1

                # Formatting
                print()
                print("_" * 70)
                print(f"{to_solve_list[0].upper()}")
                print(f"For line {points}:")
                print("_" * 70)
                print(formula)
                print(working)
                print("_" * 30)

                # For equation calculations, output the answer differently
                if to_solve_list[0] == "equation":
                    print(f"  {answer}")

                # Otherwise don't
                else:
                    print(f"{to_solve_list[0].upper()} = {answer}")

                print("_" * 30)
                print()

            # After printing the last calculation wanted, ask if they'd like another one
            another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list,
                                                 "Please "
                                                 "enter "
                                                 "either "
                                                 "yes / no")

            # If they don't, break out, they will then be asked if they want another line/problem
            if another_calculation == "no":
                break

            # Reset the list so it doesn't reprint every equation
            to_solve_list = []

            # Ask what they want to calculate next (does not include all mode this time since it's not the first
            # calculation)
            print("What would you like to calculate?")
            next_calculation = int_checker(
                "Distance [1], Midpoint [2], Gradient [3], Equation [4]: ", 4)

            # If they already calculated that, tell them, then go back to top of loop, so they can re-enter
            if next_calculation in already_calculated:
                print()
                print(f"You have already calculated the {next_calculation} for this problem!\n")

            # If it has not already been calculated, add it to the lists, then go back to top of loop
            else:
                already_calculated.append(next_calculation)
                to_solve_list.append(next_calculation)

        # Once the line / problem is finished, append the items in the sort order so they format to pandas correctly
        data.append(first_append)
        data.append(second_append)
        data.append(third_append)
        data.append(fourth_append)

    # If they want 'all' calculations for the problem
    if mode == "all":

        # Heading
        print("_" * 70)
        print("**** ALL MODE ****\n")

        # For all each item in the list
        for item in dmge_list:

            number_of_calculations += 1

            # Call calculator function, use the next item in the dmge list
            answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, item)

            # Separate the formula, answer and working
            formula = answer_and_working[0]
            answer = answer_and_working[1]
            working = answer_and_working[2]

            # Remember the answer and working for the summary
            summary_string = f"Answer = {answer} \n{working}\n\n\n"
            data.append(summary_string)

            # Break up the calculations by getting user to press <enter> to continue
            print()
            input("Press <enter> to continue: ")
            print()
            print()

            # Formatting
            print("_" * 70)
            print(f"{item.upper()}")
            print(f"For line {points}:")
            print("_" * 70)
            print(formula)
            print(working)
            print("_" * 30)

            # For equation calculations, output the answer differently
            if item == "equation" and answer != "Undefined":
                print(f"  {answer}")

            # Otherwise don't
            else:
                print(f"{item.upper()} = {answer}")

            print("_" * 30)
            print()

    # After they say 'no' to another calculation, ask if they want to solve another problem
    # If they choose yes, program will go back to the top of the main loop
    # If they choose no, program will end the main loop and start printing summaries
    another_problem = string_checker("Would you like to solve a different problem / line? (y/n): ", yes_no_list,
                                     "Please enter either "
                                     "yes / no")

# CALCULATION SUMMARY

# Get the date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Heading
print("\n\n")
print("=" * 40)
print("========= CALCULATION SUMMARY ==========")
print("=" * 40)

summary_frame = pd.DataFrame(
    {
        "Coordinates": data[0::6],
        "Question Name": data[1::6],
        "Distance": data[2::6],
        "Midpoint": data[3::6],
        "Gradient": data[4::6],
        "Equation": data[5::6],
    }
)
# Format the frame nicely and print
table_formatting(summary_frame)

# Thank the user
print("\nThe calculation summary has been sent to your files\n")
print("Thankyou for using Coordinate Geometry Calculator by Jack Pringle!")



# Create file to hold data (add .txt extension)
file_name = f"Calculation Summary {day}_{month}_{year}.txt"

# Create a text file for the user
with open(file_name, "w+") as text_file:
    # File heading
    text_file.write("=" * 45 + "\n")
    text_file.write("======= COORDINATE GEOMETRY SUMMARY =========" + "\n")
    text_file.write("=" * 14 + f"   {day} {month} {year}    " + "=" * 14 + "\n")
    text_file.write("=" * 45 + "\n\n")

    # Add the rows to the text file
    for index, row in summary_frame.iterrows():

        # Write each row's data
        for col, value in row.items():
            text_file.write(f"{col}: {value}\n")

        # Write problem separator
        text_file.write("=" * 60 + "\n")

# Close file
text_file.close()
