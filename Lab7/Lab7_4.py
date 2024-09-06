import RPi.GPIO as GPIO
import drivers
from time import sleep

SW1 = 27
SW2 = 22
display = drivers.Lcd()
display.lcd_clear()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
current_state = 0

try:
    while True:
        if GPIO.event_detected(SW1):
            if current_state == 0:
                display.lcd_clear()
                display.lcd_display_string("Chusanapak Fongmanee", 1)
                display.lcd_display_string("116630462001-4",2)
                current_state = 1
            elif current_state == 1:
                display.lcd_clear()
                display.lcd_display_string("Tipog Boonyanupong", 1)
                display.lcd_display_string("116630462010-5",2)
                current_state = 0
        elif GPIO.event_detected(SW2):
            display.lcd_clear()
            display.lcd_display_string("BYE !!!", 1)
            sleep(1)
            display.lcd_clear()
            break
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO cleanup completed")