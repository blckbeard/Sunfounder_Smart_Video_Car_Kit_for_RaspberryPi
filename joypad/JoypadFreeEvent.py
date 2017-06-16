#!/usr/bin/python
# -*- coding: latin-1 -*-
from evdev import InputDevice, categorize, ecodes
from select import select

from time import sleep
from datetime import date
import os, sys, socket
import RPi.GPIO as GPIO

#def
def analogicStick(e_code,e_type,e_value,mid,mutePrint=False):
    if e_value < mid or e_value > mid:
        valPerc = (e_value - 128)/128. #(e_value / 255.)*1.
    else:
        e_value = mid
        valPerc = 0 #(mid / 255.)*1.
    if mutePrint: print "e :",e_code
    if mutePrint: print "val :",e_value
    if mutePrint: print "valPerc :",valPerc
    return valPerc

# Get Joypad
''' 0 - 133 - 255 '''
dev = InputDevice('/dev/input/event0')
print "device :",dev

#device dict
devDict = {
    "stick1H":0,
    "stick1V":0,
    "stick2H":0,
    "stick2V":0,
    "crossU":0,
    "crossD":0,
}
# reprendre le meme identifiant "event"
for event in dev.read_loop(): # boucle qui surveille l'arrivee d'un evenement
    e_code=event.code
    e_type=event.type
    e_value=event.value
    mutePrint = False
    exclude = [0,1,3,5]

    
    if e_value != 0:
        if e_code in exclude:
            if e_value < 127.99 or e_value > 128.01:
                if mutePrint: print "e_code :",e_code
                if mutePrint: print "e_type :",e_code
                if mutePrint: print "e_value :",e_value
                print "devDict :",devDict
        else:
            if mutePrint: print "e_code :",e_code
            if mutePrint: print "e_type :",e_code
            if mutePrint: print "e_value :",e_value
            print "devDict :",devDict
    # Stick 1 R<->L Analogique 
    if e_code == 0:
        if e_value != 0 :
            devDict['stick1H'] = analogicStick(e_code,e_type,e_value,128,mutePrint=mutePrint)
    # Stick 1 H<->B Analogique
    if e_code == 1 :
        devDict['stick1V'] = analogicStick(e_code,e_type,e_value,128,mutePrint=mutePrint)

    # Stick 2 G<->D Analogique
    if e_code == 3:
        devDict['stick2H'] = analogicStick(e_code,e_type,e_value,128,mutePrint=mutePrint)

    # Stick 2 H<->B Analogique
    if e_code == 5:
        devDict['stick2V'] = analogicStick(e_code,e_type,e_value,128,mutePrint=mutePrint)

    # Cross Up/Down
    if e_code == 17:
        if e_value == -1:
            print "Up Cross"
        if e_value == 1:
            print "Down Cross"

    # Cross Left/Right
    if e_code == 16:
        if e_value == -1:
            print "Left Cross"
        if e_value == 1:
            print "Right Cross"

    # Btn 1
    if e_code == 288:
        if e_value == 0:
            print "Btn 1 release"
        if e_value == 1:
            print "Btn 1 pressed"

    # Btn 2
    if e_code == 289:
        if e_value == 0:
            print "Btn 2 release"
        if e_value == 1:
            print "Btn 2 pressed"

    # Btn 3
    if e_code == 290:
        if e_value == 0:
            print "Btn 3 release"
        if e_value == 1:
            print "Btn 3 pressed"

    # Btn 3
    if e_code == 291:
        if e_value == 0:
            print "Btn 4 release"
        if e_value == 1:
            print "Btn 4 pressed"

    # Btn Select
    if e_code == 296:
        if e_value == 0:
            print "Btn Select release"
        if e_value == 1:
            print "Btn Select pressed"

    # Btn Select
    if e_code == 297:
        if e_value == 0:
            print "Btn Start release"
        if e_value == 1:
            print "Btn Start pressed"

    # L1
    if e_code == 292:
        print "L1 :",e_value

    # L2
    if e_code == 294:
        print "L2 :",e_value

    # R1
    if e_code == 293:
        print "R1 :",e_value

    # R2
    if e_code == 295:
        print "R2 :",e_value

    

