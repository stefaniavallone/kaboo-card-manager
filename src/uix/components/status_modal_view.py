from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty
from kivy.uix.modalview import ModalView

Builder.load_file("uix/components/kv/status_modal_view.kv")


class StatusModalView(ModalView):

    icon = StringProperty()
    text = StringProperty()
    subtext = StringProperty()
    text_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.size_hint = (0.4, 0.4)

    def open(self, *_args, **kwargs):
        super().open(*_args, **kwargs)
        Clock.schedule_once(self.dismiss, 2)

    def ok(self):
        self.icon = "check-circle"
        self.text_color = (8 / 255, 153 / 255, 17 / 255, 1)
        self.text = "Great"
        self.subtext = "Card added!"

    def already_added(self):
        self.icon = "alert"
        self.text_color = (215/255, 91/255, 0/255, 1)
        self.text = "Wait"
        self.subtext = "Card already added. Check it"

    def format_error(self):
        self.icon = "close"
        self.text_color = (225/255, 10/255, 10/255, 1)
        self.text = "Format error"
        self.subtext = 'Provide a good card format, like: "word; forb1, forb2, fobr3, forb4, forb5"'
