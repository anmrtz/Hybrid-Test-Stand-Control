import valvecontrol
import time
import  RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)

open_detected=0
closed_detected=0

#Set funtions to detect and global vars based on if we hit the limit switches
def open_callback(channel):
    global open_detected
    print ("open detected by thread")
    print ("Pause for burn")
    print("Now we would call close func")
    open_detected=1

def close_callback(channel):
    global closed_detected
    print ("closed detected by thread")
    print("Just stop the motor!")
    closed_detected=1

print("starting lib test")
#In networked test
#-Generate settings object
#-wait until we recive settings
#-Grab settings from client and store
#-use these settings instead of hardcoded ones to test

GPIO.add_event_detect(21,GPIO.FALLING, callback=close_callback,bouncetime=300)
GPIO.add_event_detect(26,GPIO.FALLING, callback=open_callback,bouncetime=300)

stepper = valvecontrol.SetupStepper(0)
valvecontrol.SetRescale(stepper,0.1125)
print("Opening valve")
valvecontrol.SetStart(stepper)
startTime = time.time()
#open stepper to 90 degrees with 20 degree slowopen and 10 percent b
valvecontrol.OpenValve(stepper, 100, 20, 200, 90, 5,10)
print("Simulating burn time of 4 seconds")
while(!open_detected) degOpen(stepper,200,20)
time.sleep(4)
print("Closing valve")
valvecontrol.closeValve(stepper,100,5,10)
while(!closed_detected) degClose(stepper,100,10)
valvecontrol.UnlockValve(stepper)
if (open_detected):
    print("we hit open switch during this run")
if (closed_detected) :
    print("we hit close switch during this run")
exit(0)
