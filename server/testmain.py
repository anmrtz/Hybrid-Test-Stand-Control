import threading
import socket
import sys
import time
import os
import signal
import queue

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
		self.sock = None

		self.instructionQueue = queue.Queue()

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
		checkStatusThread = threading.Thread(target = self.checkStatus, args = ())
		checkStatusThread.daemon = False
		checkStatusThread.start()

		recvClientMsgThread = threading.Thread(target = self.recvClientMsg, args = ())
		recvClientMsgThread.daemon = False 	
		recvClientMsgThread.start()

		while not testEnded():
			try:
				instruction = self.instructionQueue.get(True, 1)				
				self.processInstruction(instruction)
			except queue.Empty:
				pass
				
		print("Main waiting for threads to clear...")
				
		self.clearInstructionQueue();

		# wait for all dispatched threads to terminate gracefully...
		checkStatusThread.join()
		recvClientMsgThread.join()

		self.client.close()
		self.client = None

		self.valveControl = None

		print("Main thread ended!")

	def processInstruction(self, instruction):

		params = instruction.split(' ')

		if params[0] == "HEAD" and len(params) > 1:
			self.sendMsgToClient("Initializing automated test...")
			self.startAutoTest(params[1:])
		elif params[0] == "VALVE" and len(params) == 2 and params[1] == "OPEN":
			self.sendMsgToClient("Manually opening valve to limit switch...")
			self.valveControl.moveValveToOpenLimit()
		elif params[0] == "VALVE" and len(params) == 2 and params[1] == "CLOSE":
			self.sendMsgToClient("Manually closing valve to limit switch...")
			self.valveControl.moveValveToCloseLimit()
		elif params[0] == "IGNITE":
			self.sendMsgToClient("Toggling ignitor...")
			self.valveControl.setIgnitor(not self.valveControl.ignitorActive())
		elif params[0] == "CALIBRATE_ENCODER":
			pass
		elif params[0] == "ABORT":
			self.sendMsgToClient("Abort received!")
			endTest("Client abort signal received!")
			# force close the valve
			self.valveControl.moveValveToCloseLimit()
		else:
			self.sendMsgToClient("Invalid instruction received!")
			endTest("Invalid instruction: " + data)

	def clearInstructionQueue(self):
		while not self.instructionQueue.empty():
			self.instructionQue.get(False)

	def checkStatus(self):
		while not testEnded():
			# periodically check for broken ethernet connection
			try:
				f = os.popen('cat /sys/class/net/eth0/carrier')
				eth0_active = int(f.read())
				f.close()			
			except Exception as e:
				endTest(e)
				break

			if not eth0_active:
				endTest("Ethernet connection broken")
				break

			# send status information back to client
			if self.valveControl is not None:
				#limit_switch_msg = "LIMIT " + str(int(self.valveControl.openLimitHit())) + " " + str(int(self.valveControl.closeLimitHit()))
				#self.sendMsgToClient(limit_switch_msg)
				#encoder_position_msg = "ENCODER " + str(int(self.valveControl.motorPos))
				#self.sendMsgToClient(encoder_position_msg)
				#ignitor_state_msg = "IGNITOR 0"
				#self.sendMsgToClient(ignitor_state_msg)
				
				state_msg = "STATEALL " + str(int(self.valveControl.openLimitHit())) + " " + str(int(self.valveControl.closeLimitHit())) + " " + \
					str(int(self.valveControl.encoder.getPosition())) + " " + str(int(self.valveControl.ignitorActive()))
					
				self.sendMsgToClient(state_msg)
			time.sleep(0.1)
		print("checkConnection thread ended!")
		
	def recvClientMsg(self):
		while not testEnded():
			try:
				data = self.client.recv(1024)	
			except Exception as e:
				endTest(e)
				break

			data = data.decode('utf-8')
			if (data == ''):
				endTest("recvClientMsg: Connection broken")
				break
			elif not testEnded():
				self.instructionQueue.put(data)

		print("recvClientMsg thread ended!")

	# use this function to start the motor-controller test sequence
	def startAutoTest(self, params):
		print("Auto test parameters recieved: " + str(params))
		if len(params) != 10:
			endTest("Need 10 input parameters for auto test")
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
			self.sendMsgToClient("ERROR! Cannot start auto test: " + str(e))
			return
		
		self.valveControl.moveValveToCloseLimit()
		self.valveControl.calibratePosition()
		self.sendMsgToClient("Moving to buffer angle")
		self.valveControl.moveToAngle(60,200)
		self.sendMsgToClient("Moving slowly to open position")
		self.valveControl.moveToAngle(90,100)
		self.valveControl.setIgnitor(True)
		self.sendMsgToClient("Burning for " + str(burn_duration) + " seconds")
		time.sleep(burn_duration)
		self.valveControl.setIgnitor(False)
		self.sendMsgToClient("Closing valve")
		self.valveControl.moveValveToCloseLimit()
		
		self.sendMsgToClient("Auto test ended")

	def sendMsgToClient(self,msg):
		if self.client is not None:
			try:
				self.client.sendall(msg.encode())
			except Exception as e:
				endTest(e)

	# handle Ctrl-C
	def handleKeyboardInt(self, signal, frame):
		endTest("Keyboard interrupt")
		self.client.shutdown(socket.SHUT_WR)

	def __del__(self):
		if self.client is not None:
			try:
				self.client.close()
			except Exception as e:
				print("Failed to close client: " + str(e))
		if self.sock is not None:
			try:
				self.sock.close()
			except Exception as e:
				print("Failed to close server: " + str(e))

# start test directly from command line
#def terminalStart():
#	print("Starting terminal test...")
#	test = TestMain()
#	test.startTest(sys.argv[1:])

# start test server and wait for connection
def main():
	print("Starting test server...")
	test = TestMain()
	test.initServer()
	print("testmain ended")

if __name__ == '__main__':
	main()
