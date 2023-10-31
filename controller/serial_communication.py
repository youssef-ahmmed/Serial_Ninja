import time

import serial
import serial.tools.list_ports
from serial.serialutil import SerialException, SerialTimeoutException

import strings
from controller.log_controller import LogController
from controller.setting_controller import SettingController


class SerialCommunication:
    def __init__(self):
        self.serial_port = serial.Serial()

    def execute_serial_transaction(self, data):
        try:
            self.get_setting_data()
            self.serial_port.open()
            self.send_data(data)
            LogController.get_instance().log_success(strings.SEND_SUCCESS)
        except Exception as e:
            LogController.get_instance().log_error(strings.PORT_NOT_OPEN_ERROR)
        finally:
            self.close_serial_port()

    def execute_serial_receiving(self):
        try:
            self.get_setting_data()
            self.serial_port.open()
            LogController.get_instance().log_success(strings.RECEIVE_SUCCESS)
            LogController.get_instance().log_info(f"Data Received: {self.read_data()}")
        except Exception as e:
            LogController.get_instance().log_error(strings.PORT_NOT_OPEN_ERROR)
        finally:
            self.close_serial_port()

    def get_setting_data(self):
        setting_data = SettingController.get_instance().get_port_configuration_data()
        self.serial_port.port = setting_data[0]
        self.serial_port.baudrate = int(setting_data[1])
        self.serial_port.bytesize = int(setting_data[2])
        self.serial_port.parity = setting_data[3]
        self.serial_port.stopbits = int(setting_data[4])
        self.serial_port.timeout = int(setting_data[5])
        flow_control = setting_data[6]
        if flow_control == "Xon/Xoff":
            self.serial_port.xonxoff = True
        elif flow_control == "RTS/CTS":
            self.serial_port.rtscts = True
        elif flow_control == "DSR/DTR":
            self.serial_port.dsrdtr = True

    def send_data(self, data):
        try:
            if not self.serial_port.is_open:
                LogController.get_instance().log_error(strings.PORT_NOT_OPEN_ERROR)
                return False
            else:
                for char in data:
                    self.serial_port.write(char.encode())
                    time.sleep(0.01)
        except SerialTimeoutException as e:
            LogController.get_instance().log_error(strings.TIMEOUT_ERROR)
            raise e
        except SerialException as e:
            LogController.get_instance().log_error(strings.CONFIGURATION_ERROR)
            raise e

    def read_data(self):
        try:
            return self.serial_port.readline().decode()
        except SerialTimeoutException as e:
            raise e
        except SerialException as e:
            raise e

    def close_serial_port(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
