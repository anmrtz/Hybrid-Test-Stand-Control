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
        self.l_code_box = QLineEdit(self)
        self.l_code_box.move(80, 80)
        self.l_code_box.resize(230,30)
        self.l_code_box.setPlaceholderText("Launch code")

        #Burn duration
        self.b_drtn_box = QLineEdit(self)
        self.b_drtn_box.move(80, 140)
        self.b_drtn_box.resize(230,30)
        self.b_drtn_box.setPlaceholderText("Burn duration")

        #Ignitor timing
        self.ignt_time_box = QLineEdit(self)
        self.ignt_time_box.move(80, 200)
        self.ignt_time_box.resize(230,30)
        self.ignt_time_box.setPlaceholderText("Ignitor timing")

        #Valve open timing
        self.vlv_opn_time_box = QLineEdit(self)
        self.vlv_opn_time_box.move(80, 260)
        self.vlv_opn_time_box.resize(230,30)
        self.vlv_opn_time_box.setPlaceholderText("Valve open timing")

        #Valve closing time
        self.vlv_cls_time_box = QLineEdit(self)
        self.vlv_cls_time_box.move(80, 320)
        self.vlv_cls_time_box.resize(230,30)
        self.vlv_cls_time_box.setPlaceholderText("Valve closing time")

        #Limit switch slowdown mode speed
        self.switch_slow_box = QLineEdit(self)
        self.switch_slow_box.move(80, 380)
        self.switch_slow_box.resize(230,30)
        self.switch_slow_box.setPlaceholderText("Limit switch slowdown mode speed")

        #Angle limit switch slowdown
        self.switch_angle_box = QLineEdit(self)
        self.switch_angle_box.move(80, 440)
        self.switch_angle_box.resize(230,30)
        self.switch_angle_box.setPlaceholderText("Angle limit switch slowdown")

        #Opening profile angle
        self.prof_ang_box = QLineEdit(self)
        self.prof_ang_box.move(80, 500)
        self.prof_ang_box.resize(230,30)
        self.prof_ang_box.setPlaceholderText("Opening profile angle")

        #Total opening time
        self.opn_time_box = QLineEdit(self)
        self.opn_time_box.move(80, 560)
        self.opn_time_box.resize(230,30)
        self.opn_time_box.setPlaceholderText("Total opening time")

        #Initial opening time
        self.init_time_box = QLineEdit(self)
        self.init_time_box.move(80, 620)
        self.init_time_box.resize(230,30)
        self.init_time_box.setPlaceholderText("Initial opening time")

        #Raspberry Status
        self.status_box = QPlainTextEdit(self);
        self.status_box.move(80,790);
        self.status_box.resize(230,80);
        self.status_box.setPlaceholderText("Message from the raspberry pi")
        self.status_box.setDisabled(True)


    


    def buttons(self):

        #connect button
        self.connect = QPushButton('Connect', self)
        self.connect.setToolTip('You can only submit after the connection has been successfully established')
        self.connect.resize(80,40)
        self.connect.move(100, 730)
        self.connect.clicked.connect(self.set_connection)


        #submit button
        self.submit = QPushButton('Submit', self)
        self.submit.setToolTip('You can only submit after the connection has been successfully established')
        self.submit.resize(80,40)
        self.submit.move(200, 730)


    #in this part of the code we need to connect using sockets
    def set_connection(self):
        self.sock = socket.socket()
        self.sock.connect(('localhost', 9999))
        self.conn_data = self.sock.recv(1024)
        self.sock.close()

        if(self.conn_data):
            print("connected")


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
