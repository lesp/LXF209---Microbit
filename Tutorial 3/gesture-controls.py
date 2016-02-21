from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        print("shake")
        display.clear()
        display.scroll("Teleport")
        sleep(100)
        accelerometer.reset_gestures()
        sleep(100)