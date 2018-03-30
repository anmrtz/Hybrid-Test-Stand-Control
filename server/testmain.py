import threading
import socket
import sys
import time
import os
import signal
import queue
import re

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
		self.charStream = ''

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

		# spawn a new thread to periodically check the connection with the new client
		checkStatusThread = threading.Thread(target = self.checkStatus, args = ())
		checkStatusThread.daemon = False
		checkStatusThread.start()

		self.client.settimeout(1)

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

		print("Closing client connection...")
		self.client.close()
		self.client = None

		self.valveControl = None

		print("Main thread ended!")

	def processInstruction(self, instruction):

		params = instruction.split()

		if params[0] == "AUTO_TEST_PARAMS" and len(params) > 1:
			self.sendMsgToClient("Initializing automated test...")
			self.startAutoTest(params[1:])
		elif params[0] == "MEV_OPEN":
			self.sendMsgToClient("Manually opening MEV to limit switch...")
			self.valveControl.moveMEVToOpenLimit()
		elif params[0] == "MEV_CLOSE":
			self.sendMsgToClient("Manually closing MEV to limit switch...")
			self.valveControl.moveMEVToCloseLimit()
		elif params[0] == "VENT_OPEN":
			self.sendMsgToClient("Manually opening vent valve to limit switch...")
			self.valveControl.moveVentToOpenLimit()
		elif params[0] == "VENT_CLOSE":
			self.sendMsgToClient("Manually closing vent valve to limit switch...")
			self.valveControl.moveVentToCloseLimit()
		elif params[0] == "IGNITOR":
			self.sendMsgToClient("Toggling ignitor...")
			self.valveControl.setIgnitor(not self.valveControl.ignitorActive())
		elif params[0] == "NC_VALVE":
			self.sendMsgToClient("Toggling NC valve...")
			self.valveControl.setNCValve(not self.valveControl.NCValveActive())
		elif params[0] == "DEFAULT_VEL" and len(params) == 2:
			try:
				new_default_vel = int(params[1])
			except:
				self.sendMsgToClient("Set default velocity error: invalid integer parameter")
				return
			self.sendMsgToClient("Setting default velocity to " + params[1] + " deg/s...")
			set_result = self.valveControl.setMEVDefaultVelocity(new_default_vel)
			self.sendMsgToClient(set_result)
		elif params[0] == "CALIBRATE_ENCODER":
			self.sendMsgToClient("Calibrating encoder...")	
		elif params[0] == "ABORT":
			self.sendMsgToClient("Abort received!")
			endTest("Client abort signal received!")
			# force close the valve
			#self.valveControl.moveValveToCloseLimit()
		else:
			self.sendMsgToClient("Invalid instruction received!")
			endTest("Invalid instruction: " + instruction + '|')

	def clearInstructionQueue(self):
		print("Clearing instruction queue...")
		while not self.instructionQueue.empty():
			self.instructionQueue.get(False)

	def checkStatus(self):
		while not testEnded():
			# periodically check for broken ethernet connection
			try:
				f = os.popen('cat /sys/class/net/eth0/carrier')
				eth0_active = int(f.read())
				#print("Eth0: " + str(eth0_active))
				f.close()			
			except socket.timeout as e:
				continue
			except Exception as e:
				endTest(e)
				break

			if eth0_active == 0:
				endTest("Ethernet connection broken")
				break

			# send status information back to client
			if self.valveControl is not None:			
				try:
					state_msg = "STATEALL " + \
						str(int(self.valveControl.MEVOpenLimitHit())) + " " + \
						str(int(self.valveControl.MEVCloseLimitHit())) + " " + \
						str(int(self.valveControl.VentOpenLimitHit())) + " " + \
						str(int(self.valveControl.VentCloseLimitHit())) + " " + \
						str(int(self.valveControl.encoder.getPosition())) + " " + \
						str(int(self.valveControl.ignitorActive())) + " " + \
						str(float(self.valveControl.MEVStepper.defaultVelocity)) + " " + \
						str(float(self.valveControl.MEVStepper.stepper.getVelocity())) + " " + \
						str(int(self.valveControl.NCValveActive())) + " " + \
						str(int(self.valveControl.lockoutArmed()))
				except Exception as e:
					print("Status send error: " + str(e))
				else:
					self.sendMsgToClient(state_msg)
			time.sleep(0.02)
		print("checkConnection thread ended!")
		
	def recvClientMsg(self):
		while not testEnded():
			try:
				data = self.client.recv(1024)	
			except socket.timeout as e:
				continue
			except Exception as e:
				endTest(e)
				break

			data = data.decode('utf-8')
			if (data == ''):
				endTest("recvClientMsg: Connection broken")
				break
			elif not testEnded():
				self.charStream += data
			
				while True:
					a = re.search(r'\b(END)\b', self.charStream)
					if a is None:
						break

					instruction = self.charStream[:a.start()]
					self.charStream = self.charStream[a.start()+3:]
			
					self.instructionQueue.put(instruction)

		print("recvClientMsg thread ended!")

	# use this function to start the motor-controller test sequence
	def startAutoTest(self, params):
		print("Auto test parameters recieved: " + str(params))
		if len(params) != 5:
			endTest("Need 5 input parameters for auto test")
			return
		try:
			launch_code = int(params[0])
			burn_duration = float(params[1]) 
			ignitor_delay = float(params[2])
			valve_opening_time = float(params[3])
			valve_closing_time = float(params[4])
		except Exception as e:
			self.sendMsgToClient("ERROR! Cannot start auto test: " + str(e))
			return
		
		self.valveControl.moveMEVValveToCloseLimit()
		self.valveControl.calibratePosition()
		
		try:
			open_velocity = 90.0 / valve_opening_time
			close_velocity = 90.0 / valve_closing_time
			if (open_velocity > self.valveControl.MEVStepper.maxVelocity or open_velocity <= 0.0):
				raise Exception('Specified valve open time results in out of range speed!')
			if (close_velocity > self.valveControl.MEVStepper.maxVelocity or close_velocity <= 0.0):
				raise Exception('Specified valve close time results in out of range speed!')
			if (burn_duration < 0.0):
				raise Exception('Invalid burn duration time!')
			if (ignitor_delay < 0.0):
				raise Exception('Invalid burn delay!')
		except Exception as e:
			self.sendMsgToClient("Auto test error:" + str(e))
			self.valveControl.moveMEVValveToCloseLimit()
			return

		#self.sendMsgToClient("Activating ignitor and waiting for " + str(ignitor_delay) + " seconds")
		#self.valveControl.setIgnitor(True)
		#time.sleep(ignitor_delay)
		#self.sendMsgToClient("Moving to open position")
		#self.valveControl.moveMEVToAngle(90,open_velocity)
		#self.sendMsgToClient("Burning for " + str(burn_duration) + " seconds")
		#time.sleep(burn_duration)
		#self.sendMsgToClient("Closing valve")
		#self.valveControl.moveValveToCloseLimit()
		#self.valveControl.moveMEVToAngle(0,close_velocity)
		#self.valveControl.setIgnitor(False)
		
		self.sendMsgToClient("Auto test ended")

	def sendMsgToClient(self,msg):
		msg += ' END\n'
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

# start test server and wait for connection
def main():
	print("Starting test server...")
	test = TestMain()
	test.initServer()
	print("testmain ended")

if __name__ == '__main__':
	main()
