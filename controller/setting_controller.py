import strings
from controller.log_controller import LogController


class SettingController:

    _instance = None

    @staticmethod
    def get_instance():
        if SettingController._instance is None:
            raise Exception("No object was created")
        return SettingController._instance

    def __init__(self, setting_dialog):
        if SettingController._instance is None:
            super(SettingController, self).__init__()
            SettingController._instance = self
            self.setting_dialog = setting_dialog
        else:
            raise Exception(strings.SINGLETON_ERROR)

        self.port_configurations = []
        self.start_communication()

    def start_communication(self):
        self.setting_dialog.cancel_button.clicked.connect(self.setting_dialog.reject)
        self.setting_dialog.save_button.clicked.connect(self.save_settings)

    def get_communication_protocol(self):
        return self.setting_dialog.protocol_combo.currentText()

    def validate_selected_protocol(self):
        if self.get_communication_protocol() == "Select Protocol":
            LogController.get_instance().log_error(strings.SETTING_ERROR)
            return False
        return True

    def save_settings(self):
        selected_protocol = self.get_communication_protocol()

        if selected_protocol == "Select Protocol":
            self.setting_dialog.show_protocol_selection_error()
        elif selected_protocol == "UART":
            self.port_configurations = self.collect_uart_settings()
            if self.port_configurations is not None:
                self.setting_dialog.accept()

    def get_port_configuration_data(self):
        return self.port_configurations

    def collect_uart_settings(self):
        port_name = self.setting_dialog.port_edit.text()
        baudrate = self.setting_dialog.baudrate_combo.currentText()
        data_bits = self.setting_dialog.data_bits_combo.currentText()
        parity = self.setting_dialog.parity_combo.currentText()
        stop_bits = self.setting_dialog.stop_bits_combo.currentText()
        time_out = self.setting_dialog.time_out_edit.text()
        flow_control = self.setting_dialog.flow_control_combo.currentText()

        if not port_name:
            self.setting_dialog.set_error_style_port()
            return None
        if not time_out:
            self.setting_dialog.set_error_style_time_out()
            return None

        return [port_name, baudrate, data_bits, parity, stop_bits, time_out, flow_control]
