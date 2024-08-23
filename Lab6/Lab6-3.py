import RPi.GPIO as GPIO
import time

SW = 22
LED = 18
count = 0
state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.wait_for_edge(SW,GPIO.FALLING):
            count += 1
            state = not(state)
            GPIO.output(LED,state)
            if state:
                print(f"Button pressed {count}: LED ON")
            else:
                print(f"Button pressed {count}: LED OFF")
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye...")