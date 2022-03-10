from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.app import MDApp
from uix.pages.root import Root


class BaseApp(MDApp):

    def __init__(self, **kwargs):
        super(BaseApp, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "Kaboo Card Manager"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        self._set_font("assets/fonts/Montserrat/", "Montserrat")

    def _set_font(self, fonts_path, font_name):
        fonts = [
            {
                "name": f"{font_name}",
                "fn_regular": fonts_path + f"{font_name}-Regular.ttf",
                "fn_bold": fonts_path + f"{font_name}-Bold.ttf",
            },
            {
                "name": f"{font_name}Light",
                "fn_regular": fonts_path + f"{font_name}-Light.ttf",
            },
            {
                "name": f"{font_name}Medium",
                "fn_regular": fonts_path + f"{font_name}-Medium.ttf",
            },
        ]
        for font in fonts:
            LabelBase.register(**font)
        for name, style in self.theme_cls.font_styles.items():
            if style[0].endswith("Light"):
                style[0] = f"{font_name}Light"
            elif style[0].endswith("Medium"):
                style[0] = f"{font_name}Medium"
            elif style[0] != "Icons":
                style[0] = f"{font_name}"

    def build(self):
        return Root()
