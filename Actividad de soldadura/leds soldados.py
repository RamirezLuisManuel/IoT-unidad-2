from machine import Pin
import time

# Definir los pines GPIO donde están conectados los LEDs
led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(5, Pin.OUT)
led4 = Pin(12, Pin.OUT)
led5 = Pin(13, Pin.OUT)
led6 = Pin(14, Pin.OUT)
led7 = Pin(15, Pin.OUT)
led8 = Pin(16, Pin.OUT)
led9 = Pin(17, Pin.OUT)
led10 = Pin(18, Pin.OUT)

leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10]

def led_sequence(delay=0.5):
    while True:
        # Encender los LEDs uno por uno
        for led in leds:
            led.value(1)
            time.sleep(delay)
            led.value(0)

try:
    led_sequence(0.3)  # Puedes cambiar el tiempo de delay
except KeyboardInterrupt:
    # Apagar todos los LEDs al detener el programa
    for led in leds:
        led.value(0)
    print("Programa detenido")
