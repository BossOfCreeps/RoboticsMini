#!/usr/bin/env python

from pyxl320 import ServoSerial
from pyxl320 import Packet
from time import sleep
from pyxl320 import xl320

angles = {
    #            1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16
	"stand":  [150, 150,  70, 230, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
	"right":  [300, 150,  70, 230, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
	"left":   [150,   0,  70, 230, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
	"tilt":   [100, 200,  70, 230, 150, 150, 150, 150, 120, 180, 150, 150, 150, 150, 150, 150],
	"sit":    [150, 150,  70, 230, 150, 150, 150, 150, 120, 180, 180, 120, 160, 140, 150, 150],
}

serial = None
last_pose = "stand"

def init(port):
	global serial
	serial = ServoSerial(port)
	serial.open()
	set_pose("stand")
	
def set_pose(pose):
	f = (13,14,1,2,3,4,5,6,7,8,9,10,11,12,15,16)
	speed = 1/15

	if pose=="stand":
		f = (1,2,3,4,5,6,7,8,13,14,15,16,9,10,11,12)[::-1]
		speed = 1/30
	
	serial.sendPkt(Packet.makeServoSpeedPacket(xl320.XL320_BROADCAST_ADDR, speed))

	for l in f:
		serial.sendPkt(Packet.makeServoPacket(l,angles[pose][l-1]))

def end():
	global serial
	serial.close()

def podbor(a, b):
	i = a-1
	while i<b:
		i+=1
		print("Motor: ", i)
		a = 150
		while a < 500:
			serial.sendPkt(Packet.makeServoPacket(i, a))
			a = int(input("Getting angle:"))

def fun_with_pose():
	while True:
		pose = input("pose: ")
		if pose == "end":
			break 
		set_pose(pose)

if __main__ = "__main__":
	init("COM8")
	end()
