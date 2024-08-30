import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

# Create a figure and a set of subplots (e.g., 3 rows and 1 column)
fig, axs = plt.subplots(3, 1, figsize=(8, 6))

# Set the axis range 
x_range = 30
y_range = 400

def animate(i):
    data = pd.read_csv('sensor_data.csv')

    # Loop through each subplot and update the data
    for j, ax in enumerate(axs):
        ax.cla()  # Clear the current axes

        # Extract the relevant columns for x and y values
        x_vals = data['Index']
        y_vals = data[f'Distance{j+1}']  # Dynamically select Distance1, Distance2, Distance3

        # Plot the data
        ax.plot(x_vals, y_vals, color="red")

        # Hide the labels
        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(False)  

        # Determine the current x-axis range
        if len(x_vals) > 0:
            ax.set_xlim(max(0, x_vals.iloc[-1] - x_range), x_vals.iloc[-1])
            ax.set_ylim(0, 400)  # Assuming y-values range from 0 to 400

    plt.tight_layout()  # Automatically adjusts subplot parameters

# Set the tittle for both 3 graph
fig.suptitle("Distance from sensor (cm)")

# Create the animation object
ani = FuncAnimation(fig, animate, interval=1000)

plt.tight_layout()
plt.show()
