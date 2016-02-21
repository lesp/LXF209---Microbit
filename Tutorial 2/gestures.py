from microbit import *

while True:
    if accelerometer.was_gesture('up'):
        display.clear()
        display.scroll("Dogs cannot look up")
        sleep(100)
    elif accelerometer.was_gesture('down'):
        display.clear()
        display.scroll("I feel sick")
        sleep(100)
    elif accelerometer.was_gesture('left'):
        display.clear()
        display.scroll("Woah I'm going to fall over")
        sleep(100)
    elif accelerometer.was_gesture('right'):
        display.clear()
        display.scroll("I've been tilted right")
        sleep(100)
    elif accelerometer.was_gesture('shake'):
        display.clear()
        display.scroll("Stop shaking me!")
        sleep(100)