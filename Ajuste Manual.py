import serial
ser = serial.Serial('COM4', 9600) # Establish the connection on a specific port

info1=10
info2=3
senal_envio="a"+str(info1)+"b"+str(info2)
ser.write(senal_envio) # Convert the decimal number to ASCII then send it to the Arduino
cont=0
on=True
while on:
    x=str(raw_input("Ingrese: "))
    if x==-1 or x=="exit":
        on=False
    else:
        ser.write(x)
    
