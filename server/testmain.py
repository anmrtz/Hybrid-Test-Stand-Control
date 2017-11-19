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
		print("\n\nEnding test: " + str(msg))

def testEnded():
	global END_TEST
	return END_TEST

from lib.valvecontrol import *

class TestMain:
	def __init__(self):	
		self.valveControl = None
		self.client = None
		
		self.motorBusy = False
		self.busyLock = threading.Lock()

	def initServer(self):

		# get eth0 IP in Linux
		try:
			f = os.popen('ip addr show eth0')
			host = f.read().split("inet ")[1].split("/")[0]
			f.close()
		except Exception as e:
			endTest(e)
			return

		self.sock = socket.socket()
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
			# the recieved message is stored in data
		except Exception as e:
			endTest(e)
			return	
		except KeyboardInterrupt:
			endTest("Keyboard interrupt")
			return	


		signal.signal(signal.SIGINT, self.handleKeyboardInt)

		if self.valveControl is None:
			self.valveControl = ValveControl()
			self.valveControl.initStepper()
			self.valveControl.initEncoder()

		# spawn a new thread to periodically check the connection with the new client
		checkConnectThread = threading.Thread(target = self.checkConnection, args = ())
		checkConnectThread.daemon = False 	
		checkConnectThread.start()

		recvClientMsgThread = threading.Thread(target = self.recvClientMsg, args = ())
		recvClientMsgThread.daemon = False 	
		recvClientMsgThread.start()
					
		# keep main thread alive
		while not END_TEST:
			time.sleep(0.1)
		print("Main thread ended!")

	# periodically check for broken ethernet connection
	def checkConnection(self):
		while not END_TEST:
			#print("Checking connection...")
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
				break

			# piggy-backing limit switch status messages on this thread
			if self.valveControl is not None:
				limit_switch_msg = "LIMIT " + str(int(self.valveControl.openLimitHit())) + " " + str(int(self.valveControl.closeLimitHit()))
				self.client.sendall(limit_switch_msg.encode())
				
				encoder_position_msg = "ENCODER " + str(int(self.valveControl.motorPos))
				self.client.sendall(encoder_position_msg.encode())
				
				ignitor_state_msg = "IGNITOR 0"
				self.client.sendall(ignitor_state_msg.encode())
			time.sleep(0.1)
		print("checkConnection thread ended!")
		
	def recvClientMsg(self):
		# slice msg string for token + parameters
		while not END_TEST:
			try:
				data = self.client.recv(1024)	
			except Exception as e:
				endTest(e)
				break

			data = data.decode('utf-8')
			if (data == ''):
				endTest("recvClientMsg: Connection broken")
				break
			
			params = data.split(' ')
			token = params[0]
		
			if params[0] == "HEAD" and len(params) < 2:
				self.sendMsgToClient("Starting automated test")
#				self.startAutoTest(params[1:])
			elif params[0] == "VALVE" and len(params) == 2 and params[1] == "OPEN":
				self.sendMsgToClient("Manually opening valve")
				self.fullValveArc(True)
			elif params[0] == "VALVE" and len(params) == 2 and params[1] == "CLOSE":
				self.sendMsgToClient("Manually closing valve")
				self.fullValveArc(False)
			elif params[0] == "IGNITE":
				self.sendMsgToClient("Firing ignitor")			
			elif params[0] == "ABORT":
				self.sendMsgToClient("Abort received!")			
				endTest("Client abort signal received!")
				# force close the valve
				self.valveControl.closeValve()
			else:
				self.sendMsgToClient("Invalid instruction received!")			
				endTest("recvClientMsg invalid instruction: " + data)		
		print("recvClientMsg thread ended!")
		
	def _isMotorAvailable(self):
		with self.busyLock:
			if self.motorBusy:
				return False
			else:
				self.motorBusy = True
				return True

	def fullValveArc(self, setToOpen):
		if self._isMotorAvailable():
			if setToOpen:
				self.valveControl.openValve()
			else:
				self.valveControl.closeValve()			
			self.motorBusy = False
		else:
			sendMsgToClient("MOTOR BUSY!")

	# use this function to start the motor-controller test sequence - either directly or after parsing the initial client message
	def autoTest(self, params):
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
			
		if self._isMotorAvailable():
			sendMsgToClient("Running auto test")
			# run motor code here
			self.motorBusy = False
		else:
			sendMsgToClient("MOTOR BUSY!")
		
	def sendMsgToClient(self,msg):
		if self.client is not None:
			self.client.sendall(msg.encode())
		print("To client: " + msg)

	# handle Ctrl-C
	def handleKeyboardInt(self, signal, frame):
		endTest("Keyboard interrupt")
		
	def __del__(self):
		if self.client is not None:
			self.client.close()
		if self.sock is not None:
			self.sock.close()
			
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

