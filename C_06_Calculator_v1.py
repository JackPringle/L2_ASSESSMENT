import math


# Functions...

def calculator(x1, y1, x2, y2, to_solve):
    if "distance" in to_solve:
        ans = x1 + y1 + x2 + y2
        work = f"{x1} + {y1} + {x2} + {y2}"

    elif "midpoint" in to_solve:
        ans = x1 - y1 - x2 - y2
        work = f"{x1} - {y1} - {x2} - {y2}"

    elif "gradient" in to_solve:
        ans = "gradient answer here"
        work = "working"

    elif "equation" in to_solve:
        ans = "equation answer here"
        work = "working"

    else:
        ans = None
        work = None

    return ans, work


# Main Routine...

x1_var = 1
y1_var = 2
x2_var = 3
y2_var = 4

mode = input("What mode? (all or one): ")

to_solve_list = []

if mode == "one":

    next_calculation = input("What would you like to calculate? ")
    to_solve_list.append(next_calculation)
    print()

    answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, to_solve_list[0])
    answer = answer_and_working[0]
    working = answer_and_working[1]

    for item in to_solve_list:
        print(f"The answer is: {answer}")
        print(f"The working is: {working}")
        print()

if mode == "all":

    dmge_list = ["distance", "midpoint", "gradient", "equation"]

    # For all of dmge, break up the calculations by getting user to press <enter> to continue
    for item in dmge_list:

        answer_and_working = calculator(x1_var, y1_var, x2_var, y2_var, item)
        answer = answer_and_working[0]
        working = answer_and_working[1]
        input("Press <enter> to continue: ")
        print()
        print(f"** {item} calculation here **\n")
        print(f"Answer: {answer}")
        print(f"Working: {working}")
        print()


