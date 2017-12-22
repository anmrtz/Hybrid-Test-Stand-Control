# Hybrid engine test stand client

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
	nc_valve_state_received = QtCore.pyqtSignal(int)
	vent_valve_state_received = QtCore.pyqtSignal(int)

	def __init__(self, sock):
		QtCore.QThread.__init__(self)
		self.sock = sock
		self.char_stream = ''

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

			self.char_stream += msg

			while True:
				a = re.search(r'\b(END)\b', self.char_stream)
				if a is None:
					break
						
				instruction = self.char_stream[:a.start()]
				self.char_stream = self.char_stream[a.start()+3:]
			
				tokens = instruction.split()
			
				if (tokens[0] == "STATEALL"):
					try:
						switch_open = tokens[1] == "1"
						switch_closed = tokens[2] == "1"
						encoder_val = int(tokens[3])
						ignitor_on = tokens[4] == "1"
						default_velocity = float(tokens[5])
						current_velocity = float(tokens[6])
						vent_valve_open = tokens[7] == '1'
						nc_valve_open = tokens[8] == '1'
						self.limit_state_received.emit(switch_open,switch_closed)
						self.ignitor_state_received.emit(ignitor_on)
						self.encoder_position_received.emit(encoder_val)
						self.default_velocity_received.emit(default_velocity)
						self.current_velocity_received.emit(current_velocity)
						self.vent_valve_state_received.emit(vent_valve_open)
						self.nc_valve_state_received.emit(nc_valve_open)

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
		self.title = 'Hybrid Test Stand Control'

		self.receiver = None
		self.sock = None
		self.status_timer = QTimer()

		#Status message box
		self.status_box = QPlainTextEdit(self)
		self.status_box.setReadOnly(True)
		self.status_box.move(810,58);
		self.status_box.resize(380,600);

		#server connection group
		self.server_connect_group = QGroupBox(self)
		self.server_connect_group.move(10, 40)
		self.server_connect_group.resize(360, 120)
		self.server_connect_group.setTitle("Connect to server")

		#ip address
		self.ip_box = QLineEdit(self.server_connect_group)
		self.ip_box.move(180, 30)
		self.ip_box.resize(170,30)
		self.ip_box.setPlaceholderText("IP address")
		self.ip_box.setText("10.42.0.209")
		#----accompanying label
		self.ip_label = QLabel(self.server_connect_group)
		self.ip_label.setText("IP Address")
		self.ip_label.move(10,30)
		self.ip_label.resize(230,30)

		#connect button
		self.connect_button = QPushButton('Connect', self.server_connect_group)
		self.connect_button.setToolTip('You can only submit after the connection has been successfully established')
		self.connect_button.resize(140,30)
		self.connect_button.move(10, 80)
		self.connect_button.clicked.connect(self.set_connection)

		#ignition sequence group
		self.ignition_sequence_group = QGroupBox(self)
		self.ignition_sequence_group.move(10, 180)
		self.ignition_sequence_group.resize(360, 330)
		self.ignition_sequence_group.setTitle("Automated ignition sequence")

		#Launch code
		self.launch_code_box = QLineEdit(self.ignition_sequence_group)
		self.launch_code_box.move(180, 30)
		self.launch_code_box.resize(170,30)
		self.launch_code_box.setPlaceholderText("Launch code")
		#----only integers are allowed
		int_validator = QtGui.QIntValidator()
		self.launch_code_box.setValidator(int_validator)
		#----accompanying label
		self.launch_label = QLabel(self.ignition_sequence_group)
		self.launch_label.setText("Launch code")
		self.launch_label.move(10,30)
		self.launch_label.resize(230,30)

		#Burn duration
		self.burn_duration_box = QLineEdit(self.ignition_sequence_group)
		self.burn_duration_box.move(180, 80)
		self.burn_duration_box.resize(170,30)
		self.burn_duration_box.setPlaceholderText("Burn duration (s)")
		#----only doubles are allowed
		double_validator = QtGui.QDoubleValidator()
		self.burn_duration_box.setValidator(double_validator)
		#----accompanying label
		self.burn_label = QLabel(self.ignition_sequence_group)
		self.burn_label.setText("Burn duration (s)")
		self.burn_label.move(10,80)
		self.burn_label.resize(230,30)

		#Ignitor timing
		self.ignitor_timing_box = QLineEdit(self.ignition_sequence_group)
		self.ignitor_timing_box.move(180, 130)
		self.ignitor_timing_box.resize(170,30)
		self.ignitor_timing_box.setPlaceholderText("Ignitor delay (s)")
		#----only doubles are allowed
		self.ignitor_timing_box.setValidator(double_validator)
		#----accompanying label
		self.ignitor_button_label = QLabel(self.ignition_sequence_group)
		self.ignitor_button_label.setText("Ignitor delay (s)")
		self.ignitor_button_label.move(10,130)
		self.ignitor_button_label.resize(230,30)

		#Valve open timing
		self.valve_open_timing_box = QLineEdit(self.ignition_sequence_group)
		self.valve_open_timing_box.move(180, 180)
		self.valve_open_timing_box.resize(170,30)
		self.valve_open_timing_box.setPlaceholderText("Valve opening time (s)")
		#----only doubles are allowed
		self.valve_open_timing_box.setValidator(double_validator)
		#----accompanying label
		self.valve_open_label = QLabel(self.ignition_sequence_group)
		self.valve_open_label.setText("Valve opening (s)")
		self.valve_open_label.move(10,180)
		self.valve_open_label.resize(230,30)

		#Valve closing time
		self.valve_closing_time_box = QLineEdit(self.ignition_sequence_group)
		self.valve_closing_time_box.move(180, 230)
		self.valve_closing_time_box.resize(170,30)
		self.valve_closing_time_box.setPlaceholderText("Valve closing time (s)")
		#----only doubles are allowed
		self.valve_closing_time_box.setValidator(double_validator)
		#----accompanying label
		self.valve_close_label = QLabel(self.ignition_sequence_group)
		self.valve_close_label.setText("Valve closing (s)")
		self.valve_close_label.move(10,230)
		self.valve_close_label.resize(230,30)

		#start ignition sequence button
		self.auto_test_button = QPushButton('Start sequence', self.ignition_sequence_group)
		self.auto_test_button.setToolTip('You can only submit after the connection has been successfully established')
		self.auto_test_button.resize(140,30)
		self.auto_test_button.move(10, 280)
		self.auto_test_button.clicked.connect(self.send_auto_test_params)
		self.auto_test_button.setEnabled(False)

		#server status group
		self.server_status_group = QGroupBox(self)
		self.server_status_group.move(400, 40)
		self.server_status_group.resize(380, 520)
		self.server_status_group.setTitle("System status")

		#Close limit switch indicator
		self.mev_close_limit_indicator_label = QLabel(self.server_status_group)
		self.mev_close_limit_indicator_label.setText("Close limit switch")
		self.mev_close_limit_indicator_label.move(10,30)
		self.mev_close_limit_indicator = QPushButton(self.server_status_group)
		self.mev_close_limit_indicator.move(200,30)
		self.mev_close_limit_indicator.resize(170,30)
		self.mev_close_limit_indicator.setEnabled(False)

		#Open limit switch indicator
		self.mev_open_limit_indicator_label = QLabel(self.server_status_group)
		self.mev_open_limit_indicator_label.setText("Open limit switch")
		self.mev_open_limit_indicator_label.move(10,80)
		self.mev_open_limit_indicator = QPushButton(self.server_status_group)
		self.mev_open_limit_indicator.move(200,80)
		self.mev_open_limit_indicator.resize(170,30)
		self.mev_open_limit_indicator.setEnabled(False)

		#ignitor indicator
		self.ignitor_button_indicator = QPushButton(self.server_status_group)
		self.ignitor_button_indicator.move(200,230)
		self.ignitor_button_indicator.resize(170,30)
		self.ignitor_button_indicator.setEnabled(False)
		self.ignitor_button_indicator_label = QLabel(self.server_status_group)
		self.ignitor_button_indicator_label.setText("Ignitor status")
		self.ignitor_button_indicator_label.move(10,230)

		#vent valve indicator
		self.vent_valve_button_indicator = QPushButton(self.server_status_group)
		self.vent_valve_button_indicator.move(200,130)
		self.vent_valve_button_indicator.resize(170,30)
		self.vent_valve_button_indicator.setEnabled(False)
		self.vent_valve_button_indicator_label = QLabel(self.server_status_group)
		self.vent_valve_button_indicator_label.setText("Vent valve status")
		self.vent_valve_button_indicator_label.move(10,130)
		self.vent_valve_button_indicator_label.resize(170,30)
		
		#nc valve indicator
		self.nc_valve_button_indicator = QPushButton(self.server_status_group)
		self.nc_valve_button_indicator.move(200,180)
		self.nc_valve_button_indicator.resize(170,30)
		self.nc_valve_button_indicator.setEnabled(False)
		self.nc_valve_button_indicator_label = QLabel(self.server_status_group)
		self.nc_valve_button_indicator_label.setText("NC valve status")
		self.nc_valve_button_indicator_label.move(10,180)

		#encoder position
		self.encoder_position_label = QLabel(self.server_status_group)
		self.encoder_position_label.setText("Encoder pos. (deg)")
		self.encoder_position_label.move(10,280)
		self.encoder_position_label.resize(230,30)
		self.encoder_position = QLineEdit(self.server_status_group)
		self.encoder_position.move(200, 280)
		self.encoder_position.resize(170,30)
		self.encoder_position.setReadOnly(True)
		self.encoder_position.setPlaceholderText("Unknown")

		#current motor velocity
		self.current_velocity_label = QLabel(self.server_status_group)
		self.current_velocity_label.setText("Current vel. (deg/s)")
		self.current_velocity_label.move(10,330)
		self.current_velocity_label.resize(230,30)
		self.current_velocity = QLineEdit(self.server_status_group)
		self.current_velocity.move(200, 330)
		self.current_velocity.resize(170,30)
		self.current_velocity.setReadOnly(True)
		self.current_velocity.setPlaceholderText("Unknown")

		#motor default velocity
		self.default_velocity_label = QLabel(self.server_status_group)
		self.default_velocity_label.setText("Default vel. (deg/s)")
		self.default_velocity_label.move(10,380)
		self.default_velocity_label.resize(230,30)
		self.default_velocity = QLineEdit(self.server_status_group)
		self.default_velocity.move(200, 380)
		self.default_velocity.resize(170,30)
		self.default_velocity.setReadOnly(True)
		self.default_velocity.setPlaceholderText("Unknown")
		
		#time since last status update from server
		self.status_delay_label = QLabel(self.server_status_group)
		self.status_delay_label.setWordWrap(True)
		self.status_delay_label.setText("Last update (ms)")
		self.status_delay_label.move(10,480)
		self.status_delay_label.resize(230,30)
		self.status_delay = QLineEdit(self.server_status_group)
		self.status_delay.move(200, 480)
		self.status_delay.resize(170,30)
		self.status_delay.setReadOnly(True)
		self.status_delay.setPlaceholderText("Unknown")

		#Set default velocity button
		self.set_default_vel_button = QPushButton('Set default vel.', self.server_status_group)
		self.set_default_vel_button.move(10,430)
		self.set_default_vel_button.resize(140,30)
		self.set_default_vel_button.clicked.connect(self.send_new_default_vel)
		self.set_default_vel_button.setEnabled(False)
		#Set default velocity entry box
		self.default_vel_entry = QLineEdit(self.server_status_group)
		self.default_vel_entry.move(200, 430)
		self.default_vel_entry.resize(170,30)
		self.default_vel_entry.setPlaceholderText("Default vel. (deg/s)")

		#manual control group
		self.manual_control_group = QGroupBox(self)
		self.manual_control_group.move(10, 530)
		self.manual_control_group.resize(340, 130)
		self.manual_control_group.setTitle("Manual control")

		#ABORT button
		self.abort_button = QPushButton('Abort', self.manual_control_group)
		self.abort_button.resize(100,40)
		self.abort_button.move(230,80)
		self.abort_button.clicked.connect(self.send_abort)
		self.abort_button.setEnabled(False)
		self.abort_button.setStyleSheet("background-color: red")

		#TEST IGNITOR button
		self.ignitor_button = QPushButton('Toggle\n Ignitor', self.manual_control_group)
		self.ignitor_button.resize(100,40)
		self.ignitor_button.move(230,30)
		self.ignitor_button.clicked.connect(self.send_toggle_ignitor)
		self.ignitor_button.setEnabled(False)

		#OPEN VALVE button
		self.mev_open_button = QPushButton('Open MEV', self.manual_control_group)
		self.mev_open_button.resize(100,40)
		self.mev_open_button.move(10,30)
		self.mev_open_button.clicked.connect(self.send_mev_open)
		self.mev_open_button.setEnabled(False)

		#CLOSE VALVE button
		self.mev_close_button = QPushButton('Close MEV', self.manual_control_group)
		self.mev_close_button.resize(100,40)
		self.mev_close_button.move(10,80)
		self.mev_close_button.clicked.connect(self.send_mev_close)
		self.mev_close_button.setEnabled(False)

		#TEST Vent valve button
		self.vent_valve_button = QPushButton('Toggle\n Vent Valve', self.manual_control_group)
		self.vent_valve_button.resize(100,40)
		self.vent_valve_button.move(120,30)
		self.vent_valve_button.clicked.connect(self.send_toggle_vent_valve)
		self.vent_valve_button.setEnabled(False)

		#TEST NC valve button
		self.nc_valve_button = QPushButton('Toggle\n NC Valve', self.manual_control_group)
		self.nc_valve_button.resize(100,40)
		self.nc_valve_button.move(120,80)
		self.nc_valve_button.clicked.connect(self.send_toggle_nc_valve)
		self.nc_valve_button.setEnabled(False)

		self.set_all_indicator_buttons("Unknown", "background-color: gray")

		#disable unused instructions
		self.disable_element(self.launch_code_box)

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
				self.receiver.vent_valve_state_received.connect(self.on_vent_valve_state_received)
				self.receiver.nc_valve_state_received.connect(self.on_nc_valve_state_received)
				self.receiver.start()

			self.connect_button.setEnabled(False)
			self.auto_test_button.setEnabled(True)
			self.ignitor_button.setEnabled(True)
			self.abort_button.setEnabled(True)
			self.mev_open_button.setEnabled(True)
			self.mev_close_button.setEnabled(True)
			self.nc_valve_button.setEnabled(True)
			self.vent_valve_button.setEnabled(True)
			self.set_default_vel_button.setEnabled(True)
			
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
	def send_auto_test_params(self):
				#Collecting all of the variables from the textboxes
		launch_code = self.launch_code_box.text()
		burn_duration = self.burn_duration_box.text()
		ignitor_timing = self.ignitor_timing_box.text()
		valve_open_timing = self.valve_open_timing_box.text()
		valve_closing_time = self.valve_closing_time_box.text()

		auto_test_params = "AUTO_TEST_PARAMS " + launch_code + " " + burn_duration + " " + ignitor_timing + " " + valve_open_timing + " " + valve_closing_time
		if len(auto_test_params.split()) != 6:
			self.on_msg_received("Auto test error: need 5 parameters\n")
			return

		try:
			self.send_to_server(auto_test_params)
		except Exception as e:
			self.status_box.appendPlainText("Problem: " + str(e))
			return
		#self.auto_test_button.setEnabled(False)
		
	def set_disconnect(self):
		self.on_conn_lost("Disconnected")

	#abort
	def send_abort(self):
		self.send_to_server("ABORT")

	def send_toggle_vent_valve(self):
		self.send_to_server("VENT_VALVE")
		
	def send_toggle_nc_valve(self):
		self.send_to_server("NC_VALVE")
		
	def send_new_default_vel(self):
		new_default_vel = self.default_vel_entry.text()
		try:
			int(new_default_vel)
		except:
			self.on_msg_received("Set default velocity error: invalid integer\n")
			return			
		self.send_to_server("DEFAULT_VEL " + new_default_vel)

	#open valve
	def send_mev_open(self):
		self.send_to_server("MEV OPEN")

	#ignition
	def send_toggle_ignitor(self):
		self.send_to_server("IGNITOR")

	#valve closing
	def send_mev_close(self):
		self.send_to_server("MEV CLOSE")

	def on_msg_received(self, msg):
		self.status_box.appendPlainText(msg)

	def on_limit_state_received(self, switch_open, switch_closed):
		self.elapsed_timer.restart()
		if switch_open:
			self.mev_open_limit_indicator.setText("FULLY OPEN")
			self.mev_open_limit_indicator.setStyleSheet("background-color: green")
		else:
			self.mev_open_limit_indicator.setText("")
			self.mev_open_limit_indicator.setStyleSheet("background-color: white")
		if switch_closed:
			self.mev_close_limit_indicator.setText("FULLY CLOSED")
			self.mev_close_limit_indicator.setStyleSheet("background-color: green")
		else:
			self.mev_close_limit_indicator.setText("")
			self.mev_close_limit_indicator.setStyleSheet("background-color: white")

	def on_encoder_position_received(self, value):
		self.encoder_position.setText('{:.1f}'.format(value * _DEGREES_PER_ENCODER_COUNT))
			
	def on_ignitor_state_received(self, active):
		if active:
			self.ignitor_button_indicator.setText("ON")
			self.ignitor_button_indicator.setStyleSheet("background-color: red")
		else:
			self.ignitor_button_indicator.setText("OFF")
			self.ignitor_button_indicator.setStyleSheet("background-color: white")

	def on_vent_valve_state_received(self, active):
		if active:
			self.vent_valve_button_indicator.setText("ON")
			self.vent_valve_button_indicator.setStyleSheet("background-color: red")
		else:
			self.vent_valve_button_indicator.setText("OFF")
			self.vent_valve_button_indicator.setStyleSheet("background-color: white")

	def on_nc_valve_state_received(self, active):
		if active:
			self.nc_valve_button_indicator.setText("ON")
			self.nc_valve_button_indicator.setStyleSheet("background-color: red")
		else:
			self.nc_valve_button_indicator.setText("OFF")
			self.nc_valve_button_indicator.setStyleSheet("background-color: white")

	def on_default_velocity_received(self, vel):
		self.default_velocity.setText('{:.1f}'.format(vel))

	def on_current_velocity_received(self, vel):
		self.current_velocity.setText('{:.1f}'.format(vel))
		
	def set_all_indicator_buttons(self, msg, color):
		self.mev_close_limit_indicator.setText(msg)
		self.mev_close_limit_indicator.setStyleSheet(color)

		self.mev_open_limit_indicator.setText(msg)
		self.mev_open_limit_indicator.setStyleSheet(color)

		self.ignitor_button_indicator.setText(msg)
		self.ignitor_button_indicator.setStyleSheet(color)

		self.vent_valve_button_indicator.setText(msg)
		self.vent_valve_button_indicator.setStyleSheet(color)

		self.nc_valve_button_indicator.setText(msg)
		self.nc_valve_button_indicator.setStyleSheet(color)

	def send_to_server(self, msg):
		msg += ' END\n'
		if self.sock is not None:
			try:
				self.sock.sendall(msg.encode())
			except Exception as e:
				print("Send to server failed: " + str(e))

	def on_conn_lost(self, msg = ""):
		self.status_box.appendPlainText(msg)
		self.set_all_indicator_buttons("Unknown", "background-color: gray")
		self.encoder_position.setText("Unknown")
		self.default_velocity.setText("Unknown")
		self.current_velocity.setText("Unknown")
		
		
		self.ip_box.setEnabled(True)
		
		if self.sock is not None:
			self.sock.close()
			self.sock = None

		self.connect_button.setEnabled(True)
		self.abort_button.setEnabled(False)
		self.ignitor_button.setEnabled(False)
		self.mev_open_button.setEnabled(False)
		self.mev_close_button.setEnabled(False)
		self.auto_test_button.setEnabled(False)
		self.nc_valve_button.setEnabled(False)
		self.vent_valve_button.setEnabled(False)
		self.set_default_vel_button.setEnabled(False)

		self.receiver = None

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
