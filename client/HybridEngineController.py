#-----------------------------------------------------------------
#
#----- This is a Hybrid Engine Controller written in Python ------
#
#-----------------------------------------------------------------

#required libraries
import sys
import socket
import _thread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal

#The main class containing our app
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hybrid Engine Controller'
        self.textboxes()
        self.buttons()
        self.window()
        self.sock = socket.socket()

    def textboxes(self):

        #ip address
        self.ip_box = QLineEdit(self)
        self.ip_box.move(130, 20)
        self.ip_box.resize(230,30)
        self.ip_box.setPlaceholderText("IP address")
        self.ip_box.setText("localhost")
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
        self.status_box = QPlainTextEdit(self);
        self.status_box.move(80,690);
        self.status_box.resize(230,100);
        self.status_box.setPlainText("Awaiting the message from the raspberry pi. Please, don't input anything in this field")

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
        #self.submit.clicked.connect(self.set_connection)

        #ABORT button
        self.abort = QPushButton('Abort', self)
        self.abort.resize(80,40)
        self.abort.move(205,630)
        self.abort.clicked.connect(self.abortion)

        #TEST IGNITOR button
        self.ignitor = QPushButton('Test Ignitor', self)
        self.ignitor.resize(80,40)
        self.ignitor.move(295,630)
        self.ignitor.clicked.connect(self.ignition)

        #OPEN VALVE button
        self.open_valve = QPushButton('Open Valve', self)
        self.open_valve.resize(80,40)
        self.open_valve.move(30,630)
        self.open_valve.clicked.connect(self.valve_opener)

        #CLOSE VALVE button
        self.close_valve = QPushButton('Close Valve', self)
        self.close_valve.resize(80,40)
        self.close_valve.move(120,630)
        self.close_valve.clicked.connect(self.valve_closer)
        

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
            self.status_box.setPlainText("CONNECTION IS ESTABLISHED! Here is the data that your are about to send: " + "LAUNCH CODE: " + self.launch_code + " BURN DURATION: " + self.burn_duration + " IGNITOR TIMING: " + self.ignitor_timing + " VALVE OPENING TIME: " + self.valve_open_timing + " VALVE CLOSING TIME: " + self.valve_closing_time + " LIMIT SWITCH SLOWDOWN: " + self.limit_switch_slowdown + " OPENING PROFILE ANGLE DELIMITER: " + self.opening_profile_angle_delimiter + " TOTAL OPENING TIME: " + self.total_opening_time + " INITIAL OPENING TIME: " + self.initial_opening_time + " Click submit if the data is correct!")
        except:
            print("Error")
            QMessageBox.about(self, "Problem", "No connection baby!")
 

    
    #submit data to the  server
    def submit_data(self):
        self.sock.sendall(self.engine_data.encode())
        _thread.start_new_thread(self.receive_data, ())

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

    #read data from the server to assure that the message was received
    def receive_data(self):
        data_received = pyqtSignal('QString')
        while 1:
            server_response = self.sock.recv(1024)
            if(server_response):
                print(server_response) #this should be shown on the status_box but I don't know how to get the data from this thread and send it to the main thread
                #self.status_box.setPlainText("fuck man")#str(server_response, "utf-8"))
                
   
    
        

    #this method is responsible for basic window parameters
    def window(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(400,815)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
        
#Create the object of the class and thus our app

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
