#PI4 (MASTER)
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while True:
    ser.write(b'Connection to Raspberry Pi 4\n')
    time.sleep(1)
    response = ser.readline().strip()
    if response:
        print(response.decode()) 

       


#PICO (SLAVE)
import machine
import time

uart = machine.UART(0, baudrate=115200)

while True:
    if uart.any():
        message = uart.readline().strip()
        print(message.decode())
        uart.write(b'Hello from Raspberry Pi Pico\n')
        time.sleep(1)
'''In this example, the code creates a UART object and continuously checks for incoming data using the any method. When it receives a message, it prints it to the terminal and sends a response "Connection from Raspberry Pi Pico" using the write method.'''

