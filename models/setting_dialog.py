import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QComboBox, \
    QPushButton, QVBoxLayout, QFormLayout, QWidget, QHBoxLayout, QSizePolicy

BAUD_RATE = ['110', '300', '600', '1200', '2400', '4800', '9600', '14400',
             '19200', '38400', '57600', '115200', '128000', '256000']

COMMUNICATION_PROTOCOLS = ["Select Protocol", "UART", "SPI", "I2C", "CAN"]

FLOW_CONTROL = ["None", "Xon/Xoff", "RTS/CTS", "DSR/DTR"]


class SerialSettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Serial Settings")
        self.setGeometry(100, 100, 400, 300)

        self.create_widgets()
        self.start_communication()
        self.create_layout()

    def create_widgets(self):
        self.settings_widget = QWidget()
        self.form_layout = QFormLayout(self.settings_widget)
        self.settings_widget.hide()

        self.protocol_layout = QHBoxLayout()
        self.protocol_label = QLabel("Communication Protocol:")
        self.protocol_combo = QComboBox()
        self.protocol_combo.addItems(COMMUNICATION_PROTOCOLS)
        self.protocol_combo.currentIndexChanged.connect(self.update_settings)

        self.protocol_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.protocol_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.protocol_layout.addWidget(self.protocol_label)
        self.protocol_layout.addWidget(self.protocol_combo)

        self.cancel_button = QPushButton("Cancel")
        self.save_button = QPushButton("Save")

    def start_communication(self):
        self.cancel_button.clicked.connect(self.reject)
        self.save_button.clicked.connect(self.save_settings)

    def create_uart_settings(self):
        self.clear_layout(self.form_layout)

        self.baudrate_label = QLabel("Baudrate:")
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItems(BAUD_RATE)
        self.baudrate_combo.setEditable(True)

        self.data_bits_label = QLabel("Data Bits:")
        self.data_bits_combo = QComboBox()
        self.data_bits_combo.addItems(["8", "7", "6", "5"])

        self.parity_label = QLabel("Parity:")
        self.parity_combo = QComboBox()
        self.parity_combo.addItems(["None", "Even", "Odd"])

        self.stop_bits_label = QLabel("Stop Bits:")
        self.stop_bits_combo = QComboBox()
        self.stop_bits_combo.addItems(["1", "2"])

        self.flow_control_label = QLabel("Flow Control:")
        self.flow_control_combo = QComboBox()
        self.flow_control_combo.addItems(FLOW_CONTROL)

        self.form_layout.addRow(self.baudrate_label, self.baudrate_combo)
        self.form_layout.addRow(self.data_bits_label, self.data_bits_combo)
        self.form_layout.addRow(self.parity_label, self.parity_combo)
        self.form_layout.addRow(self.stop_bits_label, self.stop_bits_combo)
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

    def save_settings(self):
        selected_protocol = self.protocol_combo.currentText()

        if selected_protocol == "UART":
            baudrate = self.baudrate_combo.currentText()
            data_bits = self.data_bits_combo.currentText()
            parity = self.parity_combo.currentText()
            stop_bits = self.stop_bits_combo.currentText()

        self.accept()
