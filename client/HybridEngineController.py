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

#The main class containing our app
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hybrid Engine Controller'
        self.textboxes()
        self.buttons()
        self.window()

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
        self.launch_code_box.move(130, 80)
        self.launch_code_box.resize(230,30)
        self.launch_code_box.setPlaceholderText("Launch code")
        #----only integers are allowed
        int_validator = QtGui.QIntValidator()
        self.launch_code_box.setValidator(int_validator)
        #----accompanying label
        self.launch_label = QLabel(self)
        self.launch_label.setText("LAUNCH CODE ")
        self.launch_label.move(20,80)

        #Burn duration
        self.burn_duration_box = QLineEdit(self)
        self.burn_duration_box.move(130, 140)
        self.burn_duration_box.resize(230,30)
        self.burn_duration_box.setPlaceholderText("Burn duration")
        #----only doubles are allowed
        double_validator = QtGui.QDoubleValidator()
        self.burn_duration_box.setValidator(double_validator)
        #----accompanying label
        self.burn_label = QLabel(self)
        self.burn_label.setText("BURN DURATION")
        self.burn_label.move(20,140)
        
        #Ignitor timing
        self.ignitor_timing_box = QLineEdit(self)
        self.ignitor_timing_box.move(130, 200)
        self.ignitor_timing_box.resize(230,30)
        self.ignitor_timing_box.setPlaceholderText("Ignitor timing")
        #----only doubles are allowed
        self.ignitor_timing_box.setValidator(double_validator)
        #----accompanying label
        self.ignitor_label = QLabel(self)
        self.ignitor_label.setText("IGNITOR TIME")
        self.ignitor_label.move(20,200)
        
        #Valve open timing
        self.valve_open_timing_box = QLineEdit(self)
        self.valve_open_timing_box.move(130, 260)
        self.valve_open_timing_box.resize(230,30)
        self.valve_open_timing_box.setPlaceholderText("Valve open timing")
        #----only doubles are allowed
        self.valve_open_timing_box.setValidator(double_validator)
        #----accompanying label
        self.valve_open_label = QLabel(self)
        self.valve_open_label.setText("VALVE OPENING")
        self.valve_open_label.move(20,260)
        
        
        #Valve closing time
        self.valve_closing_time_box = QLineEdit(self)
        self.valve_closing_time_box.move(130, 320)
        self.valve_closing_time_box.resize(230,30)
        self.valve_closing_time_box.setPlaceholderText("Valve closing time")
        #----only doubles are allowed
        self.valve_closing_time_box.setValidator(double_validator)
        #----accompanying label
        self.valve_close_label = QLabel(self)
        self.valve_close_label.setText("VALVE CLOSING")
        self.valve_close_label.move(20,320)

        #Limit switch slowdown mode speed
        self.limit_switch_slowdown_box = QLineEdit(self)
        self.limit_switch_slowdown_box.move(130, 380)
        self.limit_switch_slowdown_box.resize(230,30)
        self.limit_switch_slowdown_box.setPlaceholderText("Limit switch slowdown speed")
        #----only doubles are allowed
        self.limit_switch_slowdown_box.setValidator(double_validator)
        #----accompanying label
        self.limit_label = QLabel(self)
        self.limit_label.setText("LIMIT SWITCH")
        self.limit_label.move(20,380)

        #Angle limit switch slowdown
        self.angle_limit_switch_slowdown_box = QLineEdit(self)
        self.angle_limit_switch_slowdown_box.move(130, 440)
        self.angle_limit_switch_slowdown_box.resize(230,30)
        self.angle_limit_switch_slowdown_box.setPlaceholderText("Angle limit switch slowdown")
        #----only doubles are allowed
        self.angle_limit_switch_slowdown_box.setValidator(double_validator)
        #----accompanying label
        self.angle_limit_label = QLabel(self)
        self.angle_limit_label.setText("ANGLE LIMIT")
        self.angle_limit_label.move(20,440)

        #Opening profile angle
        self.opening_profile_angle_delimiter_box = QLineEdit(self)
        self.opening_profile_angle_delimiter_box.move(130, 500)
        self.opening_profile_angle_delimiter_box.resize(230,30)
        self.opening_profile_angle_delimiter_box.setPlaceholderText("Opening profile angle delimiter")
        #----only doubles are allowed
        self.opening_profile_angle_delimiter_box.setValidator(double_validator)
        #----accompanying label
        self.opening_profile_label = QLabel(self)
        self.opening_profile_label.setText("PROFILE ANGLE")
        self.opening_profile_label.move(20,500)
        
        #Total opening time
        self.total_opening_time_box = QLineEdit(self)
        self.total_opening_time_box.move(130, 560)
        self.total_opening_time_box.resize(230,30)
        self.total_opening_time_box.setPlaceholderText("Total opening time")
        #----only doubles are allowed
        self.total_opening_time_box.setValidator(double_validator)
        #----accompanying label
        self.total_time_label = QLabel(self)
        self.total_time_label.setText("Total Time")
        self.total_time_label.move(20,560)

        #Initial opening time
        self.initial_opening_time_box = QLineEdit(self)
        self.initial_opening_time_box.move(130, 620)
        self.initial_opening_time_box.resize(230,30)
        self.initial_opening_time_box.setPlaceholderText("Initial opening time")
        #----only doubles are allowed
        self.initial_opening_time_box.setValidator(double_validator)
        #----accompanying label
        self.opening_time_label = QLabel(self)
        self.opening_time_label.setText("Opening Time")
        self.opening_time_label.move(20,620)
        
        #Raspberry Status
        self.status_box = QPlainTextEdit(self);
        self.status_box.move(80,770);
        self.status_box.resize(230,100);
        self.status_box.setPlainText("Awaiting the message from the raspberry pi. Please, don't input anything in this field")
        

    


    def buttons(self):

        #connect button
        self.connect = QPushButton('Connect', self)
        self.connect.setToolTip('You can only submit after the connection has been successfully established')
        self.connect.resize(80,40)
        self.connect.move(100, 700)
        self.connect.clicked.connect(self.set_connection)


        #submit button
        self.submit = QPushButton('Submit', self)
        self.submit.setToolTip('You can only submit after the connection has been successfully established')
        self.submit.resize(80,40)
        self.submit.move(200, 700)
        self.submit.clicked.connect(self.submit_data)
        #self.submit.clicked.connect(self.set_connection)
        

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
        
        self.engine_data = "HEAD" + self.launch_code + " " + self.burn_duration + " " + self.ignitor_timing + " " + self.valve_open_timing + " " + self.valve_closing_time + " " + self.limit_switch_slowdown + " " + self.opening_profile_angle_delimiter + " " + self.total_opening_time + " " + self.initial_opening_time
        
         #establishing the socket connection
        self.sock = socket.socket()
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

    #read data from the server to assure that the message was received
    def receive_data(self):
        while 1:
            server_response = self.sock.recv(1024);
            if(server_response):
                print(server_response)

    #this method is responsible for basic window parameters
    def window(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(400,900)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()



#Create the object of the class and thus our app

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
