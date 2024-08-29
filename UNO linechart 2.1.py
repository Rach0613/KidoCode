import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random  # Simulating live data input

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Initialize empty data lists
xdata, ydata = [], []

# Set up plot limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)

def init():
    """Initialize the background of the plot"""
    line.set_data([], [])
    return line,

def update(frame):
    """Update the data"""
    # Simulate data collection
    xdata.append(frame)
    ydata.append(random.uniform(0, 10))  # Replace this with real data
    
    # Set the data for the line
    line.set_data(xdata, ydata)
    
    # If needed, adjust the limits dynamically
    ax.set_xlim(0, max(xdata))
    ax.set_ylim(0, max(ydata) + 1)
    
    return line,

# Call the animation function
ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

plt.show()
