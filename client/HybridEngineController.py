#-----------------------------------------------------------------
#
#----- This is a Hybrid Engine Controller written in Python ------
#
#-----------------------------------------------------------------

#required libraries
import sys
import socket
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5 import *

_DEGREES_PER_ENCODER_COUNT = 90.0 / 300.0

class ReceiveThread(QtCore.QThread):

	conn_lost = QtCore.pyqtSignal(object)
	msg_received = QtCore.pyqtSignal(object)
	limit_state_received = QtCore.pyqtSignal(int, int)
	ignitor_state_received = QtCore.pyqtSignal(int)
	encoder_position_received = QtCore.pyqtSignal(int)
	default_velocity_received = QtCore.pyqtSignal(float)
	current_velocity_received = QtCore.pyqtSignal(float)

	def __init__(self, sock):
		QtCore.QThread.__init__(self)
		self.sock = sock
		self.charStream = ''

	def run(self):
		self.msg_received.emit('\nStarting receive thread...')
		while True:
			try:				
				server_response = self.sock.recv(1024)
			except Exception as e:
				self.conn_lost.emit('\nReceive thread failed: %s' % str(e))
				return
			msg = str(server_response, "utf-8")
			if (msg == ''):
				self.conn_lost.emit('\nReceive thread connection lost!')
				return

			self.charStream += msg

			while True:
				a = re.search(r'\b(END)\b', self.charStream)
				if a is None:
					break
						
				instruction = self.charStream[:a.start()]
				self.charStream = self.charStream[a.start()+3:]
			
				tokens = instruction.split()
			
				if (tokens[0] == "STATEALL"):
					try:
						switch_open = tokens[1] == "1"
						switch_closed = tokens[2] == "1"
						encoder_val = int(tokens[3])
						ignitor_on = tokens[4] == "1"
						default_velocity = float(tokens[5])
						current_velocity = float(tokens[6])
						self.limit_state_received.emit(switch_open,switch_closed)
						self.ignitor_state_received.emit(ignitor_on)
						self.encoder_position_received.emit(encoder_val)
						self.default_velocity_received.emit(default_velocity)
						self.current_velocity_received.emit(current_velocity)
						
						#self.msg_received.emit('\nFrom server: %s' % msg)
					except Exception as e:
						self.msg_received.emit('\nInvalid state token: ' + str(e))
				elif (tokens[0] == "LIMIT"):
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
					self.msg_received.emit('\nFrom server: %s' % instruction)

