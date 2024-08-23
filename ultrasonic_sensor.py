import serial
import time
import csv

# Open serial port
ser = serial.Serial('COM4', 9600)  # Change COM3 to your port
time.sleep(2)  # Wait for Arduino to initialize

# Open a CSV file to write data
with open('ultrasonic_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Time (ms)', 'Distance (cm)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Read data from serial and write to CSV
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                time_ms, distance_cm = line.split(',')
                writer.writerow({'Time (ms)': time_ms, 'Distance (cm)': distance_cm})
                print(f"Time: {time_ms} ms, Distance: {distance_cm} cm")
        except KeyboardInterrupt:
            print("Data collection stopped")
            break

# Close serial port
ser.close()