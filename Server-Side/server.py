import threading
import socket
import sys
import time

class ServerMain:
	def __init__(self):	
		#self.print_lock = threading.Lock()
		pass

	def initServer(self):
		self.sock = socket.socket()
		
		# get *ethernet* port IP in linux
		#f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
		#host = f.read()
		#f.close()
		
		host = socket.gethostname()
		print('eth0 IP:',host)
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
		print("Recieved: ", data)
	
		# spawn a new thread to periodically check the connection with the new client
		thr = threading.Thread(target = self.checkConnection, args = ())
		
		thr.daemon = False 	
		thr.start()

	def checkConnection(self):
		while True:
			time.sleep(1)
			print "Checking connection..."
			# check connection status here with a try-catch block around a send attempt
			# if send fails, then signal ALL other threads to enter abort sequence and end the program
			try:
				self.client.send("Test")
			except Exception as err:
				print(err)
				break
		print("Connection broken!")
			
	def parseString(self, str):
		pass
		
# start from command line
def terminalStart():
	if len(sys.argv) != 11:
		print('Need 10 parameters')
		sys.exit(1)
	try:
		launch_code = int(sys.argv[1])
		burn_duration = float(sys.argv[2]) 
		ignitor_timing = float(sys.argv[3])
		valve_open_timing = float(sys.argv[4])
		valve_closing_time = float(sys.argv[5])
		limit_switch_slowdown_speed = float(sys.argv[6])
		angle_limit_switch_slowdown_mode = float(sys.argv[7])
		opening_profile_angle_delimiter = float(sys.argv[8])
		total_opening_time = float(sys.argv[9])
		initial_opening_time = float(sys.argv[10])
	except ValueError:
		print('ValueError. Check that parameters are valid numbers')
		sys.exit(2)

	test = ServerMain()
	# init main test routine directly (don't forget connect test thread!)
	
def serverStart():
	# init test server and main test routine
	test = ServerMain()
	test.initServer()
