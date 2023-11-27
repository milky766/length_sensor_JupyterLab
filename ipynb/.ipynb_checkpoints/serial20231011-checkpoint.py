import serial
import datetime
import time

com = serial.Serial("COM4", 9600)

path = './csv/'

file_name = str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sec_finish= 55
print('start!')

t0 = time.time()

with open(path+file_name+".csv", "a",encoding='cp1252') as f:
    print("time(s),p1(kPa),p2(kPa),flow(L/min),Voltage(V)",file=f)   
    while True:
        t = time.time()
        t_inner = t - t0
        if t_inner > sec_finish:
            print("saved as "+file_name+".csv"+"!")  
            break
        val = str(com.readline().decode('cp1252').rstrip("\r\n"))
        if t_inner > 0.05:
            print("{}".format(val), file=f)
com.close() 
