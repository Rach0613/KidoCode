import serial
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Set up the serial connection
ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with your port
data = []

try:
    print("Starting data collection. Press Ctrl+C to stop.")
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            # Check if the line contains 'cm' and extract the numeric value
            if 'cm' in line:
                distance = line.replace('cm', '').strip()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data.append([timestamp, distance])
                
except KeyboardInterrupt:
    print("Data collection stopped.")

finally:
    ser.close()

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Timestamp', 'Distance'])

# Save to CSV
df.to_csv('sensor_data.csv', index=False)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Distance'], marker='o', linestyle='-', color='b')
plt.xlabel('Timestamp')
plt.ylabel('Distance (cm)')
plt.title('Distance Measurements Over Time')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(True)
plt.savefig('distance_plot.png')
plt.show()