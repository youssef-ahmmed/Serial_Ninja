from datetime import datetime

import strings
from controller.log_controller import LogController
from controller.password_controller import PasswordController
from controller.serial_communication import SerialCommunication
from controller.setting_controller import SettingController
from models.engine.file_storage import FileStorage


class ReceiveButtonController:
    _instance = None

    @staticmethod
    def get_instance():
        if ReceiveButtonController._instance is None:
            raise Exception("No object was created")
        return ReceiveButtonController._instance

    def __init__(self, receive_button):
        if ReceiveButtonController._instance is None:
            super(ReceiveButtonController, self).__init__()
            ReceiveButtonController._instance = self
            self.receive_button = receive_button
            self.receive_serial = SerialCommunication()

        else:
            raise Exception(strings.SINGLETON_ERROR)

        self.start_communication()

    def start_communication(self):
        self.receive_button.clicked.connect(self.receive_data)

    def receive_data(self):
        if not SettingController.get_instance().validate_selected_protocol():
            self.save_to_file()
            return

        self.save_to_file()
        self.receive_serial.initiate_communication()
        self.receive_serial.execute_serial_receiving()

    def save_to_file(self):
        file_storage = FileStorage()
        log_dict = {"status": LogController.get_instance().get_log_status(),
                    "password": PasswordController.get_instance().get_password(),
                    "port_configuration": SettingController.get_instance().get_port_configuration_data(),
                    "time_stamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), "encryption_mode": False}
        file_storage.new(log_dict)
        file_storage.save()
