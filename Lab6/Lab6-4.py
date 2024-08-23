import RPi.GPIO as GPIO
import time
SW = 22
RED = 14
GREEN = 15
BLUE = 18
count = 0
state = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        if GPIO.wait_for_edge(SW,GPIO.FALLING):
            count += 1
            if count > 7:
                count = 0
            bin_count = format(count, '03b')
            red_state = int(bin_count[0])
            green_state = int(bin_count[1])
            blue_state = int(bin_count[2])
            GPIO.output(RED,red_state)
            GPIO.output(GREEN,green_state)
            GPIO.output(BLUE,blue_state)
            print(f"Button pressed {count}: Red={red_state}, Green={green_state}, Blue={blue_state}")
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye...")