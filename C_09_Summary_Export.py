import pandas
from datetime import date

# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

title = "Calculation Summary"
points = "(1, 2) to (3, 4)"
name = "Question (a)"
distance = ""
midpoint = ""
gradient = ""
equation = ""

table_dict = {
    "Line": [points],
    "Question Name": [name],
    "Distance": [distance],
    "Midpoint": [midpoint],
    "Gradient": [gradient],
    "Equation": [equation]
}

table_dict = pandas.DataFrame(table_dict)

# Change frames to strings
table_txt = pandas.DataFrame.to_string(table_dict)

to_write = [title, table_txt]

# Write to file...
# Create file to hold data (add .txt extension)
file_name = f"Calc_Summary_{day}_{month}_{year}.txt"
text_file = open(file_name, "w+")

# Heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close file
text_file.close()

# Print stuff
for item in to_write:
    print(item)
    print()