#The main class containing our app
class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title = 'Hybrid Engine Controller'

		self.receiver = None
		self.sock = None
		self.status_timer = QTimer()

		#ip address
		self.ip_box = QLineEdit(self)
		self.ip_box.move(190, 20)
		self.ip_box.resize(170,30)
		self.ip_box.setPlaceholderText("IP address")
		self.ip_box.setText("10.42.0.209")
		#----accompanying label
		self.ip_label = QLabel(self)
		self.ip_label.setText("IP Address")
		self.ip_label.move(20,20)
		self.ip_label.resize(230,30)

		#Launch code
		self.launch_code_box = QLineEdit(self)
		self.launch_code_box.move(190, 70)
		self.launch_code_box.resize(170,30)
		self.launch_code_box.setPlaceholderText("Launch code")
		#----only integers are allowed
		int_validator = QtGui.QIntValidator()
		self.launch_code_box.setValidator(int_validator)
		#----accompanying label
		self.launch_label = QLabel(self)
		self.launch_label.setText("Launch code")
		self.launch_label.move(20,70)
		self.launch_label.resize(230,30)

		#Burn duration
		self.burn_duration_box = QLineEdit(self)
		self.burn_duration_box.move(190, 120)
		self.burn_duration_box.resize(170,30)
		self.burn_duration_box.setPlaceholderText("Burn duration (s)")
		#----only doubles are allowed
		double_validator = QtGui.QDoubleValidator()
		self.burn_duration_box.setValidator(double_validator)
		#----accompanying label
		self.burn_label = QLabel(self)
		self.burn_label.setText("Burn duration (s)")
		self.burn_label.move(20,120)
		self.burn_label.resize(230,30)

		#Ignitor timing
		self.ignitor_timing_box = QLineEdit(self)
		self.ignitor_timing_box.move(190, 170)
		self.ignitor_timing_box.resize(170,30)
		self.ignitor_timing_box.setPlaceholderText("Ignitor delay (s)")
		#----only doubles are allowed
		self.ignitor_timing_box.setValidator(double_validator)
		#----accompanying label
		self.ignitor_label = QLabel(self)
		self.ignitor_label.setText("Ignitor delay (s)")
		self.ignitor_label.move(20,170)
		self.ignitor_label.resize(230,30)

		#Valve open timing
		self.valve_open_timing_box = QLineEdit(self)
		self.valve_open_timing_box.move(190, 220)
		self.valve_open_timing_box.resize(170,30)
		self.valve_open_timing_box.setPlaceholderText("Valve opening time (s)")
		#----only doubles are allowed
		self.valve_open_timing_box.setValidator(double_validator)
		#----accompanying label
		self.valve_open_label = QLabel(self)
		self.valve_open_label.setText("Valve opening (s)")
		self.valve_open_label.move(20,220)
		self.valve_open_label.resize(230,30)

		#Valve closing time
		self.valve_closing_time_box = QLineEdit(self)
		self.valve_closing_time_box.move(190, 270)
		self.valve_closing_time_box.resize(170,30)
		self.valve_closing_time_box.setPlaceholderText("Valve closing time (s)")
		#----only doubles are allowed
		self.valve_closing_time_box.setValidator(double_validator)
		#----accompanying label
		self.valve_close_label = QLabel(self)
		self.valve_close_label.setText("Valve closing (s)")
		self.valve_close_label.move(20,270)
		self.valve_close_label.resize(230,30)

		#Limit switch slowdown mode speed
		self.limit_switch_slowdown_box = QLineEdit(self)
		self.limit_switch_slowdown_box.move(190, 320)
		self.limit_switch_slowdown_box.resize(170,30)
		self.limit_switch_slowdown_box.setPlaceholderText("Limit switch slowdown speed")
		#----only doubles are allowed
		self.limit_switch_slowdown_box.setValidator(double_validator)
		#----accompanying label
		self.limit_label = QLabel(self)
		self.limit_label.setText("Limit switch (s)")
		self.limit_label.move(20,320)
		self.limit_label.resize(230,30)

		#Angle limit switch slowdown
		self.angle_limit_switch_slowdown_box = QLineEdit(self)
		self.angle_limit_switch_slowdown_box.move(190, 370)
		self.angle_limit_switch_slowdown_box.resize(170,30)
		self.angle_limit_switch_slowdown_box.setPlaceholderText("Angle limit switch slowdown")
		#----only doubles are allowed
		self.angle_limit_switch_slowdown_box.setValidator(double_validator)
		#----accompanying label
		self.angle_limit_label = QLabel(self)
		self.angle_limit_label.setText("Angle limit (deg)")
		self.angle_limit_label.move(20,370)
		self.angle_limit_label.resize(230,30)

		#Opening profile angle
		self.opening_profile_angle_delimiter_box = QLineEdit(self)
		self.opening_profile_angle_delimiter_box.move(190, 420)
		self.opening_profile_angle_delimiter_box.resize(170,30)
		self.opening_profile_angle_delimiter_box.setPlaceholderText("Opening profile angle delimiter")
		#----only doubles are allowed
		self.opening_profile_angle_delimiter_box.setValidator(double_validator)
		#----accompanying label
		self.opening_profile_label = QLabel(self)
		self.opening_profile_label.setText("Profile angle (deg)")
		self.opening_profile_label.move(20,420)
		self.opening_profile_label.resize(230,30)

		#Total opening time
		self.total_opening_time_box = QLineEdit(self)
		self.total_opening_time_box.move(190, 470)
		self.total_opening_time_box.resize(170,30)
		self.total_opening_time_box.setPlaceholderText("Total opening time")
		#----only doubles are allowed
		self.total_opening_time_box.setValidator(double_validator)
		#----accompanying label
		self.total_time_label = QLabel(self)
		self.total_time_label.setText("Total time (s)")
		self.total_time_label.move(20,470)
		self.total_time_label.resize(230,30)

		#Initial opening time
		self.initial_opening_time_box = QLineEdit(self)
		self.initial_opening_time_box.move(190, 520)
		self.initial_opening_time_box.resize(170,30)
		self.initial_opening_time_box.setPlaceholderText("Initial opening time")
		#----only doubles are allowed
		self.initial_opening_time_box.setValidator(double_validator)
		#----accompanying label
		self.opening_time_label = QLabel(self)
		self.opening_time_label.setText("Opening time (s)")
		self.opening_time_label.move(20,520)
		self.opening_time_label.resize(230,30)

		#Raspberry Status
		self.status_box = QPlainTextEdit(self)
		self.status_box.setReadOnly(True)
		self.status_box.move(800,20);
		self.status_box.resize(380,650);

		#Close limit switch indicator
		self.close_indicator_label = QLabel(self)
		self.close_indicator_label.setText("Close switch")
		self.close_indicator_label.move(400,70)
		self.close_indicator = QPushButton(self)
		self.close_indicator.move(590,70)
		self.close_indicator.resize(170,30)
		self.close_indicator.setEnabled(False)

		#Open limit switch indicator
		self.open_indicator_label = QLabel(self)
		self.open_indicator_label.setText("Open switch")
		self.open_indicator_label.move(400,20)
		self.open_indicator = QPushButton(self)
		self.open_indicator.move(590,20)
		self.open_indicator.resize(170,30)
		self.open_indicator.setEnabled(False)

		#ignitor indicator
		self.ignitor_indicator = QPushButton(self)
		self.ignitor_indicator.move(590,120)
		self.ignitor_indicator.resize(170,30)
		self.ignitor_indicator.setEnabled(False)
		self.ignitor_indicator_label = QLabel(self)
		self.ignitor_indicator_label.setText("Ignitor status")
		self.ignitor_indicator_label.move(400,120)

		#encoder position
		self.encoder_position_label = QLabel(self)
		self.encoder_position_label.setText("Encoder pos. (deg)")
		self.encoder_position_label.move(400,170)
		self.encoder_position_label.resize(230,30)
		self.encoder_position = QLineEdit(self)
		self.encoder_position.move(590, 170)
		self.encoder_position.resize(170,30)
		self.encoder_position.setReadOnly(True)
		self.encoder_position.setPlaceholderText("Unknown")

		#current motor velocity
		self.current_velocity_label = QLabel(self)
		self.current_velocity_label.setText("Current vel. (deg/s)")
		self.current_velocity_label.move(400,220)
		self.current_velocity_label.resize(230,30)
		self.current_velocity = QLineEdit(self)
		self.current_velocity.move(590, 220)
		self.current_velocity.resize(170,30)
		self.current_velocity.setReadOnly(True)
		self.current_velocity.setPlaceholderText("Unknown")

		#motor default velocity
		self.default_velocity_label = QLabel(self)
		self.default_velocity_label.setText("Default vel. (deg/s)")
		self.default_velocity_label.move(400,270)
		self.default_velocity_label.resize(230,30)
		self.default_velocity = QLineEdit(self)
		self.default_velocity.move(590, 270)
		self.default_velocity.resize(170,30)
		self.default_velocity.setReadOnly(True)
		self.default_velocity.setPlaceholderText("Unknown")
		
		#motor default velocity
		self.status_delay_label = QLabel(self)
		self.status_delay_label.setWordWrap(True)
		self.status_delay_label.setText("Last update (ms)")
		self.status_delay_label.move(400,520)
		self.status_delay_label.resize(230,30)
		self.status_delay = QLineEdit(self)
		self.status_delay.move(590, 520)
		self.status_delay.resize(170,30)
		self.status_delay.setReadOnly(True)
		self.status_delay.setPlaceholderText("Unknown")

		self.set_all_indicator_buttons("Unknown", "background-color: gray")

		#disable unused instructions
		self.disable_element(self.launch_code_box)
		self.disable_element(self.limit_switch_slowdown_box)
		self.disable_element(self.angle_limit_switch_slowdown_box)
		self.disable_element(self.opening_profile_angle_delimiter_box)
		self.disable_element(self.total_opening_time_box)
		self.disable_element(self.initial_opening_time_box)
		self.disable_element(self.opening_profile_angle_delimiter_box)
		self.disable_element(self.total_opening_time_box)
		self.disable_element(self.initial_opening_time_box)

		#connect button
		self.connect = QPushButton('Connect', self)
		self.connect.setToolTip('You can only submit after the connection has been successfully established')
		self.connect.resize(80,40)
		self.connect.move(20, 570)
		self.connect.clicked.connect(self.set_connection)

		#submit button
		self.auto_test = QPushButton('Auto Test', self)
		self.auto_test.setToolTip('You can only submit after the connection has been successfully established')
		self.auto_test.resize(80,40)
		self.auto_test.move(200, 570)
		self.auto_test.clicked.connect(self.submit_data)
		self.auto_test.setEnabled(False)

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
				self.receiver.default_velocity_received.connect(self.on_default_velocity_received)
				self.receiver.current_velocity_received.connect(self.on_current_velocity_received)
				self.receiver.conn_lost.connect(self.on_conn_lost)
				self.receiver.start()

			self.connect.setEnabled(False)
			#self.disconnect.setEnabled(True)
			self.auto_test.setEnabled(True)
			self.ignitor.setEnabled(True)
			self.abort.setEnabled(True)
			self.open_valve.setEnabled(True)
			self.close_valve.setEnabled(True)
			
			self.ip_box.setEnabled(False)
			
			self.elapsed_timer = QElapsedTimer()
			self.elapsed_timer.start()
			self.status_timer.timeout.connect(self.on_status_timer)
			self.count = 0
			self.status_timer.start(1)
		except Exception as e:
			self.status_box.appendPlainText("Connection failure:" + str(e))

	def on_status_timer(self):
		self.status_delay.setText(str(self.elapsed_timer.elapsed()).zfill(3))
		
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

		engine_data = "HEAD " + launch_code + " " + burn_duration + " " + ignitor_timing + " " + valve_open_timing + " " + valve_closing_time + " " + \
			limit_switch_slowdown + " " + angle_limit_switch_slowdown + " " + opening_profile_angle_delimiter + " " + total_opening_time + " " + \
			initial_opening_time

		if len(engine_data.split()) != 11:
			self.on_msg_received("Auto test error: need 10 parameters\n")
			return

		try:
			self.send_to_server(engine_data)
		except Exception as e:
			self.status_box.appendPlainText("Problem: " + str(e))
			return
		#self.auto_test.setEnabled(False)
		
	def set_disconnect(self):
		self.on_conn_lost("Disconnected")

	#abort
	def abortion(self):
		self.send_to_server("ABORT")

	#open valve
	def valve_opener(self):
		self.send_to_server("VALVE OPEN")

	#ignition
	def ignition(self):
		self.send_to_server("IGNITE")

	#valve closing
	def valve_closer(self):
		self.send_to_server("VALVE CLOSE")

	def on_msg_received(self, msg):
		self.status_box.appendPlainText(msg)

	def on_limit_state_received(self, switch_open, switch_closed):
		self.elapsed_timer.restart()
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
		self.encoder_position.setText('{:.1f}'.format(value * _DEGREES_PER_ENCODER_COUNT))
			
	def on_ignitor_state_received(self, active):
		if active:
			self.ignitor_indicator.setText("ON")
			self.ignitor_indicator.setStyleSheet("background-color: red")
		else:
			self.ignitor_indicator.setText("OFF")
			self.ignitor_indicator.setStyleSheet("background-color: white")

	def on_default_velocity_received(self, vel):
		self.default_velocity.setText('{:.1f}'.format(vel))

	def on_current_velocity_received(self, vel):
		self.current_velocity.setText('{:.1f}'.format(vel))
		
	def set_all_indicator_buttons(self, msg, color):
		self.close_indicator.setText(msg)
		self.close_indicator.setStyleSheet(color)

		self.open_indicator.setText(msg)
		self.open_indicator.setStyleSheet(color)

		self.ignitor_indicator.setText(msg)
		self.ignitor_indicator.setStyleSheet(color)

	def send_to_server(self, msg):
		msg += ' END\n'
		if self.sock is not None:
			try:
				self.sock.sendall(msg.encode())
			except Exception as e:
				print("Send to server failed: " + str(e))

	def on_conn_lost(self, msg):
		self.status_box.appendPlainText(msg)
		self.set_all_indicator_buttons("Unknown", "background-color: gray")
		self.encoder_position.setText("Unknown")
		self.default_velocity.setText("Unknown")
		self.current_velocity.setText("Unknown")
		
		self.ip_box.setEnabled(True)
		
		if self.sock is not None:
			self.sock.close()
			self.sock = None

		self.connect.setEnabled(True)
		self.disconnect.setEnabled(False)

		self.abort.setEnabled(False)
		self.ignitor.setEnabled(False)
		self.open_valve.setEnabled(False)
		self.close_valve.setEnabled(False)
		self.auto_test.setEnabled(False)

		self.receiver = None

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
