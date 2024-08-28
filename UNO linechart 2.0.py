import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('Solarize_Light2')

# Set the width of the visible x-axis range (e.g., 50 units)
x_range = 50

def animate(i):
    data = pd.read_csv('sensor_data.csv')
    x_vals = data['Index']
    y_vals = data['Distance']

    plt.cla()  # Clear the current axes

    # Plot the data
    plt.plot(x_vals, y_vals, color="red")

    # Set the title and labels
    plt.title("Distance from sensor (cm) vs Time (seconds)")
    plt.ylabel("Distance from sensor (cm)")
    plt.xlabel("Time (sec)")

    # Determine the current x-axis range
    if len(x_vals) > 0:
        # Set the x-axis range to the last 'x_range' values
        plt.xlim(max(0, x_vals.iloc[-1] - x_range), x_vals.iloc[-1])

    plt.tight_layout()  # Automatically adjusts subplot parameters

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()