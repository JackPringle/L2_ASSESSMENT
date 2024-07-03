import pandas as pd
from prettytable import PrettyTable
from datetime import date


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

    for col_var in ["Addition", "Subtraction"]:
        table.align[col_var] = 'l'

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
for item in range(0, 2):
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

    # Addition print string
    addition_working = (f'''Answer = {addition}
WORKING:
A = {x1_var} + {y1_var} + {x2_var} + {y2_var}
  = {x1_var + y1_var} + {x2_var + y2_var}
  = {x1_var + y1_var + x2_var + y2_var}\n\n\n''')

    # Subtraction print string
    subtraction_working = (f'''Answer = {subtraction}
WORKING:
S = {x1_var} - {y1_var} - {x2_var} - {y2_var}
  = {x1_var - y1_var} - {x2_var - y2_var}
  = {x1_var - y1_var - x2_var - y2_var}\n\n\n''')

    # In base code, will need to add these to the lists from separate points
    data.append(points)
    data.append(f"{name}\n\n")
    data.append(addition_working)
    data.append(subtraction_working)

# Calculation Summary

# Create DataFrame
# Separate elements from the data list and assign them to the columns
# If not done like this, the programme will break as it doesn't like the way we've added
# things to the data list one by one
summary_frame = pd.DataFrame(
    {
        "Coordinates": data[0::4],
        "Question Name": data[1::4],
        "Addition": data[2::4],
        "Subtraction": data[3::4],
    }
)

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
file_name = f"Calculation Summary {day}_{month}_{year}.txt"

# Open file for writing
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
        text_file.write("=" * 45 + "\n")

# Close file
text_file.close()
