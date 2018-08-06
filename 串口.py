import serial,time,random

ser = serial.Serial("COM2",9600,timeout=5)

ok = bytes([160,1,1,162])
no = bytes([160,1,0,161])
while True:
    a = random.randint(1,10)
    time.sleep(a)
    ser.write(ok)
    print(1,end='\r')
    time.sleep(a)
    ser.write(no)
    print(2,end='\r')
ser.close()