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

    def set_initial_style(self):
        self.setStyleSheet("background-color: #CCCCCC;")

    def adjust_size(self):
        screen = QDesktopWidget().screenGeometry()
        self.log.setFixedSize(screen.width(), 100)
