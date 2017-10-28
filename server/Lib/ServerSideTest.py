import valve as valve
import time


#Set funtions to detect and global vars based on if we hit the limit switches


print("starting lib test")
#In networked test
#-Generate settings object
#-wait until we recive settings
#-Grab settings from client and store
#-use these settings instead of hardcoded ones to test


stepper = valve.SetupStepper(0)
valve.storeSettings(stepper,)
valve.SetRescale(stepper,0.1125)
print("Opening valve")
valve.SetStart(stepper)
startTime = time.time()
#open stepper to 90 degrees with 20 degree slowopen and 10 percent b
valve.OpenValve(stepper, 100, 20, 200, 90, 5,10)
print("Simulating burn time of 4 seconds")
while (open_detected==0):
    valve.degOpen(stepper,200,20)

time.sleep(4)
print("Closing valve")
valve.closeValve(stepper,100,5,10)
while (closed_detected==0) :
    valve.degClose(stepper,100,10)

valve.UnlockValve(stepper)
if (open_detected):
    print("we hit open switch during this run")
if (closed_detected) :
    print("we hit close switch during this run")
exit(0)
