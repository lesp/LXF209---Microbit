import serial, time
from mcpi.minecraft import Minecraft
from random import randint
port = "/dev/ttyACM0"
baud = 115200
mc = Minecraft.create()

while True:
    s = serial.Serial(port)
    s.baudrate = baud
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    data = s.readline()
    time.sleep(0.1)
    data = str(data)
    x,y,z = mc.player.getPos()
    if "shake" in data:
        mc.postToChat("Teleport")
        mc.player.setTilePos(x+(randint(-50,50)),y+(randint(1,50)),z)
