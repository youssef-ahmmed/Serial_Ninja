from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QLineEdit, QCheckBox


class PasswordEntry(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)

        self.top = 50
        self.left = 50
        self.width = 200
        self.height = 30

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(self.left, self.top, self.width, self.height)
        # self.line_edit.setEchoMode(QLineEdit.Password)    # hide password

        self.hovered_text = "Enter your password"
        self.line_edit.setPlaceholderText(self.hovered_text)

        palette = self.line_edit.palette()
        palette.setColor(QPalette.Text, Qt.black)
        self.line_edit.setPalette(palette)

        self.show_password_checkbox = QCheckBox("hide password", self)
        self.show_password_checkbox.setGeometry(self.left, self.top + self.height + 10, self.width, 20)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_echo_mode)

    def toggle_password_echo_mode(self, state):
        if state == Qt.Checked:
            self.line_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit.setEchoMode(QLineEdit.Password)
