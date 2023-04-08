# Pico 1 (END TO END)
import machine
import utime

spi = machine.SPI(0, baudrate=1000000, sck=machine.Pin(0), mosi=machine.Pin(1), miso=machine.Pin(2))
cs1 = machine.Pin(3, machine.Pin.OUT)
cs2 = machine.Pin(4, machine.Pin.OUT)

while True:
    data = bytearray([1, 2, 3, 4, 5])
    cs1.value(0)
    spi.write(data)
    cs1.value(1)
    utime.sleep_ms(1000)
    cs2.value(0)
    response = spi.read(5)
    cs2.value(1)
    print(response)



# Pico 2 (END TO END)
import machine

spi = machine.SPI(0, baudrate=1000000, sck=machine.Pin(0), mosi=machine.Pin(1), miso=machine.Pin(2))
cs1 = machine.Pin(3, machine.Pin.OUT)
cs2 = machine.Pin(4, machine.Pin.OUT)

while True:
    cs1.value(0)
    data = spi.read(5)
    cs1.value(1)
    print(data)
    cs2.value(0)
    spi.write(data)
    cs2.value(1)