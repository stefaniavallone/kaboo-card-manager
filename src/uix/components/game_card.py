from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField

from src.utils.widget import hide_widget

Builder.load_file("uix/components/kv/game_card.kv")


class GameCard(MDCard):
    word = StringProperty()
    forbidden = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda x: hide_widget(self.ids.controls, hide=True))

    def on_forbidden(self, instance, value):
        self.ids.forbidden_container.clear_widgets()
        for i, f in enumerate(value):
            self.ids.forbidden_container.add_widget(
                MDTextField(text=f,
                            halign="center")
            )
        hide_widget(self.ids.controls, hide=False)

    def add_forbidden(self):
        self.ids.forbidden_container.add_widget(
            MDTextField(text="",
                        halign="center")
        )

    def save(self):
        forbidden = []
        for c in reversed(self.ids.forbidden_container.children):
            if c.text != "":
                forbidden.append(c.text)
        self.forbidden = forbidden
        self.update_callback(self.word,
                             self.forbidden)
