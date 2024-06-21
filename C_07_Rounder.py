# Functions...

# Gets calculated answer and rounds depending on float / integer
def rounder(answer):

    # For integer answers, remove any trailing 0's from decimals
    if answer.is_integer():
        answer = int(answer)

    # For float answers, round to 3 decimals
    else:
        answer = f"{answer:.3f}"
        answer = f"{answer:g}"

    # Return the rounded answer
    return answer


# Main Routine...

# Hard coded answer for testing
ans = 5.43000001

# Call function
rounded_ans = rounder(ans)

# Output values for comparison
print(f"The answer = {ans}")
print(f"The rounded answer = {rounded_ans}")
