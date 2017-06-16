#!/usr/bin/python
# -*- coding: latin-1 -*-
from evdev import InputDevice, categorize, ecodes
from select import select

from time import sleep
from datetime import date
import os, sys, socket
import RPi.GPIO as GPIO

#def
def getAllValue(dev):
    # The select() call will block until there are events on dev_obj.
    #r, w, x = select([dev], [], [])
    foo = []
    try:
        for event in dev.read():
            print event
            foo.append(event)
        return foo
    except IOError:
        pass
    

# Get Joypad
''' 0 - 133 - 255 '''
dev = InputDevice('/dev/input/event0')
print "device :",dev
# reprendre le meme identifiant "event"
for event in dev.read_loop(): # boucle qui surveille l'arrivee d'un evenement
    e_code=event.code
    e_type=event.type
    e_value=event.value
    mutePrint = False
    exclude = [0]
    if mutePrint :
        if e_code not in exclude:
            if e_value < 115 or e_value > 125:
                print "e_code : ",e_code
                print "e_type : ",e_code
                print "e_value : ",e_value
                #print(categorize(event))
    # Stick 1 G<->D Analogique
    if e_code == 0:
        if e_value != 0 :
            if e_value < 115 or e_value > 125:
                valPerc = (e_value / 255.)*1.
                print "Stick 1 G<->D : ",valPerc

    # Stick 1 H<->B Analogique
    if e_code == 1 :
        #print "Stick 1 H<->B e_value : ",e_value
        # range : 21 - 210
        if e_value < 115 or e_value > 125:
            valPerc = (e_value / 255.)*1.
            print "Stick 1 H<->B : ",valPerc

    # Stick 2 H<->B Analogique
    if e_code == 5:
        if e_value < 115 or e_value > 125:
            valPerc = (e_value / 255.)*1.
            print "Stick 2 H<->B : ",valPerc

    # Stick 2 G<->D Analogique
    if e_code == 3:
        if e_value < 115 or e_value > 125:
            valPerc = (e_value / 255.)*1.
            print "Stick 2 G<->D : ",valPerc

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
            gen = getAllValue(dev)
            print gen
            for i in gen:
                print("i",i)
        if e_value == 1:
            print "Btn Start pressed"

    # L1
    if e_code == 292:
        print "L1 : ",e_value

    # L2
    if e_code == 294:
        print "L2 : ",e_value

    # R1
    if e_code == 293:
        print "R1 : ",e_value

    # R2
    if e_code == 295:
        print "R2 : ",e_value


