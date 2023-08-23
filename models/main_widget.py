import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget

from button import RoundButton
from control.button_controller import ButtonController
from control.log_controller import LogController
from control.password_controller import PasswordController
from log import LogWidget
from menu_bar import MenuBar
from password import PasswordEntry


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Ninja")

        self.setGeometry(200, 200, 1000, 700)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self.central_widget)

        menu_bar = MenuBar(self)

        password_entry = PasswordEntry(self)
        PasswordController(password_entry)

        round_button = RoundButton("Click Me!")
        ButtonController(round_button)

        log_widget = LogWidget(self)
        LogController(log_widget)

        layout.addWidget(menu_bar)
        layout.addWidget(password_entry)
        layout.addWidget(round_button)
        layout.addWidget(log_widget)

        self.central_widget.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
