import valvecontrol as valve
import time
import sys
import  RPi.GPIO as GPIO


#Set funtions to detect and global vars based on if we hit the limit switches


print("starting lib test")
#In networked test
#-Generate settings object
#-wait until we recive settings
#-Grab settings from client and store
#-use these settings instead of hardcoded ones to test


stepper = valve.SetupStepper(0)
valve.storeSettings(stepper, 200, 100, 40, 90, 5, 50, 26,21)
valve.SetRescale()
print("Opening valve")
try:
    valve.SetStart(stepper)
except Exception as e:
    print("--------------")
    print(" Err -"+str(e))
startTime = time.time()
#open stepper to 90 degrees with 20 degree slowopen and 10 percent b
#valve.OpenValve()
valve.hasOpened = 1
valve.close_detected = 0;
valve.open_detected = 0;
print("Simulating burn time of 4 seconds")
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)
while (GPIO.input(26) == 1):
    valve.degOpen(10)

time.sleep(4)
print("Closing valve")
#valve.closeValve()
while (GPIO.input(21) == 1) :
    valve.degClose(10)

valve.UnlockValve()
valve.shutdown()
if (valve.open_detected):
    print("we hit open switch during this run")
if (valve.closed_detected) :
    print("we hit close switch during this run")
time.sleep(10)

sys.exit(0)

