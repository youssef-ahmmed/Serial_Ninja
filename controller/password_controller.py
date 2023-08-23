import strings
from controller.log_controller import LogController


class PasswordController:

    _instance = None

    @staticmethod
    def get_instance():
        if PasswordController._instance is None:
            raise Exception("No object was created")
        return PasswordController._instance

    def __init__(self, password_entry):
        if PasswordController._instance is None:
            super(PasswordController, self).__init__()
            PasswordController._instance = self
            self.password_entry = password_entry
        else:
            raise Exception(strings.SINGLETON_ERROR)

    def get_password(self):
        return self.password_entry.line_edit.text()

    def validate_password(self):
        password = self.get_password()

        if len(password) == 4 and password.isascii():
            return True
        elif len(password) != 4 or not password.isascii():
            LogController.get_instance().log_error(strings.PASSWORD_ERROR)
            return False