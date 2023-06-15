import os
import datetime
from pygame import mixer

mixer.init()

setHour = int(input("Enter hour your alarm should beep :"))
setMin = int(input("Enter min your alarm should beep :"))
setTimeSlot = input("am / pm : ")


if setTimeSlot == "pm" :
    setHour+=12

    while True :
        if setHour == datetime.datetime.now().hour and setMin == datetime.datetime.now().minute:
            print("sound will start playing now to wake you up....")
        
            mixer.music.load("audio.mp3")
            mixer.music.play()
            break
