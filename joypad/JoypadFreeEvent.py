#!/usr/bin/python
# -*- coding: latin-1 -*-
from evdev import InputDevice, categorize, ecodes
from time import sleep
from datetime import date
import os, sys, socket
import RPi.GPIO as GPIO

# configure servo
''' 2.5 - 7.15 - 11.8 '''
servo_pin = 12  # equivalent de GPIO 18
GPIO.setmode(GPIO.BOARD)  # notation board plutôt que BCM
GPIO.setup(servo_pin, GPIO.OUT)  # pin configuree en sortie
pwm = GPIO.PWM(servo_pin, 50)  # pwm à une fréquence de 50 Hz
rapport = 7       # rapport cyclique initial de 7%
pwm.start(rapport)

# Get Joypad
''' 0 - 133 - 255 '''
dev = InputDevice('/dev/input/event0')
# reprendre le meme identifiant "event"
for event in dev.read_loop(): # boucle qui surveille l'arrivee d'un evenement
    e_code=event.code
    e_type=event.type
    e_value=event.value
    if e_code == 2:
        # Stick 1 D<->G
        if e_value < 118 or e_value > 124:
            valPerc = (e_value / 255.)*1.
            print valPerc

