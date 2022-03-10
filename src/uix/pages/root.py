from kivy import Logger
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from utils.setup.class_loader import import_and_create_screens


Builder.load_file("uix/pages/kv/root.kv")


screens = import_and_create_screens("uix/pages")


class Root(ScreenManager):
    """
    The Root (or Assembler) of the App.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.add_screen("home")

    def add_screen(self, screen_name, **kwargs):
        if screen_name not in self.screen_names:
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])  # You must import kv before
            exec(screen_details["import"])  # executing imports
            screen_object = screen_details[
                "object"](**kwargs)  # eval(screen_details["object"])  # calling it
            screen_object.name = screen_name  # giving the name of the screen
            self.add_widget(
                screen_object
            )  # finally adding it to the screen manager
            Logger.debug(f"Added Screen: {screen_name}")

    def go_to_screen(self, screen_name, direction="left", **kwargs):
        self.add_screen(screen_name, **kwargs)
        self.transition.direction = direction
        self.current = screen_name



