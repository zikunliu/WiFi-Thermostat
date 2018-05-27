import serial, time
import re
serial_port = '/dev/ttyACM0';
baud_rate = 9600;
ser = serial.Serial(serial_port, baud_rate);
def get_temp_from_Arduino(cur_temp):
    data = str(ser.readline())
    if(re.search(r'\d',data)):
        temp=re.findall(r'\d',data)
        a=''
        a=a.join(temp)
        b=int(a)
        print(b)
        if(b>30 and b<110):
            c=b
            return b
    else:
        return cur_temp

