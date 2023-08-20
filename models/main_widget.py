import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget

from button import RoundButton
from log import LogWidget
from menu_bar import MenuBar
from password import PasswordEntry


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widgets Example")
        screen = QDesktopWidget().screenGeometry()

        self.setGeometry(screen.left(), screen.top(), screen.width(), screen.height())

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self.central_widget)

        menu_bar = MenuBar(self)
        password_entry = PasswordEntry(self)
        round_button = RoundButton("Click Me!")
        log_widget = LogWidget(self)

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
