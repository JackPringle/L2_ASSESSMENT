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


# Main Routine...

# Lists of valid responses
yes_no_list = ["yes", "no"]

# Loop for testing purposes
for item in range(0, 6):

    # Ask user if they want instructions
    want_instructions = string_checker("Would you like instructions? (y/n): ", yes_no_list, "Please enter either yes "
                                                                                            "/ no")

    # Print the instructions
    if want_instructions == "yes":
        print()
        instructions()
