import serial
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)
ser.write("UART the Font")
read = ser.read(15)
print read
ser.close()
