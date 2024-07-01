import pandas as pd
from prettytable import PrettyTable
from datetime import date


# Formats the panda frame
def table_formatting(dataframe):

    # Make the table using the pretty table library
    table = PrettyTable()

    # Add columns from the DataFrame
    table.field_names = dataframe.columns.tolist()

    # Add columns from the DataFrame
    for _, row in dataframe.iterrows():
        table.add_row(row.tolist())

    # Align the columns differently
    for col in ["Coordinates", "Question Name"]:
        table.align[col] = 'c'

    for col in ["Addition", "Subtraction"]:
        table.align[col] = 'l'

    # Set style and border options
    table.header_style = "upper"
    table.horizontal_char = "_"
    table.junction_char = "+"
    table.vertical_char = "|"

    # Print the table
    print(table)


# Main Routine...
# Using only addition and subtraction to simplify component

# Create a list of all the data that needs to be added to panda for each problem / line
data = []

# Loop for testing
for item in range(0, 1):

    # Get coordinates
    x1_var = float(input("X1: "))
    y1_var = float(input("Y1: "))
    x2_var = float(input("X2: "))
    y2_var = float(input("Y2: "))

    # Get a question name
    name = input("Name: ")

    # Write the coordinates string
    points = f"({x1_var}, {y1_var}) to ({x2_var}, {y2_var})"

    # Calculations
    addition = x1_var + x2_var + y1_var + y2_var
    subtraction = x1_var - x2_var - y1_var - y2_var

    # Addition answer
    addition_answer = f"Addition = {addition}"

    # Addition working
    addition_working = (f'''Addition working here...
..................
...................
...................
....................''')

    # Subtraction answer
    subtraction_answer = f"Subtraction = {subtraction}"

    # Subtraction working
    subtraction_working = (f'''Subtraction working here...
..................
...................
...................
....................''')

    # Combine the answer and working
    addition_print = f"{addition_answer}\n\n{addition_working}"
    subtraction_print = f"{subtraction_answer}\n\n{subtraction_working}"

    # Add the data from the problem to the list
    data.append([points, name, addition_print, subtraction_print])


# Calculation Summary

# Add all data from session to the panda
summary_frame = pd.DataFrame(data, columns=["Coordinates", "Question Name", "Addition", "Subtraction"])

# Format the frame nicely and print
table_formatting(summary_frame)

# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Write to file...
# Create file to hold data (add .txt extension)
file_name = f"Calculation Summary {day} {month} {year}.txt"
text_file = open(file_name, "w+")

# Heading
for item in summary_frame:
    text_file.write(item)
    text_file.write("\n\n")

# Close file
text_file.close()
