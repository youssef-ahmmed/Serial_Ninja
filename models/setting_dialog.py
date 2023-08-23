from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, \
    QPushButton, QVBoxLayout, QFormLayout, QWidget, QHBoxLayout, QSizePolicy, QLineEdit, QMessageBox

import strings


class SerialSettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.port_configurations = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Serial Settings")
        self.setGeometry(100, 100, 400, 300)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.settings_widget = QWidget()
        self.form_layout = QFormLayout(self.settings_widget)
        self.settings_widget.hide()

        self.protocol_layout = QHBoxLayout()
        self.protocol_label = QLabel("Communication Protocol:")
        self.protocol_combo = QComboBox()
        self.protocol_combo.addItems(strings.COMMUNICATION_PROTOCOLS)
        self.protocol_combo.currentIndexChanged.connect(self.update_settings)

        self.protocol_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.protocol_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.protocol_layout.addWidget(self.protocol_label)
        self.protocol_layout.addWidget(self.protocol_combo)

        self.cancel_button = QPushButton("Cancel")
        self.save_button = QPushButton("Save")

    def create_uart_settings(self):
        self.clear_layout(self.form_layout)

        self.port_number_label = QLabel("Port Number")
        self.port_edit = QLineEdit()
        self.port_edit.setPlaceholderText("Enter port name")
        self.port_edit.textChanged.connect(self.clear_error_style)

        self.baudrate_label = QLabel("Baudrate")
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItems(strings.BAUD_RATE)
        self.baudrate_combo.setEditable(True)

        self.data_bits_label = QLabel("Data Bits")
        self.data_bits_combo = QComboBox()
        self.data_bits_combo.addItems(["8", "7", "6", "5"])

        self.parity_label = QLabel("Parity")
        self.parity_combo = QComboBox()
        self.parity_combo.addItems(["N", "E", "O"])

        self.stop_bits_label = QLabel("Stop Bits")
        self.stop_bits_combo = QComboBox()
        self.stop_bits_combo.addItems(["1", "2"])

        self.flow_control_label = QLabel("Flow Control")
        self.flow_control_combo = QComboBox()
        self.flow_control_combo.addItems(strings.FLOW_CONTROL)

        self.time_out_label = QLabel("Timeout")
        self.time_out_edit = QLineEdit()
        self.time_out_edit.setPlaceholderText("Enter timeout")
        self.time_out_edit.textChanged.connect(self.clear_error_style)

        self.form_layout.addRow(self.port_number_label, self.port_edit)
        self.form_layout.addRow(self.baudrate_label, self.baudrate_combo)
        self.form_layout.addRow(self.data_bits_label, self.data_bits_combo)
        self.form_layout.addRow(self.parity_label, self.parity_combo)
        self.form_layout.addRow(self.stop_bits_label, self.stop_bits_combo)
        self.form_layout.addRow(self.time_out_label, self.time_out_edit)
        self.form_layout.addRow(self.flow_control_label, self.flow_control_combo)

        self.settings_widget.show()

    def create_layout(self):
        layout = QVBoxLayout()

        layout.addLayout(self.protocol_layout)

        layout.addWidget(self.settings_widget)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def update_settings(self):
        selected_protocol = self.protocol_combo.currentText()

        if selected_protocol == "UART":
            self.create_uart_settings()
        else:
            self.settings_widget.hide()

    @staticmethod
    def clear_layout(layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def show_protocol_selection_error(self):
        self.error_dialog = QMessageBox()
        self.error_dialog.setIcon(QMessageBox.Warning)
        self.error_dialog.setWindowTitle("Error")
        self.error_dialog.setText("Please select a communication protocol")
        self.error_dialog.setStandardButtons(QMessageBox.Ok)
        self.error_dialog.exec_()

    def set_error_style_port(self):
        error_style = "border: 1px solid red;"
        self.port_edit.setStyleSheet(error_style)

    def set_error_style_time_out(self):
        error_style = "border: 1px solid red;"
        self.time_out_edit.setStyleSheet(error_style)

    def clear_error_style(self):
        self.port_edit.setStyleSheet("")
        self.time_out_edit.setStyleSheet("")
