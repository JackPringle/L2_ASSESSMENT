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


# Main Routine...

# Lists of valid responses
yes_no_list = ["yes", "no"]

line_number = 0
number_of_calculations = 0
another_line = "yes"
another_calculation = "yes"
another_calculation_question = "Would you like to calculate something else? (y/n): ", yes_no_list, "Please enter " \
                                                                                                   "either yes / no"


while another_line == "yes":

    another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list, "Please "
                                                                                                             "enter "
                                                                                                             "either"
                                                                                                             "yes / no")

    while another_calculation == "yes":
        print("Work all of the calculations out here\n")
        another_calculation = string_checker("Would you like to calculate something else? (y/n): ", yes_no_list,
                                             "Please "
                                             "enter "
                                             "either"
                                             "yes / no")

    another_line = string_checker("Would you like to enter another line? (y/n): ", yes_no_list, "Please enter either "
                                                                                                "yes / no")

print("Congrats you broke out of the loop!")
