from PySide6.QtWidgets import QPushButton, QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QPainter, QBrush, QColor, QFont

class RoundButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setFixedSize(100, 40)

        self.normal_color = QColor("#126963")
        self.hover_color = QColor("#19958c")

        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.setPalette(palette)

        # self.setGeometry(100, 200, 60, 40)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.underMouse():
            painter.setBrush(QBrush(self.hover_color))
        else:
            painter.setBrush(QBrush(self.normal_color))

        painter.drawRoundedRect(self.rect(), 15, 15)


        painter.setPen(Qt.white)
        painter.setFont(QFont("Arial", 12, QFont.Bold))
        text_rect = self.rect()
        painter.drawText(text_rect, Qt.AlignCenter, self.text())




# if __name__ == "__main__":
#     app = QApplication([])
#     window = QMainWindow()
#     window.setWindowTitle("button")
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
#     button = RoundButton()
#     button.setText('send')
#     layout.addWidget(button)
#     window.show()
#     app.exec()