from datetime import datetime

import strings
from controller.log_controller import LogController
from controller.password_controller import PasswordController
from controller.serial_communication import SerialCommunication
from controller.setting_controller import SettingController
from models.engine.file_storage import FileStorage


class SendButtonController:
    _instance = None

    @staticmethod
    def get_instance():
        if SendButtonController._instance is None:
            raise Exception("No object was created")
        return SendButtonController._instance

    def __init__(self, send_button):
        if SendButtonController._instance is None:
            super(SendButtonController, self).__init__()
            SendButtonController._instance = self
            self.send_button = send_button
        else:
            raise Exception(strings.SINGLETON_ERROR)

        self.start_communication()

    def start_communication(self):
        self.send_button.clicked.connect(self.send_data)

    def send_data(self):
        if not SettingController.get_instance().validate_selected_protocol():
            self.save_to_file()
            return

        password = PasswordController.get_instance().get_password()
        send_serial = SerialCommunication()
        send_serial.execute_serial_transaction(password)
        self.save_to_file()

    def save_to_file(self):
        file_storage = FileStorage()
        log_dict = {"status": LogController.get_instance().get_log_status(),
                    "password": PasswordController.get_instance().get_password(),
                    "port_configuration": SettingController.get_instance().get_port_configuration_data(),
                    "time_stamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), "encryption_mode": False}
        file_storage.new(log_dict)
        file_storage.save()
