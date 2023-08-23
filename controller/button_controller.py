from datetime import datetime

import strings
from controller.log_controller import LogController
from controller.password_controller import PasswordController
from controller.serial_communication import SerialCommunication
from controller.setting_controller import SettingController
from models.engine.file_storage import FileStorage


class ButtonController:
    _instance = None

    @staticmethod
    def get_instance():
        if ButtonController._instance is None:
            raise Exception("No object was created")
        return ButtonController._instance

    def __init__(self, round_button):
        if ButtonController._instance is None:
            super(ButtonController, self).__init__()
            ButtonController._instance = self
            self.round_button = round_button
        else:
            raise Exception(strings.SINGLETON_ERROR)

        self.start_communication()

    def start_communication(self):
        self.round_button.clicked.connect(self.send_data)

    def send_data(self):
        if not SettingController.get_instance().validate_selected_protocol():
            self.save_to_file()
            return
        if not PasswordController.get_instance().validate_password():
            self.save_to_file()
            return

        password = PasswordController.get_instance().get_password()
        SerialCommunication(password)
        LogController.get_instance().log_success(strings.SEND_SUCCESS)
        self.save_to_file()

    def save_to_file(self):
        file_storage = FileStorage()
        log_dict = {"status": LogController.get_instance().get_log_status(),
                    "password": PasswordController.get_instance().get_password(),
                    "port_configuration": SettingController.get_instance().get_port_configuration_data(),
                    "time_stamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), "encryption_mode": False}
        file_storage.new(log_dict)
        file_storage.save()
