import RPi.GPIO as GPIO
import time

red_2 = 17
red_1 = 4
blue_2 = 3
blue_1 = 2

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red_1, GPIO.OUT)
    GPIO.setup(red_2, GPIO.OUT)
    GPIO.setup(blue_1, GPIO.OUT)
    GPIO.setup(blue_2, GPIO.OUT)

def loop():
    while True:
        try:
            GPIO.output(blue_1, GPIO.LOW)
            GPIO.output(blue_2, GPIO.LOW)
            GPIO.output(red_1, GPIO.HIGH)
            GPIO.output(red_2, GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(red_1, GPIO.LOW)
            GPIO.output(red_2, GPIO.LOW)
            GPIO.output(blue_1, GPIO.HIGH)
            GPIO.output(blue_2, GPIO.HIGH)
            time.sleep(.5)
        except KeyboardInterrupt:
            GPIO.cleanup()

init()
loop()
