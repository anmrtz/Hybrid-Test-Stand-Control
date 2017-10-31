import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def open_callback(channel):
    print ("open detected by thread")
    print ("Pause for burn")
    time.sleep(4)
    print("Now we would call close func")

def close_callback(channel):
    print ("closed detected by thread")
    print("Just stop the motor!")
           
GPIO.add_event_detect(21,GPIO.FALLING, callback=close_callback,bouncetime=300)
GPIO.add_event_detect(26,GPIO.FALLING, callback=open_callback,bouncetime=300)
try :
    
    while(True):
        print(".")
        time.sleep(1)
#raw_input("Press enter when ready\n>")

except KeyboardInterrupt:
    GPIO.cleanup()
