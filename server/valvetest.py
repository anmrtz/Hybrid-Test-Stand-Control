from lib.valvecontrol import *
import time
import sys


print("Starting valve test")

valve = ValveControl()

valve.initStepper()

while True:
    #print("Opening valve")
    time.sleep(0.1)

    valve.openValve()

    #print("Waiting 2 seconds")
    time.sleep(0.1)

    #print("Closing valve")
    valve.closeValve()

print("Test ended")

