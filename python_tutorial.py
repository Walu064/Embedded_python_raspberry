from ctypes import sizeof
from operator import length_hint
import string
import RPi.GPIO as GPIO
import time
import os

list_tooMany = []
list_missing = []
alfabet_dictonary = {}

#obsługa świecidełek:
red_2 = 17
red_1 = 4
green_2 = 3
green_1 = 2

def init_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red_1, GPIO.OUT)
    GPIO.setup(red_2, GPIO.OUT)
    GPIO.setup(green_1, GPIO.OUT)
    GPIO.setup(green_2, GPIO.OUT)
    GPIO.output(green_1, GPIO.LOW)
    GPIO.output(green_2, GPIO.LOW)
    GPIO.output(red_1, GPIO.LOW)
    GPIO.output(red_2, GPIO.LOW)
    GPIO.setwarnings(True)

def correct_pangram():
    GPIO.output(green_1, GPIO.HIGH)
    GPIO.output(green_2, GPIO.HIGH)
    GPIO.output(red_1, GPIO.LOW)
    GPIO.output(red_2, GPIO.LOW)

def incorrect_pangram():
    GPIO.output(red_1, GPIO.HIGH)
    GPIO.output(red_2, GPIO.HIGH)
    GPIO.output(green_1, GPIO.LOW)
    GPIO.output(green_2, GPIO.LOW)

def check_pangram():
    if len(list_tooMany) == 0 and len(list_missing) == 0:
        correct_pangram()
    else:
        incorrect_pangram()

#rozwiązanie zadania z przekazaniem jako argumenty tesotwych stringów 0
def is_pangram():

    alfabet = input("Wprowadź alfabet: ")
    alfabet = alfabet.upper()
    sign_1 = input("Wprowadź napis: ")
    sign_1 = sign_1.upper()
    
    for i in range(len(alfabet)):
        alfabet_dictonary [alfabet[i]] = 0

    for letter in sign_1:
        if letter in alfabet_dictonary:
            alfabet_dictonary[letter] += 1
        else:
            if letter != ' ' or letter != '.':
                if not(letter in list_missing):
                    list_missing.append(letter)

    for letter, value in alfabet_dictonary.items():
        if value > 1:
            list_tooMany.append(letter)
        if value == 0:
            list_missing.append(letter)
    
    print("Wprowadzony alfabet: ", alfabet)
    print("Wprowadzony napis: ", sign_1)
    print("Wystąpiły więcej niż jeden raz: ", list_tooMany)
    print("Brakujące litery: ", list_missing)
    check_pangram()
    time.sleep(2)
    os.system("clear")

#main:
init_GPIO()
try:
    while True:
        is_pangram()
        list_tooMany.clear()
        list_missing.clear()
        alfabet_dictonary.clear()
except KeyboardInterrupt:
    os.system("clear")
    GPIO.output(green_1, GPIO.LOW)
    GPIO.output(green_2, GPIO.LOW)
    GPIO.output(red_1, GPIO.LOW)
    GPIO.output(red_2, GPIO.LOW)
