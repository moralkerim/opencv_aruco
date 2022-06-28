import time
import serial
import struct

detected = 1
x	 = 120
y	 = 150
zcam = 200
yaw  = 260



#values = (detected, x, y, zcam, yaw)

string = b''


ser = serial.Serial("/dev/ttyS0",   
	baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 1
    
)

string = struct.pack('<BBBBH',detected,x,y,zcam,yaw)


while 1:
	print("Printing.")
	ser.write(string)
	time.sleep(5)
	
	
