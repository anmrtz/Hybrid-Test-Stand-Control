import valvecontrol as valve
import time


#Set funtions to detect and global vars based on if we hit the limit switches


print("starting lib test")
#In networked test
#-Generate settings object
#-wait until we recive settings
#-Grab settings from client and store
#-use these settings instead of hardcoded ones to test


stepper = valve.SetupStepper(0)
valve.storeSettings(stepper, 200, 100, 20, 90, 5, 10, 26,21)
valve.SetRescale()
print("Opening valve")
valve.SetStart(stepper)
startTime = time.time()
#open stepper to 90 degrees with 20 degree slowopen and 10 percent b
valve.OpenValve()
print("Simulating burn time of 4 seconds")
while (valve.open_detected==0):
    valve.degOpen()

time.sleep(4)
print("Closing valve")
valve.closeValve()
while (valve.closed_detected==0) :
    valve.degClose()

valve.UnlockValve(stepper)
if (valve.open_detected):
    print("we hit open switch during this run")
if (valve.closed_detected) :
    print("we hit close switch during this run")
exit(0)
