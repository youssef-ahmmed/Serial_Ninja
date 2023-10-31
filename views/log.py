from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QDesktopWidget


class LogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.set_initial_style()
        self.adjust_size()

    def init_ui(self):
        self.log = QPlainTextEdit(self)
        self.log.setReadOnly(True)
        self.log.setFont(QFont("Helvetica", 11, weight=QFont.Bold))
        self.log.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.log.setStyleSheet(
            "color: #333; background-color: #ADC4CE; border: 1px solid #AAA;"
        )

    def set_initial_style(self):
        self.setStyleSheet("border: 1px solid #AAA;")

    def adjust_size(self):
        screen = QDesktopWidget().screenGeometry()
        self.log.setFixedSize(screen.width(), 200)
