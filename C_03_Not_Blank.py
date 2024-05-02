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

while True:
    # Ask user what name they want to assign to the question
    question_name = not_blank("Name: ")

    # If they have chosen to quit, output the name they chose
    if question_name != "xxx":
        print(f"{question_name}")
        break

    else:
        print("You have chosen to quit")
        break
