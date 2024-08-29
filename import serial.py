import serial #Encapsulates the access for the serial port.

uno_port = "COM3" #right side
baud = 9600 #communication speed between your computer and the Arduino
file_name = "sensor_data.csv"
print_label = False
line= 0

ser = serial.Serial(uno_port, baud)
print(f"Connected to Arduino Port {uno_port}") 
file = open(file_name, "w") #w=write mode
print("File Created. ")


while True: #starts an infinite loop that continues to run indefinitely (keep reading and writing data until it's manually stopped)

    getData = str(ser.readline())
    data = getData[2:][:-5] #to clean up the data [slide off the first 2 character('b'); remove the last 5 characters('/r/n')]
    print(data) #prints the cleaned-up data to the console.

    file = open(file_name,"a") #a=append mode: allowing new data to be added without overwriting the existing content
    file.write(data + "\n")

file.close()