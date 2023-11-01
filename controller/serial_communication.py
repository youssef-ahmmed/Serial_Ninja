import time

import serial
import serial.tools.list_ports
from serial.serialutil import SerialException, SerialTimeoutException

import strings
from controller.log_controller import LogController
from controller.setting_controller import SettingController


class SerialCommunication:
    serial_port = serial.Serial()

    def __init__(self):
        SerialCommunication.initiate_communication()

    @staticmethod
    def initiate_communication():
        if not SerialCommunication.serial_port.is_open:
            SerialCommunication.get_default_data()
            SerialCommunication.serial_port.open()
        else:
            SerialCommunication.get_setting_data()

    def execute_serial_transaction(self, data):
        try:
            self.send_data(data)
            LogController.get_instance().log_success(strings.SEND_SUCCESS)
        except Exception as e:
            LogController.get_instance().log_error(strings.PORT_NOT_OPEN_ERROR)

    def execute_serial_receiving(self):
        try:
            data = self.read_data()
            LogController.get_instance().log_success(strings.RECEIVE_SUCCESS)
            LogController.get_instance().log_info(f"Data Received: {data}")
        except Exception as e:
            LogController.get_instance().log_error(strings.PORT_NOT_OPEN_ERROR)

    @staticmethod
    def get_default_data():
        SerialCommunication.serial_port.port = 'COM1'
        SerialCommunication.serial_port.baudrate = int(9600)
        SerialCommunication.serial_port.bytesize = int(8)
        SerialCommunication.serial_port.parity = 'N'
        SerialCommunication.serial_port.stopbits = int(1)
        SerialCommunication.serial_port.timeout = int(0)

    @staticmethod
    def get_setting_data():
        setting_data = SettingController.get_instance().get_port_configuration_data()
        # SerialCommunication.serial_port.port = setting_data[0]                 #DON'T TOUCH
        SerialCommunication.serial_port.baudrate = int(setting_data[1])
        SerialCommunication.serial_port.bytesize = int(setting_data[2])
        SerialCommunication.serial_port.parity = setting_data[3]
        SerialCommunication.serial_port.stopbits = int(setting_data[4])
        SerialCommunication.serial_port.timeout = int(setting_data[5])
        flow_control = setting_data[6]
        if flow_control == "Xon/Xoff":
            SerialCommunication.serial_port.xonxoff = True
        elif flow_control == "RTS/CTS":
            SerialCommunication.serial_port.rtscts = True
        elif flow_control == "DSR/DTR":
            SerialCommunication.serial_port.dsrdtr = True

    def send_data(self, data):
        try:
            if not SerialCommunication.serial_port.is_open:
                LogController.get_instance().log_error(strings.PORT_NOT_OPEN_ERROR)
                return False
            else:
                for char in data:
                    SerialCommunication.serial_port.write(char.encode())
                    time.sleep(0.01)
        except SerialTimeoutException as e:
            LogController.get_instance().log_error(strings.TIMEOUT_ERROR)
            raise e
        except SerialException as e:
            LogController.get_instance().log_error(strings.CONFIGURATION_ERROR)
            raise e

    def read_data(self):
        try:
            received_data = SerialCommunication.serial_port.readline().decode('utf-8')
            return received_data
        except SerialTimeoutException as e:
            LogController.get_instance().log_error(strings.TIMEOUT_ERROR)
            raise e
        except SerialException as e:
            LogController.get_instance().log_error(strings.CONFIGURATION_ERROR)
            raise e
