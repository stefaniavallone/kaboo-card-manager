import json
import os

from kivy.properties import StringProperty
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen
import version
from uix.components.info_modal_view import InfoModalView


class HomeScreen(MDScreen):
    version = StringProperty()
    info_dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.version = version.__version__
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path)

    def file_manager_open(self):
        self.file_manager.show(os.getcwd())

    def select_path(self, path):
        self.exit_manager()
        toast(path)
        self.manager.go_to_screen("card_handler", direction="left", file_path=path)

    def create_new_file(self):
        path = "./new_file.json"
        with open(path, "w") as f:
            json.dump([], f)
        toast(f"Create new file {path}")
        self.manager.go_to_screen("card_handler", direction="left", file_path=path)

    def exit_manager(self, *args):
        self.file_manager.close()

    def show_information(self):
        if not self.info_dialog:
            self.info_dialog = InfoModalView()
        self.info_dialog.open()