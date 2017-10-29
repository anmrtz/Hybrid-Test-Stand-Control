from valvecontrol import *
import time
import sys


#Set funtions to detect and global vars based on if we hit the limit switches


print("starting lib test")
#In networked test
#-Generate settings object
#-wait until we recive settings
#-Grab settings from client and store
#-use these settings instead of hardcoded ones to test


valve = ValveControl(21,26)


valve.initStepper()

print("Opening valve")
valve.openValve()

print("Waiting 4 seconds")
time.sleep(4)

print("Closing valve")
valve.closeValve()

print("Test ended")


