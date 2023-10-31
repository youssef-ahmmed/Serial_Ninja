from PyQt5.QtGui import QColor, QTextCharFormat, QTextCursor
import strings


class LogController:

    _instance = None

    @staticmethod
    def get_instance():
        if LogController._instance is None:
            raise Exception("No object was created")
        return LogController._instance

    def __init__(self, log_widget):
        if LogController._instance is None:
            super(LogController, self).__init__()
            LogController._instance = self
            self.log_widget = log_widget
        else:
            raise Exception(strings.SINGLETON_ERROR)

    def log_error(self, message):
        self._log_message(f"[Error]: {message}", QColor(255, 0, 0))

    def log_success(self, message):
        self._log_message(f"[Success]: {message}", QColor(0, 128, 0))

    def _log_message(self, message, color):
        cursor = self.log_widget.log.textCursor()
        cursor.movePosition(QTextCursor.End)

        format_msg = QTextCharFormat()
        format_msg.setForeground(color)

        cursor.insertText(message + "\n", format_msg)

        self.log_widget.log.setTextCursor(cursor)
        self.log_widget.log.ensureCursorVisible()

    def get_log_status(self):
        cursor = self.log_widget.log.textCursor()
        cursor.movePosition(QTextCursor.End - 1)
        cursor.select(QTextCursor.LineUnderCursor)
        return cursor.selectedText().strip()
    