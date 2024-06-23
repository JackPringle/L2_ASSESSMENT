# Functions...

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

    # If the rounded answer is -0, remove the negative sign
    if ans == -0 or ans == "-0":
        ans = int(ans)

    # Return the rounded answer
    return ans


# Main Routine...

# Loop for testing purposes
while True:
    # Get answer as float for testing
    answer = input("The answer = ")
    answer = float(answer)

    # Call function
    rounded_answer = rounder(answer)

    # Output rounded answer
    print(f"The rounded answer = {rounded_answer}\n")

