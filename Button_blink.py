import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
while(1):
    if(GPIO.input(24) == 0):
        print("Button pressed")
        for i in range(3):
            GPIO.output(5, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(5, GPIO.LOW)
            time.sleep(0.5)
    else:
        print("Button released")
        GPIO.output(5, GPIO.LOW)