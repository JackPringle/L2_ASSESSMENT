import matplotlib.pyplot as plt


# Functions...

# Uses the coordinates to generate a line graph for visualisation
def grapher(title, x1, y1, x2, y2):

    # Group the coordinates
    x_values = [x1, x2]
    y_values = [y1, y2]

    # Change the graphs filename
    plt.figure(num=f"{title} / graph")

    # Set axis limits to ensure both x and y axes are visible
    plt.xlim(min(x1, x2) - 1, max(x1, x2) + 1)
    plt.ylim(min(y1, y2) - 1, max(y1, y2) + 1)

    # Set equal scaling for both axes
    plt.axis('equal')

    # Plot the line
    plt.plot(x_values, y_values, marker='o')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)

    # Show x and y-axis
    plt.grid(True)
    plt.axhline(0, color='red', linewidth=3)
    plt.axvline(0, color='red', linewidth=3)

    # Display the plot
    plt.show()


# Main Routine...

# Get coordinates
x1_var = float(input("X1: "))
y1_var = float(input("Y1: "))
x2_var = float(input("X2: "))
y2_var = float(input("Y2: "))
print()

# Get the name for the graph
name = input("Name: ")

# Call the function
grapher(name, x1_var, y1_var, x2_var, y2_var)
