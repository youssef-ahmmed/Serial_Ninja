from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QDesktopWidget


class LogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.log = QPlainTextEdit(self)
        self.log.setReadOnly(True)

        # Set gray background color
        self.setStyleSheet("background-color: #CCCCCC;")

        # Get screen dimensions
        screen = QDesktopWidget().screenGeometry()
        self.log.setFixedSize(screen.width(), 100)
