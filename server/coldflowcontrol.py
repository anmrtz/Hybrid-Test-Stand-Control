from lib.valvecontrol import *
from lib.StatusCommunication import *

#For ending the test normally
END_TEST = False

#Ending the test on ABORT signal
ABORT_TEST = False

#Value of time valve starts turning
START_TIME

#If time exceded, call to return
TIME_RETURN = False

class ColdFlowControl:
    def __init__(self):
        pass
    def startColdFlow(self):
        server = ControlServer()

        #grab settings and start the server going
        settings = server.startServer()
        #Setup stepper
        stepper = valvecontrol.SetupStepper(0)
        #Pass recived settings to the stepper controller
        stepper.loadSettings(settings)

        server.sendMessage(self, "Settings Loaded")

        #verify launch code here

        Server.sendMessage(self, "Launch Code accepted ")

        #wait for open valve message
        Server.waitForOpen(self)

        #start thread to check for abort
        abortThread = threading.Thread(target = Server.checkAbort,args=())
        abortThread.daemon = False

        #start Timer for checking open
        global startTime
        startTime = time.time()
        timerThread = threading.Thread(target = self.compTime, args(self,startTime))
        timerThread.daemon = False

        #insert normal run here, checking for if we close early

        #Keep this alive till we close the server
        while not server.END_TEST:
        	time.sleep(0.2)
        print("Main thread ended")

    def compTime(self):
        #check time
        time.sleep(1)
        currTime = time.time()
        if currTime-START_TIME >= stepper.burn_duration:
            TIME_RETURN = True

    
