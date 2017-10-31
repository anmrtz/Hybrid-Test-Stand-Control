import socket
import sys
import time
import os
import signal

END_SERVER = False
end_Server_lock = threading.Lock()

def killServer(msg = "NO_ABORT_MSG"):
	with end_test_lock:
		global END_SERVER
		if END_SERVER:
			return
		END_SERVER = True
		print("Killing Server\n Reason: " + str(msg))


class ControlServer():
    def __init__ (self):
        pass
    def startServer(self):
        self.sk = socket.socket()
        self.sk.setsockopt(socket.socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            f = os.popen("ip addr showing eth0")
            host = f.read().split("inet ")[1].split("/")[0]
            f.close()
        except: Exception as e:
            killServer(e)
            return
       print('eth0 IP: ' + host)
       port = 9999
	   address = (host,port)
       print('Starting Server on %s' % sys.version)
       self.sk.bind(address)
       self.sk.listen(5)

       print("Connect control laptop")

		# wait for a new connection and pull settings data
		try:
			self.client, addr = self.sk.accept()
			# the recieved message is stored in data
			data = self.client.recv(1024)
			data = data.decode('utf-8')
		except Exception as e:
			killServer(e)
			return
		except KeyboardInterrupt:
			killServer("Keyboard interrupt")
			return
        print ("Pi got " + data)

        signal.signal = (signal.SIGINT, self.handleKeyboardInt)

        connectionTestThread = threading.Thread(target=self.checkConnection, args = ())

        connectionTestThread.daemon = False
        connectionTestThread.start()

        #tokenize thread
        params = data.split(' ')
        #check for propper header
        if params[0] != "HEAD":
            killServer("Invalid parameter header")
            return
        return data[1:]


    #Wrapper for sending a Message back to the control laptop

    def sendMessage(self, toSend):
        try:
            self.conn.send(toSend)
        except Exception as e :
            print("Error sending back to control!")
        return

    #Background threaded process to ensure connection maintained

	def checkConnection(self):
		while not END_TEST:
			time.sleep(0.5)
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

    def waitForOpen(self):
        OPEN_GIVEN = False
        while not OPEN_GIVEN:
            time.sleep(0.5)
            #grab data and check if it's the string 'OPEN'
            check = self.client.recv(4)
			check = data.decode('utf-8')
            if data == "OPEN":
                OPEN_GIVEN = True
        #leave if we get it, procede with rest of prog

# Run in background thread, check for abort signal
    def checkAbort(self):
        ABORT_GIVEN = False
        while not OPEN_GIVEN:
            time.sleep(0.5)
            #grab data and check if it's the string 'OPEN'
            check = self.client.recv(4)
    		check = data.decode('utf-8')
            if data == "ABORT":
                ABORT_GIVEN = True
    
