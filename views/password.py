from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QLineEdit, QCheckBox, QVBoxLayout


class PasswordEntry(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter your password")
        palette = self.line_edit.palette()
        palette.setColor(QPalette.Text, Qt.black)
        self.line_edit.setPalette(palette)

        self.layout.addWidget(self.line_edit)

        self.show_password_checkbox = QCheckBox("Hide password", self)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_echo_mode)

        self.layout.addWidget(self.show_password_checkbox)

    def toggle_password_echo_mode(self, state):
        if state == Qt.Checked:
            self.line_edit.setEchoMode(QLineEdit.Password)
        else:
            self.line_edit.setEchoMode(QLineEdit.Normal)

    def set_text(self, text):
        self.line_edit.setText(text)

    def clear_text(self):
        self.line_edit.clear()