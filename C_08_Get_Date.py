from datetime import date

# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Get the heading and filename
heading = f"The current date is {day}/{month}/{year}"
filename = f"Calc_Summary_{day}_{month}_{year}"

# Print headings
print(heading)
print(f"The filename will be {filename}.txt")
