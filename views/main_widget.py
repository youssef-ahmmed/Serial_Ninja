import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from views.button import RoundButton
from views.button_controller import ButtonController
from controller.log_controller import LogController
from controller.password_controller import PasswordController
from views.log import LogWidget
from views.toolbar import Toolbar
from views.password import PasswordEntry


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

    def init_ui(self):
        layout = QVBoxLayout(self.central_widget)

        horizontal_spacer = QHBoxLayout()
        horizontal_spacer.addStretch(1)

        sub_layout = QVBoxLayout()
        sub_layout.setAlignment(Qt.AlignCenter)

        toolbar = Toolbar(self)

        password_entry = PasswordEntry(self)
        PasswordController(password_entry)
        password_entry.setFixedHeight(100)
        password_entry.setFixedWidth(200)

        round_button = RoundButton("Click Me!")
        ButtonController(round_button)
        round_button.setFixedSize(190, 40)

        sub_layout.addWidget(password_entry)
        sub_layout.addWidget(round_button)

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


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
