import threading
import socket
import sys
import time
import os
import signal

# global abort/end-of-test flag
# consider placing this in TestMain...
END_TEST = False
end_test_lock = threading.Lock()		
def endTest(msg = "NO_ABORT_MSG"):
	with end_test_lock:
		global END_TEST 
		if END_TEST:
			return
		END_TEST = True
		print("Ending test: " + str(msg))

class TestMain:
	def __init__(self):	
		signal.signal(signal.SIGINT, self.handleKeyboardInt)

	def initServer(self):
		self.sock = socket.socket()
		
		# get eth0 IP in Linux
		try:
			f = os.popen('ip addr show eth0')
        	        host = f.read().split("inet ")[1].split("/")[0]
                	f.close()
		except Exception as e:
			endTest(e)
			return

		print('eth0 IP: ' + host)
		port = 9999
		address = (host,port)
		print('Starting Server on %s' % sys.version)
		self.sock.bind(address)
		self.sock.listen(5)

		print("Waiting for client connection...")
		
		# wait for a new connection
		try:
			self.client, addr = self.sock.accept()	
		except Exception as e:
			endTest(e)
			return
			
		# the recieved message is stored in data
		data = self.client.recv(1024)
		print("Recieved: " + data)

		# spawn a new thread to periodically check the connection with the new client
		thr = threading.Thread(target = self.checkConnection, args = ())
		
		thr.daemon = False 	
		thr.start()

		# slice param string as needed and start test

	# periodically check for broken ethernet connection
	def checkConnection(self):
		while not END_TEST:
			time.sleep(0.5)
			print("Checking connection...")
			try:
				# get eth0 status
				f = os.popen('cat /sys/class/net/eth0/carrier')
				eth0_active = int(f.read())
				f.close()			
			except Exception as e:
				endTest(e)
				break

			if not eth0_active:
				endTest("Ethernet connection broken")
		self.client.close()
			
	# use this function to start the motor-controller test sequence - either directly or after parsing the initial client message
	def startTest(self,	params):
		if len(params) != 10:
			endTest('Need 10 input parameters')
			return
		try:
			launch_code = int(params[0])
			burn_duration = float(params[1]) 
			ignitor_timing = float(params[2])
			valve_open_timing = float(params[3])
			valve_closing_time = float(params[4])
			limit_switch_slowdown_speed = float(params[5])
			angle_limit_switch_slowdown_mode = float(params[6])
			opening_profile_angle_delimiter = float(params[7])
			total_opening_time = float(params[8])
			initial_opening_time = float(params[9])
		except Exception as e:
			endTest(e)
			return

		print("Starting test...")
		#verify launch code		
		#verify input type/ranges then start the test

		#successful end of test
		endTest("End of TestMain")

	# handle Ctrl-C
	def handleKeyboardInt(self, signal, frame):
		endTest("Keyboard interrupt")

# start test directly from command line
def terminalStart():
	print("Starting terminal test...")
	test = TestMain()
	test.startTest(sys.argv[1:])
	
# start test server and wait for connection
def serverStart():
	print("Starting test server...")
	test = TestMain()
	test.initServer()

if len(sys.argv) > 1:
	terminalStart()
else:
	serverStart()

# keep main thread alive until end of test
while not END_TEST:
	time.sleep(1)
print("Main thread ended")
