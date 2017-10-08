import threading
import socket
import sys
import time
import os

# global abort flag
ABORT_TEST = False
abort_lock = threading.Lock()		
def setAbort(msg = "NO_ABORT_MSG"):
	with abort_lock:
		global ABORT_TEST 
		if ABORT_TEST:
			return
		ABORT_TEST = True
		print("Aborting test: " + msg)

class ServerMain:
	def __init__(self):	
		pass

	def initServer(self):
		self.sock = socket.socket()
		
		# eth0 IP
		f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
		host = f.read().strip()
		f.close()

		print('eth0 IP: ' + host)
		port = 9999
		address = (host,port)
		print('Starting Server on %s' % sys.version)
		self.sock.bind(address)
		self.sock.listen(5)

		print("Waiting for client connection...")
		
		# wait for a new connection
		self.client, addr = self.sock.accept()	
			
		# the recieved message is stored in data
		data = self.client.recv(1024)
		print("Recieved: " + data)

		# spawn a new thread to periodically check the connection with the new client
		thr = threading.Thread(target = self.checkConnection, args = ())
		
		thr.daemon = False 	
		thr.start()

		# slice param string as needed and start test

	def checkConnection(self):
		while not ABORT_TEST:
			time.sleep(1)
			print("Checking connection...")
			try:
				self.client.send("Test")
			except Exception as e:
				setAbort("Ethernet connection broken: " + str(e))
		self.client.close()
			
	# use this function to start the motor-controller test sequence - either directly or after parsing the initial client message
	def startTest(self,	params):
		if len(params) != 10:
			setAbort('Need 10 test input parameters')
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
		except ValueError:
			setAbort('ValueError. Check that parameters are valid numbers')
			return
		#verify launch code		
		#verify input type/ranges then start the test
		print("Starting test...")

# start test directly from command line
def terminalStart():
	test = ServerMain()
	test.startTest(sys.argv[1:])
	
# start test server and wait for connection
def serverStart():
	test = ServerMain()
	test.initServer()

#serverStart()
#while not ABORT_TEST:
#	time.sleep(1)
#	print("Looping main...")
#print("Main terminated")
