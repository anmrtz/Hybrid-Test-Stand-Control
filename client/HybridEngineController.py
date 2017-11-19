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

	conn_lost = QtCore.pyqtSignal(object)
	msg_received = QtCore.pyqtSignal(object)
	limit_state_received = QtCore.pyqtSignal(int, int)
	ignitor_state_received = QtCore.pyqtSignal(int)
	encoder_position_received = QtCore.pyqtSignal(int)

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
					switch_open = tokens[1] == "1"
					switch_closed = tokens[2] == "1"
					self.limit_state_received.emit(switch_open,switch_closed)
				except Exception as e:
					self.msg_received.emit('\nInvalid limit switch token: ' + str(e))
			elif (tokens[0] == "IGNITOR"):
				try:
					ignitor_on = tokens[1] == "1"
					self.ignitor_state_received.emit(ignitor_on)
				except Exception as e:
					self.msg_received.emit('\nInvalid ignitor state token: ' + str(e))
			elif (tokens[0] == "ENCODER"):
				try:
					encoder_val = int(tokens[1])
					self.encoder_position_received.emit(encoder_val)
				except Exception as e:
					self.msg_received.emit('\nInvalid encoder state token: ' + str(e))
			else:
				self.msg_received.emit('\nFrom server: %s' % msg)

