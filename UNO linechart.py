import pandas as pd #work with structured data, reading and manipulating csv file
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation #allows the creation of animations by repeatedly calling a function at specified intervals

plt.style.use('Solarize_Light2')

def animate(i):
    data = pd.read_csv('sensor_data.csv')
    x_vals = data['Index']
    y_vals = data['Distance']
    
    plt.cla() #Clear the current axes to prevent old data from being drawn over new data.

    plt.plot(x_vals, y_vals, color="red")
    plt.title("Distance from sensor (cm) vs Time (seconds)")
    plt.ylabel("Distance from sensor (cm)")
    plt.xlabel("Time (sec)")
    plt.tight_layout() #Automatically adjusts subplot parameters to give specified padding

ani = FuncAnimation(plt.gcf(), animate, interval=1000) #plt.gcf()=Automatically adjusts subplot parameters to give specified padding

plt.tight_layout()
plt.show()