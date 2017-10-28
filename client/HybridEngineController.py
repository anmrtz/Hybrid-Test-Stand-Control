#-----------------------------------------------------------------
#
#----- This is a Hybrid Engine Controller written in Python ------
#
#-----------------------------------------------------------------

#required libraries
import sys
import socket
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5 import *

class ReceiveThread(QtCore.QThread):

    msg_received = QtCore.pyqtSignal(object)
    limit_state_received = QtCore.pyqtSignal(int, int)
    conn_lost = QtCore.pyqtSignal(object)

    def __init__(self, sock):
        QtCore.QThread.__init__(self)
        self.sock = sock

    def run(self):
        self.msg_received.emit('\nStarting receive thread...')
        while True:
            try:
                server_response = self.sock.recv(4096)
            except Exception as e:
                self.msg_received.emit('\nReceive thread failed: %s' % str(e))
                break    
            msg = str(server_response, "utf-8")
            if (msg == ''):
                self.conn_lost.emit('\nReceive thread connection lost!')
                break
                
            tokens = msg.split()
            if (tokens[0] == 'LIMIT'):
            	try:
                    switch_open = int(tokens[1])
                    switch_closed = int(tokens[2])
                    self.limit_state_received.emit(switch_open,switch_closed)
            	except Exception as e:
                    self.msg_received.emit('\nInvalid limit switch token: ' + str(e))
            else:
                self.msg_received.emit('\nReceived: %s' % msg)
	
