print("Hello Tester!\n Now We Are Going To See How This Works")
from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)

push_button = Pin(13,Pin.IN)

while True:
    logic_state = push_button.value()
    if logic_state == True:
        led.value(1)
    else:
        led.value(0)