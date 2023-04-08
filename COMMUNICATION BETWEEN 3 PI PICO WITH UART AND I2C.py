# Pico (MASTER)
import machine
import utime

i2c = machine.I2C(0, scl=machine.Pin(19), sda=machine.Pin(18))
addr1 = 0x10
addr2 = 0x20

while True:
    data = bytearray([1, 2, 3, 4, 5])
    i2c.writeto(addr1, data)
    utime.sleep_ms(1000)
    response = i2c.readfrom(addr2, 5)
    print(response)

uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))
addr1 = 0x10
addr2 = 0x20

while True:
    data = bytearray()
    while uart.any():
        data.extend(uart.read(5))
    print(data)
    uart.write(data)


# Pico 2  SLAVE
import machine

i2c = machine.I2C(0, scl=machine.Pin(0), sda=machine.Pin(1))
addr1 = 0x10
addr2 = 0x20

while True:
    data = i2c.readfrom(addr1, 5)
    print(data)
    i2c.writeto(addr2, data)


    # Pico 3 SLAVE
import machine
import utime

uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))
addr1 = 0x10
addr2 = 0x20

while True:
    data = bytearray([1, 2, 3, 4, 5])
    uart.write(data)
    utime.sleep_ms(1000)
    response = bytearray()
    while uart.any():
        response.extend(uart.read(5))
    print(response)