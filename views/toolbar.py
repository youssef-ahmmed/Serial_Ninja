from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QToolBar, QAction

from controller.setting_controller import SettingController
from views.encryption_dialog import EncryptionDialog
from views.setting_dialog import SerialSettingsDialog


class Toolbar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_toolbar()
        self.start_communications()
        self.encryption_dialog = EncryptionDialog()
        self.serial_settings_dialog = SerialSettingsDialog()
        SettingController(self.serial_settings_dialog)

    def init_toolbar(self):
        self.port_configuration_action = QAction(QIcon("assets/configuration.ico"), "Port Configurations", self)
        self.port_configuration_action.setCheckable(True)

        self.encryption_mode_action = QAction(QIcon("assets/encrypt.ico"), "Encryption Mode", self)
        self.encryption_mode_action.setCheckable(True)

        self.help_action = QAction(QIcon("assets/help-desk.ico"), "Help", self)
        self.help_action.setCheckable(True)

        self.addAction(self.port_configuration_action)
        self.addAction(self.encryption_mode_action)
        self.addAction(self.help_action)

    def start_communications(self):
        self.port_configuration_action.triggered.connect(lambda: self.center_display(self.serial_settings_dialog))
        self.encryption_mode_action.triggered.connect(lambda: self.center_display(self.encryption_dialog))
        # TODO: self.help_action.triggered.connect(self.show_help_dialog)

    def center_display(self, widget):
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - widget.width()) / 2
        y = (screen_geometry.height() - widget.height()) / 2
        self.set_uncheckable()
        widget.move(x, y)
        widget.exec_()

    def set_uncheckable(self):
        self.encryption_mode_action.setCheckable(False)
        self.port_configuration_action.setCheckable(False)
        self.help_action.setCheckable(False)

    def show_encryption_dialog(self):
        self.encryption_dialog.exec_()

    def is_encryption_selected(self):
        return self.encryption_dialog.encryption_radio.isChecked()
