#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
class Roboter:
    def __init__(self, linker_port, rechter_port):
        self.linker_motor = Motor(linker_port)
        self.rechter_motor = Motor(rechter_port)
    
    def vorwaerts_start(self, speed):
        self.linker_motor.run(speed)
        self.rechter_motor.run(speed)
    def vorwaerts_stop(self):
        self.linker_motor.stop()
        self.rechter_motor.stop()
        
ultraschall = UltrasonicSensor(Port.S4)
mein_roboter = Roboter(Port.B, Port.C)

def vorwaerts(speed, time):
    mein_roboter.linker_motor.run(speed)
    mein_roboter.rechter_motor.run(speed)
    wait(time)
    mein_roboter.linker_motor.stop()
    mein_roboter.rechter_motor.stop()

def rueckwaerts(speed, time):
    mein_roboter.linker_motor.run(speed * -1)
    mein_roboter.rechter_motor.run(speed * -1)
    wait(time)
    mein_roboter.linker_motor.stop()
    mein_roboter.rechter_motor.stop()
    
def kurve_rechts():
    mein_roboter.linker_motor.run(350)
    mein_roboter.rechter_motor.run(-100)
    wait(900)
    mein_roboter.linker_motor.stop()
    mein_roboter.rechter_motor.stop()
    
def kurve_links():
    mein_roboter.linker_motor.run(-100)
    mein_roboter.rechter_motor.run(350)
    wait(900)
    mein_roboter.linker_motor.stop()
    mein_roboter.rechter_motor.stop()
    
def wenden(direction):
    if direction == True:
        mein_roboter.linker_motor.run(350)
        mein_roboter.rechter_motor.run(-100)
        wait(1200)
        mein_roboter.linker_motor.stop()
        mein_roboter.rechter_motor.stop()
    else:
        mein_roboter.linker_motor.run(-100)
        mein_roboter.rechter_motor.run(350)
        wait(900)
        mein_roboter.linker_motor.stop()
        mein_roboter.rechter_motor.stop()
        

# Write your program here.
while True:
    distanz = ultraschall.distance()
    if distanz < 300:
        mein_roboter.vorwaerts_stop()
        rueckwaerts(300, 1000)
        wenden(True)
    else:
        mein_roboter.vorwaerts_start(500)