#The main class containing our app
class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title = 'Hybrid Engine Controller'

		self.receiver = None
		self.sock = None

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
		self.burn_duration_box.setPlaceholderText("Burn duration (s)")
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
		self.ignitor_timing_box.setPlaceholderText("Ignitor time (s)")
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
		self.valve_open_timing_box.setPlaceholderText("Valve opening time (s)")
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
		self.valve_closing_time_box.setPlaceholderText("Valve closing time (s)")
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
		self.total_time_label.setText("TOTAL TIME")
		self.total_time_label.move(20,470)

		#Initial opening time
		self.initial_opening_time_box = QLineEdit(self)
		self.initial_opening_time_box.move(130, 520)
		self.initial_opening_time_box.resize(230,30)
		self.initial_opening_time_box.setPlaceholderText("INITIAL OPENING TIME")
		#----only doubles are allowed
		self.initial_opening_time_box.setValidator(double_validator)
		#----accompanying label
		self.opening_time_label = QLabel(self)
		self.opening_time_label.setText("OPENING TIME")
		self.opening_time_label.move(20,520)

		#Raspberry Status
		self.status_box = QPlainTextEdit(self)
		self.status_box.setReadOnly(True)
		self.status_box.move(800,20);
		self.status_box.resize(380,650);

		#Limit switch indicator
		self.close_indicator = QPushButton(self)
		self.close_indicator.move(530,70)
		self.close_indicator.resize(250,30)
		self.close_indicator.setEnabled(False)
		#Limit switch indicator
		self.open_indicator = QPushButton(self)
		self.open_indicator.move(530,20)
		self.open_indicator.resize(250,30)
		self.open_indicator.setEnabled(False)
		#ignitor indicator
		self.ignitor_indicator = QPushButton(self)
		self.ignitor_indicator.move(530,120)
		self.ignitor_indicator.resize(250,30)
		self.ignitor_indicator.setEnabled(False)

		#limit indicator label
		self.close_indicator_label = QLabel(self)
		self.close_indicator_label.setText("CLOSE SWITCH")
		self.close_indicator_label.move(400,70)
		#limit indicator label
		self.open_indicator_label = QLabel(self)
		self.open_indicator_label.setText("OPEN SWITCH")
		self.open_indicator_label.move(400,20)
		#ignitor indicator label
		self.ignitor_indicator_label = QLabel(self)
		self.ignitor_indicator_label.setText("IGNITOR STATUS")
		self.ignitor_indicator_label.move(400,120)

		#encoder position label
		self.encoder_position_label = QLabel(self)
		self.encoder_position_label.setText("ENCODER POS")
		self.encoder_position_label.move(400,170)
		#Angle limit switch slowdown
		self.encoder_position = QLineEdit(self)
		self.encoder_position.move(530, 170)
		self.encoder_position.resize(250,30)
		self.encoder_position.setReadOnly(True)
		self.encoder_position.setPlaceholderText("Unknown")

		
		self.set_all_indicator_buttons("Unknown", "background-color: gray")

		#disable unused instructions
		self.disable_element(self.limit_switch_slowdown_box)
		self.disable_element(self.angle_limit_switch_slowdown_box)
		self.disable_element(self.opening_profile_angle_delimiter_box)
		self.disable_element(self.total_opening_time_box)
		self.disable_element(self.initial_opening_time_box)
		self.disable_element(self.opening_profile_angle_delimiter_box)
		self.disable_element(self.total_opening_time_box)
		self.disable_element(self.initial_opening_time_box)
		self.disable_element(self.ignitor_timing_box)

		#connect button
		self.connect = QPushButton('Connect', self)
		self.connect.setToolTip('You can only submit after the connection has been successfully established')
		self.connect.resize(80,40)
		self.connect.move(20, 570)
		self.connect.clicked.connect(self.set_connection)

		#submit button
		self.submit = QPushButton('Auto Test', self)
		self.submit.setToolTip('You can only submit after the connection has been successfully established')
		self.submit.resize(80,40)
		self.submit.move(200, 570)
		self.submit.clicked.connect(self.submit_data)
		self.submit.setEnabled(False)

		#DISCONNECT button
		self.disconnect = QPushButton('Disconnect', self)
		self.disconnect.resize(80,40)
		self.disconnect.move(110,570)
		self.disconnect.clicked.connect(self.set_disconnect)
		self.disconnect.setEnabled(False)

		#ABORT button
		self.abort = QPushButton('Abort', self)
		self.abort.resize(70,100)
		self.abort.move(290,570)
		self.abort.clicked.connect(self.abortion)
		self.abort.setEnabled(False)
		self.abort.setStyleSheet("background-color: red")

		#TEST IGNITOR button
		self.ignitor = QPushButton('Test Ignitor', self)
		self.ignitor.resize(80,40)
		self.ignitor.move(200,630)
		self.ignitor.clicked.connect(self.ignition)
		self.ignitor.setEnabled(False)

		#OPEN VALVE button
		self.open_valve = QPushButton('Open Valve', self)
		self.open_valve.resize(80,40)
		self.open_valve.move(20,630)
		self.open_valve.clicked.connect(self.valve_opener)
		self.open_valve.setEnabled(False)

		#CLOSE VALVE button
		self.close_valve = QPushButton('Close Valve', self)
		self.close_valve.resize(80,40)
		self.close_valve.move(110,630)
		self.close_valve.clicked.connect(self.valve_closer)
		self.close_valve.setEnabled(False)

		self.setWindowTitle(self.title)
		self.setFixedSize(1200,700)
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.move(0,0)
		self.show()

	def disable_element(self, obj):
		obj.setEnabled(False)
		obj.setText("0")

	#in this part of the code we need to connect using sockets
	def set_connection(self):
		if self.sock is None:
			self.sock = socket.socket()
			self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		#establishing the socket connection
		try:
			self.sock.connect((self.ip_box.text(), 9999))
			self.status_box.appendPlainText("\nCONNECTION IS ESTABLISHED!")

			if self.receiver is None:
				self.receiver = ReceiveThread(self.sock)
				self.receiver.msg_received.connect(self.on_msg_received)
				self.receiver.limit_state_received.connect(self.on_limit_state_received)
				self.receiver.encoder_position_received.connect(self.on_encoder_position_received)
				self.receiver.ignitor_state_received.connect(self.on_ignitor_state_received)
				self.receiver.conn_lost.connect(self.on_conn_lost)
				self.receiver.start()

			self.connect.setEnabled(False)
			#self.disconnect.setEnabled(True)
			#self.submit.setEnabled(True)
			#self.ignitor.setEnabled(True)
			self.abort.setEnabled(True)
			self.open_valve.setEnabled(True)
			self.close_valve.setEnabled(True)
		except Exception as e:
			self.status_box.appendPlainText("Connection failure:" + str(e))

	#submit data to the  server
	def submit_data(self):
				#Collecting all of the variables from the textboxes
		launch_code = self.launch_code_box.text()
		burn_duration = self.burn_duration_box.text()
		ignitor_timing = self.ignitor_timing_box.text()
		valve_open_timing = self.valve_open_timing_box.text()
		valve_closing_time = self.valve_closing_time_box.text()
		limit_switch_slowdown = self.limit_switch_slowdown_box.text()
		angle_limit_switch_slowdown = self.angle_limit_switch_slowdown_box.text()
		opening_profile_angle_delimiter = self.opening_profile_angle_delimiter_box.text()
		total_opening_time = self.total_opening_time_box.text()
		initial_opening_time = self.initial_opening_time_box.text()

		engine_data = "HEAD " + launch_code + " " + burn_duration + " " + ignitor_timing + " " + valve_open_timing + " " + valve_closing_time + " " + limit_switch_slowdown + " " + angle_limit_switch_slowdown + " " + opening_profile_angle_delimiter + " " + total_opening_time + " " + initial_opening_time


		try:
			self.sock.sendall(self.engine_data.encode())
		except Exception as e:
			self.status_box.appendPlainText("Problem: " + str(e))
			return
		self.submit.setEnabled(False)
		self.abort.setEnabled(True)
		self.ignitor.setEnabled(True)
		self.open_valve.setEnabled(True)
		self.close_valve.setEnabled(True)
		self.close_valve.setEnabled(True)
		self.close_valve.setEnabled(True)

		
	def set_disconnect(self):
		on_conn_lost("Disconnected")

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
		if switch_open:
			self.open_indicator.setText("FULLY OPEN")
			self.open_indicator.setStyleSheet("background-color: green")
		else:
			self.open_indicator.setText("")
			self.open_indicator.setStyleSheet("background-color: white")
		if switch_closed:
			self.close_indicator.setText("FULLY CLOSED")
			self.close_indicator.setStyleSheet("background-color: green")
		else:
			self.close_indicator.setText("")
			self.close_indicator.setStyleSheet("background-color: white")

	def on_encoder_position_received(self, value):
		self.encoder_position.setText(str(value))
			
	def on_ignitor_state_received(self, active):
		if active:
			self.ignitor_indicator.setText("ON")
			self.ignitor_indicator.setStyleSheet("background-color: red")
		else:
			self.ignitor_indicator.setText("OFF")
			self.ignitor_indicator.setStyleSheet("background-color: white")

	def set_all_indicator_buttons(self, msg, color):
		self.close_indicator.setText(msg)
		self.close_indicator.setStyleSheet(color)

		self.open_indicator.setText(msg)
		self.open_indicator.setStyleSheet(color)

		self.ignitor_indicator.setText(msg)
		self.ignitor_indicator.setStyleSheet(color)

	def on_conn_lost(self, msg):
		self.status_box.appendPlainText(msg)
		self.set_all_indicator_buttons("Unknown", "background-color: gray")
		self.encoder_position.setText("Unknown")
		self.sock.close()
		self.sock = None

		self.connect.setEnabled(True)
		self.disconnect.setEnabled(False)

		self.abort.setEnabled(False)
		self.ignitor.setEnabled(False)
		self.open_valve.setEnabled(False)
		self.close_valve.setEnabled(False)

		self.receiver = None

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
