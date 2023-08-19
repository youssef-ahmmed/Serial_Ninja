from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette


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

        # Set the text color to black
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



# if __name__ == "__main__":
#     app = QApplication([])
#     window = QMainWindow()
#     window.setWindowTitle("Password")
#     window.resize(300, 200)
#
#     # Create a central widget to hold the password entry
#     central_widget = QWidget(window)
#     window.setCentralWidget(central_widget)
#
#     # Create a layout for the central widget
#     layout = QVBoxLayout(central_widget)
#
#     # Create the password entry widget
#     password_entry = PasswordEntry()
#     layout.addWidget(password_entry)
#
#     window.show()
#     app.exec()

