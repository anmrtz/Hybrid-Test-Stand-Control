import valvecontrol
import time

print("starting lib test")
#In networked test
#-Generate settings object
#-wait until we recive settings
#-Grab settings from client and store
#-use these settings instead of hardcoded ones to test

stepper = valvecontrol.SetupStepper(0)
valvecontrol.SetRescale(stepper,0.1125)
print("Opening valve")
valvecontrol.SetStart(stepper)
#open stepper to 90 degrees with 20 degree slowopen and 10 percent b
valvecontrol.OpenValve(stepper, 100, 20, 200, 90, 5,10)
print("Simulating burn time of 4 seconds")
time.sleep(4)
print("Closing valve")
valvecontrol.closeValve(stepper,100,5,10)
valvecontrol.UnlockValve(stepper)
exit(0)