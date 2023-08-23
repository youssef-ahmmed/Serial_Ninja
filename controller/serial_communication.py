import serial
import serial.tools.list_ports
from serial.serialutil import SerialException, SerialTimeoutException

import strings
from controller.log_controller import LogController
from controller.setting_controller import SettingController


class SerialCommunication:
    def __init__(self, data):
        self.serial_port = serial.Serial()

        self.get_setting_data()
        self.send_data(data)
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
            for char in data:
                self.serial_port.write(char.encode())
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
