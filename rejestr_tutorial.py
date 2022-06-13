import RPi.GPIO as GPIO
import time
import string

SER = 2
SRCLK = 4
RCLK = 3

bin_tab = []

#fainy init
def init_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SER, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setwarnings(True)

#gunwo
def funkcyjsko(dupsko="11110000"):
    GPIO.output(RCLK, GPIO.LOW)
    for i in range(8):
        GPIO.output(SRCLK, 0)
        GPIO.output(SER, int(dupsko[i]))
        GPIO.output(SRCLK, 1)

    GPIO.output(RCLK, GPIO.HIGH)

#odliczanie binarnem:
def binary_finalCountdown():
    for i in range (256):
        num = format(i, "b")
        if len(num) <= 8:
            temp = ""
            for j in range (8-len(num)):
                temp += "0"
            temp += str(num)
            bin_tab.append(temp)
        
    for i in range (len(bin_tab)):
        print(str(bin_tab[i]))
        time.sleep(.2)
        funkcyjsko(bin_tab[i])



#int main hehe
numbers = ["00000001", "00000010"]

init_GPIO()
try:
    while True:
        binary_finalCountdown()
except KeyboardInterrupt:
    funkcyjsko("00000000")