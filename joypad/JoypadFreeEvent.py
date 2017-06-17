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

def sendDevDict(devDict):
    print "send devDict :",devDict

# Get Joypad
''' 0 - 133 - 255 '''
dev = InputDevice('/dev/input/event0')
print "device :",dev

#device dict
devDict = {
    'stick1H':0,
    'stick1V':0,
    'stick2H':0,
    'stick2V':0,
    'crossUpDown':0,
    'crossLR':0,
    'btn1':0,
    'btn2':0,
    'btn3':0,
    'btn4':0,
    'btnSelect':0,
    'btnStart':0,
    'L1':0,
    'L2':0,
    'R1':0,
    'R2':0
}
# reprendre le meme identifiant "event"
for event in dev.read_loop(): # boucle qui surveille l'arrivee d'un evenement
    e_code=event.code
    e_type=event.type
    e_value=event.value
    mutePrint = False
    exclude = [2,4]
    filterAnalogic = [0,1,3,5]
    filterCross = [17,16]


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
        # Up -> -1    Down -> 1
        #print "Up/Down Cross :",e_value
        devDict['crossUpDown']=e_value

    # Cross Left/Right
    if e_code == 16:
        # L -> -1    R -> 1
        #print "Left/Right Cross :",e_value
        devDict['crossLR']=e_value

    # Btn 1
    if e_code == 288:
        #print "Btn 1 :",e_value
        devDict['btn1']=e_value

    # Btn 2
    if e_code == 289:
        #print "Btn 2 :",e_value
        devDict['btn2']=e_value

    # Btn 3
    if e_code == 290:
        #print "Btn 3 :",e_value
        devDict['btn3']=e_value

    # Btn 4
    if e_code == 291:
        #print "Btn 4 :",e_value
        devDict['btn4']=e_value

    # Btn Select
    if e_code == 296:
        #print "Btn Select :",e_value
        devDict['btnSelect']=e_value

    # Btn Select
    if e_code == 297:
        print "Btn Start :",e_value
        devDict['btnStart']=e_value

    # L1
    if e_code == 292:
        #print "L1 :",e_value
        devDict['L1']=e_value

    # L2
    if e_code == 294:
        #print "L2 :",e_value
        devDict['L2']=e_value

    # R1
    if e_code == 293:
        #print "R1 :",e_value
        devDict['R1']=e_value
    # R2
    if e_code == 295:
        #print "R2 :",e_value
        devDict['R2']=e_value

    # send devDict
    #if e_value != 0:
    if e_code not in exclude:
        print "e_code :",e_code
        if e_value != 0:
            if e_code in filterAnalogic:
                if e_value < 127.99 or e_value > 128.01:
                    print "debug1"
                    sendDevDict(devDict)
        elif e_code in filterCross:
            print "debug2"
            sendDevDict(devDict)
            if e_code == 17 :
                devDict['crossUpDown']=0
            if e_code == 16 :
                devDict['crossLR']=0
            sendDevDict(devDict)
        else:
            print "debug3"
            if mutePrint: print "e_code :",e_code
            if mutePrint: print "e_type :",e_code
            if mutePrint: print "e_value :",e_value
            sendDevDict(devDict)
