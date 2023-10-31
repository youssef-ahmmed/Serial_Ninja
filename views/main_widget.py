import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QHBoxLayout

from controller.log_controller import LogController
from controller.password_controller import PasswordController
from controller.receive_button_contoller import ReceiveButtonController
from controller.send_button_controller import SendButtonController
from views.button import RoundButton
from views.log import LogWidget
from views.password import PasswordEntry
from views.toolbar import Toolbar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Ninja")
        self.setGeometry(200, 200, 500, 400)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color: #F5F5F5;")
        self.setWindowIcon(QIcon("assets/ninja-logo.ico"))

        self.init_ui()
        self.center_on_screen()

    def start_communication(self):
        self.receive_button.clicked.connect(self.disable_password_entry)
        self.send_button.clicked.connect(self.enable_password_entry)

    def init_ui(self):
        layout = QVBoxLayout(self.central_widget)

        horizontal_spacer = QHBoxLayout()
        horizontal_spacer.addStretch(1)

        sub_layout = QVBoxLayout()
        sub_layout.setAlignment(Qt.AlignCenter)

        toolbar = Toolbar(self)

        self.password_entry = PasswordEntry(self)
        PasswordController(self.password_entry)
        self.password_entry.setFixedHeight(100)
        self.password_entry.setFixedWidth(200)

        self.send_button = RoundButton("Send")
        self.receive_button = RoundButton("Receive")
        SendButtonController(self.send_button)
        self.receive_button_controller = ReceiveButtonController(self.receive_button)
        self.send_button.setFixedSize(190, 40)
        self.receive_button.setFixedSize(190, 40)

        sub_layout.addWidget(self.password_entry)
        sub_layout.addWidget(self.send_button)
        sub_layout.addWidget(self.receive_button)

        horizontal_spacer.addLayout(sub_layout)
        horizontal_spacer.addStretch(1)

        log_widget = LogWidget(self)
        LogController(log_widget)

        layout.addWidget(toolbar)
        layout.addLayout(horizontal_spacer)
        layout.addWidget(log_widget)

        self.central_widget.setLayout(layout)

    def center_on_screen(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        self.move(int((screen_geometry.width() - self.width()) / 2),
                  int((screen_geometry.height() - self.height()) / 2))

    def disable_password_entry(self):
        self.password_entry.setEnabled(False)
        self.password_entry.set_text(self.receive_button_controller.receive_data())

    def enable_password_entry(self):
        self.password_entry.setEnabled(True)
        self.password_entry.clear_text()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
