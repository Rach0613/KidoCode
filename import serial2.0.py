import pandas as pd #work with structured data, reading and manipulating csv file
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation #allows the creation of animations by repeatedly calling a function at specified intervals

plt.style.use('dark_background')

# Create a figure and a set of subplots (e.g., 1 row and 1 column)
fig, ax = plt.subplots(figsize=(8, 6)) # specifies the size of the figure in inches. 1 - width, the 2 - height

# Set the width range of the x-axis 
x_range = 50

def animate(i):
    data = pd.read_csv('sensor_data.csv')
    x_vals = data['Index']
    y_vals = data['Distance']

    ax.cla()  # Clear the current axes, prevents the old data from lingering on the plot.

    # Plot the data
    ax.plot(x_vals, y_vals, color="red")

    # Set the title and labels
    ax.set_title("Distance from sensor (cm)")
    #ax.set_ylabel("Distance from sensor (cm)")
    ax.get_xaxis().set_visible(False)  # Hide the x-axis

    #ax.grid(False)  # Turn off the grid of graph
    #ax.set_facecolor('none')  # Set the background color to none (transparent)

    # Determine the current x-axis range
    if len(x_vals) > 0:
        #Sets the x-axis limits to show only the most recent data within the defined range. 
        #This creates a scrolling effect as new data comes in.
        ax.set_xlim(max(0, x_vals.iloc[-1] - x_range), x_vals.iloc[-1]) #

    plt.tight_layout()  # Automatically adjusts subplot parameters

# Create the animation object (call animate f(x) repeatedly every 1000,sces)
# The fig parameter specifies the figure to be animated.
ani = FuncAnimation(fig, animate, interval=1000)

plt.tight_layout()
plt.show()