#The main class containing our app
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hybrid Engine Controller'
        self.textboxes()
        self.buttons()
        self.window()
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(True)

    def textboxes(self):

        #ip address
        self.ip_box = QLineEdit(self)
        self.ip_box.move(130, 20)
        self.ip_box.resize(230,30)
        self.ip_box.setPlaceholderText("IP address")
        self.ip_box.setText("10.42.0.199")
        #----accompanying label
        self.ip_label = QLabel(self)
        self.ip_label.setText("IP ADDRESS ")
        self.ip_label.move(20,20)
        
        #Launch code
        self.launch_code_box = QLineEdit(self)
        self.launch_code_box.move(130, 70)
        self.launch_code_box.resize(230,30)
        self.launch_code_box.setPlaceholderText("Launch code")
        #----only integers are allowed
        int_validator = QtGui.QIntValidator()
        self.launch_code_box.setValidator(int_validator)
        #----accompanying label
        self.launch_label = QLabel(self)
        self.launch_label.setText("LAUNCH CODE ")
        self.launch_label.move(20,70)

        #Burn duration
        self.burn_duration_box = QLineEdit(self)
        self.burn_duration_box.move(130, 120)
        self.burn_duration_box.resize(230,30)
        self.burn_duration_box.setPlaceholderText("Burn duration")
        #----only doubles are allowed
        double_validator = QtGui.QDoubleValidator()
        self.burn_duration_box.setValidator(double_validator)
        #----accompanying label
        self.burn_label = QLabel(self)
        self.burn_label.setText("BURN DURATION")
        self.burn_label.move(20,120)
        
        #Ignitor timing
        self.ignitor_timing_box = QLineEdit(self)
        self.ignitor_timing_box.move(130, 170)
        self.ignitor_timing_box.resize(230,30)
        self.ignitor_timing_box.setPlaceholderText("Ignitor timing")
        #----only doubles are allowed
        self.ignitor_timing_box.setValidator(double_validator)
        #----accompanying label
        self.ignitor_label = QLabel(self)
        self.ignitor_label.setText("IGNITOR TIME")
        self.ignitor_label.move(20,170)
        
        #Valve open timing
        self.valve_open_timing_box = QLineEdit(self)
        self.valve_open_timing_box.move(130, 220)
        self.valve_open_timing_box.resize(230,30)
        self.valve_open_timing_box.setPlaceholderText("Valve open timing")
        #----only doubles are allowed
        self.valve_open_timing_box.setValidator(double_validator)
        #----accompanying label
        self.valve_open_label = QLabel(self)
        self.valve_open_label.setText("VALVE OPENING")
        self.valve_open_label.move(20,220)
        
        
        #Valve closing time
        self.valve_closing_time_box = QLineEdit(self)
        self.valve_closing_time_box.move(130, 270)
        self.valve_closing_time_box.resize(230,30)
        self.valve_closing_time_box.setPlaceholderText("Valve closing time")
        #----only doubles are allowed
        self.valve_closing_time_box.setValidator(double_validator)
        #----accompanying label
        self.valve_close_label = QLabel(self)
        self.valve_close_label.setText("VALVE CLOSING")
        self.valve_close_label.move(20,270)

        #Limit switch slowdown mode speed
        self.limit_switch_slowdown_box = QLineEdit(self)
        self.limit_switch_slowdown_box.move(130, 320)
        self.limit_switch_slowdown_box.resize(230,30)
        self.limit_switch_slowdown_box.setPlaceholderText("Limit switch slowdown speed")
        #----only doubles are allowed
        self.limit_switch_slowdown_box.setValidator(double_validator)
        #----accompanying label
        self.limit_label = QLabel(self)
        self.limit_label.setText("LIMIT SWITCH")
        self.limit_label.move(20,320)

        #Angle limit switch slowdown
        self.angle_limit_switch_slowdown_box = QLineEdit(self)
        self.angle_limit_switch_slowdown_box.move(130, 370)
        self.angle_limit_switch_slowdown_box.resize(230,30)
        self.angle_limit_switch_slowdown_box.setPlaceholderText("Angle limit switch slowdown")
        #----only doubles are allowed
        self.angle_limit_switch_slowdown_box.setValidator(double_validator)
        #----accompanying label
        self.angle_limit_label = QLabel(self)
        self.angle_limit_label.setText("ANGLE LIMIT")
        self.angle_limit_label.move(20,370)

        #Opening profile angle
        self.opening_profile_angle_delimiter_box = QLineEdit(self)
        self.opening_profile_angle_delimiter_box.move(130, 420)
        self.opening_profile_angle_delimiter_box.resize(230,30)
        self.opening_profile_angle_delimiter_box.setPlaceholderText("Opening profile angle delimiter")
        #----only doubles are allowed
        self.opening_profile_angle_delimiter_box.setValidator(double_validator)
        #----accompanying label
        self.opening_profile_label = QLabel(self)
        self.opening_profile_label.setText("PROFILE ANGLE")
        self.opening_profile_label.move(20,420)
        
        #Total opening time
        self.total_opening_time_box = QLineEdit(self)
        self.total_opening_time_box.move(130, 470)
        self.total_opening_time_box.resize(230,30)
        self.total_opening_time_box.setPlaceholderText("Total opening time")
        #----only doubles are allowed
        self.total_opening_time_box.setValidator(double_validator)
        #----accompanying label
        self.total_time_label = QLabel(self)
        self.total_time_label.setText("Total Time")
        self.total_time_label.move(20,470)

        #Initial opening time
        self.initial_opening_time_box = QLineEdit(self)
        self.initial_opening_time_box.move(130, 520)
        self.initial_opening_time_box.resize(230,30)
        self.initial_opening_time_box.setPlaceholderText("Initial opening time")
        #----only doubles are allowed
        self.initial_opening_time_box.setValidator(double_validator)
        #----accompanying label
        self.opening_time_label = QLabel(self)
        self.opening_time_label.setText("Opening Time")
        self.opening_time_label.move(20,520)
        
        #Raspberry Status
        self.status_box = QPlainTextEdit(self)
        self.status_box.setReadOnly(True)
        self.status_box.move(400,70);
        self.status_box.resize(380,600);

		#Limit switch indicator
        self.indicator = QPushButton(self)
        self.indicator.move(530,20)
        self.indicator.resize(250,30)
        self.indicator.setEnabled(False)
        self.indicator.setText("Unknown")
        self.indicator.setStyleSheet("background-color: gray")

        #limit indicator label
        self.indicator_label = QLabel(self)
        self.indicator_label.setText("Valve status")
        self.indicator_label.move(400,20)
		
    def buttons(self):

        #connect button
        self.connect = QPushButton('Connect', self)
        self.connect.setToolTip('You can only submit after the connection has been successfully established')
        self.connect.resize(80,40)
        self.connect.move(100, 570)
        self.connect.clicked.connect(self.set_connection)

        #submit button
        self.submit = QPushButton('Submit', self)
        self.submit.setToolTip('You can only submit after the connection has been successfully established')
        self.submit.resize(80,40)
        self.submit.move(200, 570)
        self.submit.clicked.connect(self.submit_data)
        self.submit.setEnabled(False)
        
        #ABORT button
        self.abort = QPushButton('Abort', self)
        self.abort.resize(80,40)
        self.abort.move(205,630)
        self.abort.clicked.connect(self.abortion)
        self.abort.setEnabled(False)

        #TEST IGNITOR button
        self.ignitor = QPushButton('Test Ignitor', self)
        self.ignitor.resize(80,40)
        self.ignitor.move(295,630)
        self.ignitor.clicked.connect(self.ignition)
        self.ignitor.setEnabled(False)

        #OPEN VALVE button
        self.open_valve = QPushButton('Open Valve', self)
        self.open_valve.resize(80,40)
        self.open_valve.move(30,630)
        self.open_valve.clicked.connect(self.valve_opener)
        self.open_valve.setEnabled(False)

        #CLOSE VALVE button
        self.close_valve = QPushButton('Close Valve', self)
        self.close_valve.resize(80,40)
        self.close_valve.move(120,630)
        self.close_valve.clicked.connect(self.valve_closer)
        self.close_valve.setEnabled(False)

    #in this part of the code we need to connect using sockets
    def set_connection(self):         
        
        #Collecting all of the variables from the textboxes
        self.launch_code = self.launch_code_box.text()
        self.burn_duration = self.burn_duration_box.text()
        self.ignitor_timing = self.ignitor_timing_box.text()
        self.valve_open_timing = self.valve_open_timing_box.text()
        self.valve_closing_time = self.valve_closing_time_box.text()
        self.limit_switch_slowdown = self.limit_switch_slowdown_box.text()
        self.angle_limit_switch_slowdown = self.angle_limit_switch_slowdown_box.text()
        self.opening_profile_angle_delimiter = self.opening_profile_angle_delimiter_box.text()
        self.total_opening_time = self.total_opening_time_box.text()
        self.initial_opening_time = self.initial_opening_time_box.text()
        
        self.engine_data = "HEAD " + self.launch_code + " " + self.burn_duration + " " + self.ignitor_timing + " " + self.valve_open_timing + " " + self.valve_closing_time + " " + self.limit_switch_slowdown + " " + self.angle_limit_switch_slowdown + " " + self.opening_profile_angle_delimiter + " " + self.total_opening_time + " " + self.initial_opening_time
        
         #establishing the socket connection
        try:
            self.sock.connect((self.ip_box.text(), 9999))
            self.status_box.appendPlainText("\nCONNECTION IS ESTABLISHED!\nHere is the data that your are about to send:" + "\nLAUNCH CODE: " + self.launch_code + "\nBURN DURATION: " + self.burn_duration + "\nIGNITOR TIMING: " + self.ignitor_timing + "\nVALVE OPENING TIME: " + self.valve_open_timing + "\nVALVE CLOSING TIME: " + self.valve_closing_time + "\nLIMIT SWITCH SLOWDOWN: " + self.limit_switch_slowdown + "\nOPENING PROFILE ANGLE DELIMITER: " + self.opening_profile_angle_delimiter + "\nTOTAL OPENING TIME: " + self.total_opening_time + "\nINITIAL OPENING TIME: " + self.initial_opening_time + "\n\nClick submit if the data is correct!")

            self.receiver = ReceiveThread(self.sock)
            self.receiver.msg_received.connect(self.on_msg_received)
            self.reciever.limit_state_received.connect(self.on_limit_state_received)
            self.reciever.conn_lost.connect(self.on_conn_lost)
            self.receiver.start()        

            self.connect.setEnabled(False)
            self.submit.setEnabled(True) 
        except Exception as e:
            self.status_box.appendPlainText("Connection failure:" + str(e))

    #submit data to the  server
    def submit_data(self):
        try:
            self.sock.sendall(self.engine_data.encode())
        except Exception as e:
            self.status_box.appendPlainText("Problem: " + str(e))
            return
        self.abort.setEnabled(True)
        self.ignitor.setEnabled(True)
        self.open_valve.setEnabled(True)
        self.close_valve.setEnabled(True)

    #abort
    def abortion(self):
        self.sock.sendall("ABORT".encode())

    #open valve
    def valve_opener(self):
        self.sock.sendall("VALVE OPEN".encode())

    #ignition
    def ignition(self):
        self.sock.sendall("IGNITE".encode())

    #valve closing
    def valve_closer(self):
        self.sock.sendall("VALVE CLOSE".encode())

    def on_msg_received(self, msg):
        self.status_box.appendPlainText(msg)
                
    def on_limit_state_received(self, switch_open, switch_closed):
        if switch_open and not switch_closed:
            self.indicator.setText("FULLY OPEN")
            self.indicator.setStyleSheet("background-color: green")
        elif not switch_open and switch_closed:
            self.indicator.setText("FULLY CLOSED")
            self.indicator.setStyleSheet("background-color: red")
        elif not switch_open and not switch_closed:
            self.indicator.setText("INTERMEDIATE")
            self.indicator.setStyleSheet("background-color: yellow")
        else:
            self.indicator.setText("INVALID")
            self.indicator.setStyleSheet("background-color: white")
    	
    def on_conn_lost(self, msg):
        self.status_box.appendPlainText(msg)
        self.indicator.setText("Unknown")
        self.indicator.setStyleSheet("background-color: gray")
        self.sock.close()

    #this method is responsible for basic window parameters
    def window(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800,700)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
