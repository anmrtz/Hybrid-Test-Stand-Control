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
        self.ip_box.move(80, 20)
        self.ip_box.resize(230,30)
        self.ip_box.setPlaceholderText("IP address")
        
        #Launch code
        self.launch_code_box = QLineEdit(self)
        self.launch_code_box.move(80, 80)
        self.launch_code_box.resize(230,30)
        self.launch_code_box.setPlaceholderText("Launch code")
        #----only integers are allowed
        int_validator = QtGui.QIntValidator()
        self.launch_code_box.setValidator(int_validator)

        #Burn duration
        self.burn_duration_box = QLineEdit(self)
        self.burn_duration_box.move(80, 140)
        self.burn_duration_box.resize(230,30)
        self.burn_duration_box.setPlaceholderText("Burn duration")
        #----only doubles are allowed
        double_validator = QtGui.QDoubleValidator()
        self.burn_duration_box.setValidator(double_validator)
        
        #Ignitor timing
        self.ignitor_timing_box = QLineEdit(self)
        self.ignitor_timing_box.move(80, 200)
        self.ignitor_timing_box.resize(230,30)
        self.ignitor_timing_box.setPlaceholderText("Ignitor timing")
        #----only doubles are allowed
        self.ignitor_timing_box.setValidator(double_validator)
        
        
        #Valve open timing
        self.valve_open_timing_box = QLineEdit(self)
        self.valve_open_timing_box.move(80, 260)
        self.valve_open_timing_box.resize(230,30)
        self.valve_open_timing_box.setPlaceholderText("Valve open timing")
        #----only doubles are allowed
        self.valve_open_timing_box.setValidator(double_validator)
        
        #Valve closing time
        self.valve_closing_time_box = QLineEdit(self)
        self.valve_closing_time_box.move(80, 320)
        self.valve_closing_time_box.resize(230,30)
        self.valve_closing_time_box.setPlaceholderText("Valve closing time")
        #----only doubles are allowed
        self.valve_closing_time_box.setValidator(double_validator)

        #Limit switch slowdown mode speed
        self.limit_switch_slowdown_box = QLineEdit(self)
        self.limit_switch_slowdown_box.move(80, 380)
        self.limit_switch_slowdown_box.resize(230,30)
        self.limit_switch_slowdown_box.setPlaceholderText("Limit switch slowdown speed")
        #----only doubles are allowed
        self.limit_switch_slowdown_box.setValidator(double_validator)

        #Angle limit switch slowdown
        self.angle_limit_switch_slowdown_box = QLineEdit(self)
        self.angle_limit_switch_slowdown_box.move(80, 440)
        self.angle_limit_switch_slowdown_box.resize(230,30)
        self.angle_limit_switch_slowdown_box.setPlaceholderText("Angle limit switch slowdown")
        #----only doubles are allowed
        self.angle_limit_switch_slowdown_box.setValidator(double_validator)

        #Opening profile angle
        self.opening_profile_angle_delimiter_box = QLineEdit(self)
        self.opening_profile_angle_delimiter_box.move(80, 500)
        self.opening_profile_angle_delimiter_box.resize(230,30)
        self.opening_profile_angle_delimiter_box.setPlaceholderText("Opening profile angle delimiter")
        #----only doubles are allowed
        self.opening_profile_angle_delimiter_box.setValidator(double_validator)
        
        #Total opening time
        self.total_opening_time_box = QLineEdit(self)
        self.total_opening_time_box.move(80, 560)
        self.total_opening_time_box.resize(230,30)
        self.total_opening_time_box.setPlaceholderText("Total opening time")
        #----only doubles are allowed
        self.total_opening_time_box.setValidator(double_validator)

        #Initial opening time
        self.initial_opening_time_box = QLineEdit(self)
        self.initial_opening_time_box.move(80, 620)
        self.initial_opening_time_box.resize(230,30)
        self.initial_opening_time_box.setPlaceholderText("Initial opening time")
        #----only doubles are allowed
        self.initial_opening_time_box.setValidator(double_validator)
        
        #Raspberry Status
        self.status_box = QPlainTextEdit(self);
        self.status_box.move(80,770);
        self.status_box.resize(230,100);
        self.status_box.setPlainText("Awaiting the message from the raspberry pi")
        self.status_box.setDisabled(True)
        

    


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
        #establishing the socket connection
        self.sock = socket.socket()
        self.sock.connect((self.ip_box.text(), 9999))              
        self.conn_data = self.sock.recv(1024)
        
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
        
        self.engine_data = self.launch_code + " " + self.burn_duration + " " + self.ignitor_timing + " " + self.valve_open_timing + " " + self.valve_closing_time + " " + self.limit_switch_slowdown + " " + self.opening_profile_angle_delimiter + " " + self.total_opening_time + " " + self.initial_opening_time
        
        
        if(self.conn_data):
            self.status_box.setPlainText("CONNECTION IS ESTABLISHED! Here is the data that your are about to send: " + self.engine_data + " Click submit if the data is correct")

    #submit data to the  server
    def submit_data(self):
        self.sock.sendall(self.engine_data.encode())

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
