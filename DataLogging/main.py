from datetime import datetime
import serial
import time
import csv

now = datetime.today().strftime('_%Y_%m_%d__%H_%M_%S')
file = ("test_stand_data"+now+".csv")
print("Writing to: ", file)

serialPort = serial.Serial(
    port="COM3", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
serialString = ""  # Used to hold data coming over UART
while 1:
    # Read data out of the buffer until a carraige return / new line is found
    serialString = serialPort.readline()
    serialString = serialString.decode().replace("\n", "")
    # Print the contents of the serial data
    try:
        with open(file,"a") as f:
            writer = csv.writer(f,delimiter=",", dialect='excel')
            writer.writerow([time.time(), int(serialString)]) #datetime.today().isoformat()
    
    except:
        pass
