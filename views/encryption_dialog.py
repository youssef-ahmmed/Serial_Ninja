from PyQt5.QtWidgets import QDialog, QVBoxLayout, QRadioButton


class EncryptionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Encryption Mode")
        self.layout = QVBoxLayout(self)

        self.encryption_radio = QRadioButton("Encryption")
        self.no_encryption_radio = QRadioButton("No Encryption")
        self.setGeometry(500, 500, 200, 200)
        self.layout.addWidget(self.encryption_radio)
        self.layout.addWidget(self.no_encryption_radio)
        self.setLayout(self.layout)
