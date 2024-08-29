import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

# Create a figure and a set of subplots (e.g., 1 row and 1 column)
fig, ax = plt.subplots(figsize=(8, 6))

# Set the width of the visible x-axis range (e.g., 50 units)
x_range = 50

def animate(i):
    data = pd.read_csv('sensor_data.csv')
    x_vals = data['Index']
    y_vals = data['Distance']

    ax.cla()  # Clear the current axes

    # Plot the data
    ax.plot(x_vals, y_vals, color="red")

    # Set the title and labels
    ax.set_title("Distance from sensor (cm)")
    ax.set_ylabel("Distance from sensor (cm)")
    ax.get_xaxis().set_visible(False)  # Hide the x-axis

    # Remove grid and make background transparent
    ax.grid(False)  # Turn off the grid
    #ax.set_facecolor('none')  # Set the background color to none (transparent)

    # Determine the current x-axis range
    if len(x_vals) > 0:
        ax.set_xlim(max(0, x_vals.iloc[-1] - x_range), x_vals.iloc[-1])

    plt.tight_layout()  # Automatically adjusts subplot parameters

# Create the animation object
ani = FuncAnimation(fig, animate, interval=1000)

plt.tight_layout()
plt.show()
