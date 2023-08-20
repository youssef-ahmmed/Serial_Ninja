from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QActionGroup


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_menus()
        self.init_actions()
        self.init_encryption_menu()

    def init_menus(self):
        self.file_menu = self.addMenu("File")
        self.settings_menu = self.addMenu("Settings")
        self.help_menu = self.addMenu("Help")

    def init_actions(self):
        self.open_action = QAction("Open", self)
        self.save_action = QAction("Save", self)
        self.port_configurations_action = QAction("Port Configurations", self)

        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.settings_menu.addAction(self.port_configurations_action)

    def init_encryption_menu(self):
        self.encryption_mode_submenu = QMenu("Encryption Mode", self)
        self.encryption_action_group = QActionGroup(self)

        self.encryption_action = QAction("Encryption", self)
        self.no_encryption_action = QAction("No Encryption", self)

        self.encryption_action.setCheckable(True)
        self.no_encryption_action.setCheckable(True)

        self.encryption_action_group.addAction(self.encryption_action)
        self.encryption_action_group.addAction(self.no_encryption_action)

        self.encryption_mode_submenu.addAction(self.encryption_action)
        self.encryption_mode_submenu.addAction(self.no_encryption_action)

        self.settings_menu.addMenu(self.encryption_mode_submenu)
