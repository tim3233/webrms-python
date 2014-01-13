#Quick&Dirty Python-Datalogger for Carrera Digital
#Please add "try/except" for serial port by yourself
#licensed under GNU GENERAL PUBLIC LICENSE Version 2

import serial
import time

#define serial port
ser = serial.Serial('/dev/cu.NoZAP-PL2303-000013FA', 19200, timeout=0.05)

line_saved=0

while 1<2:
        ser.write("\"?")
        line = ser.readline()
        print(line)
        
        #check if line has a new value
        if line!=line_saved:
                        
                ascii_string = line

                #read first bit = Controller
                first_bit = ascii_string[1:2]
                car_controller=first_bit

                #if first bit != : its a round finish
                if first_bit!=":":
                        #cut string
                        ascii_string = ascii_string[4:10]
                
                        #sort string and convert to hex
                        hex_string=ascii_string[1:2].encode("hex")[1:2]+ascii_string[0:1].encode("hex")[1:2]
                        hex_string+=ascii_string[3:4].encode("hex")[1:2]+ascii_string[2:3].encode("hex")[1:2]
                        hex_string+=ascii_string[5:6].encode("hex")[1:2]+ascii_string[4:5].encode("hex")[1:2]
                
                        #convert to decimal
                        decimal=int(hex_string, 16)
                        timer=str(decimal);
        
                        #print for testing
                        print("Auto:" + car_controller)
                        print("Zeitstempel:" + timer +"ms")
                
                        #write logfile for each car
                        datafile = open("car."+car_controller+".rnd", "a")
                        print >> datafile, timer
                        datafile.close()
                        
                        line_saved=line
                        time.sleep(.02)
                        
ser.close()
