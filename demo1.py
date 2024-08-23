import serial
import time  # Import the time module for timestamps

# Directory (not necessary in the script itself, but shown here for context)
'''
cd Desktop/Robotix/Arduino_Projects/Time_Series
'''

uno_port = "COM4"  # Change to COM4 as per your setup
baud = 9600
file_name = "sensor_data.csv"
print_label = False

# Set up serial connection
ser = serial.Serial(uno_port, baud)
print(f"Connected to Arduino Port {uno_port}")

# Open the file once
file = open(file_name, "w")
print("File Created")

# Write the header to the CSV file
file.write("Timestamp,Data\n")

try:
    while True:
        getData = str(ser.readline())
        data = getData[2:][:-5]  # Trims the newline characters

        # Get the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Print data (optional)
        if print_label:
            print(f"{timestamp}, {data}")

        # Append timestamped data to the file
        file.write(f"{timestamp},{data}\n")

except KeyboardInterrupt:
    print("Data collection stopped.")

finally:
    # Close the file and serial connection
    file.close()
    ser.close()
    print("File Closed and Serial Connection Terminated")