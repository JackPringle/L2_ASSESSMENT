# Functions...

# Checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # If the response is blank after stripping whitespace, output error
        if response == "":
            print("Sorry this can't be blank. Please try again\n")

        else:
            return response


# Main Routine...

# Loop for testing
while True:
    # Ask user what name they want to assign to the question
    question_name = not_blank("Name: ")
    print("Program continues")

