from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivy.app import App

from src.logic.cards_manager import CardsManager
from src.utils.widget import hide_widget
from uix.components.info_modal_view import InfoModalView
from uix.components.status_modal_view import StatusModalView


class GameCardListItem(OneLineAvatarIconListItem):
    word = StringProperty()
    icon = StringProperty()


class GameCardGridItem(MDRelativeLayout):
    word = StringProperty()
    forbidden = StringProperty()


class CardHandlerScreen(MDScreen):
    file_path = StringProperty()
    files_number = StringProperty()
    info_modal_view = None
    status_modal_view = None

    def __init__(self, file_path, **kw):
        super().__init__(**kw)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.app = App.get_running_app()
        self.file_path = file_path
        self.cards = CardsManager(file_path)
        self.view_type = "list"
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": v,
                "height": dp(56),
                "on_release": lambda x=v: self.set_item(x),
            } for v in ["ALL CARDS", "DUPLICATES", "<5 VALUES"]
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self._set_cards()
        self.menu.dismiss()

    def on_enter(self, *args):
        self._hide_widgets()
        self._set_cards()

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if self.ids.insert_input.focus and keycode == 40:  # 40 - Enter key pressed
            self.insert_card(self.ids.insert_input.text)

    def _set_cards(self):
        recycle_view = getattr(self.ids, self.view_type + "_view")
        recycle_view.data = []
        search_text = self.ids.search_field.text
        cards_set = self.cards.filter(filter_funct=self.ids.drop_item.current_item)
        self.files_number = f"{len(cards_set)} cards"
        for word, forbidden in cards_set.items():
            if search_text is not "":
                if search_text.lower() in word.lower():
                    self._add_game_card(word, forbidden)
            else:
                self._add_game_card(word, forbidden)

    def _add_game_card(self, word, forbidden):
        recycle_view = getattr(self.ids, self.view_type + "_view")
        recycle_view.data.append(
            {
                "viewclass": "GameCardListItem" if self.view_type == "list" else "GameCardGridItem",
                "icon": 'cards',
                "word": word,
                "forbidden": "\n".join(forbidden),
                "on_release": lambda: self._select_card(word, forbidden),
                "remove": lambda: self.remove_card(word)
            }
        )

    def _select_card(self, word, forbidden):
        self.ids.selected_card.word = word
        self.ids.selected_card.forbidden = forbidden

    def remove_card(self, word):
        self.cards.remove_card(word)
        self._set_cards()
        self.cards.save()

    def update_card(self, word, forbidden):
        self.cards.update_card(word, forbidden)
        self._set_cards()
        self.cards.save()

    def insert_card(self, uinp):
        try:
            parts = uinp.split(";")
            word = parts[0].strip()
            forbidden = parts[1].strip()
            status = self.cards.add_card(word, forbidden)
            if status:
                self.show_status("ok")
                self._set_cards()
                self.cards.save()
                self.ids.insert_input.text = ""
            else:
                self.show_status("already_added")
                self.ids.search_field.text = word
        except Exception as e:
            print("e", e)
            self.show_status("format_error")

    def toggle_grid(self):
        self.view_type = "grid" if self.view_type == "list" else "list"
        self.ids.view_changer.text = "GRID VIEW" if self.view_type == "list" else "LIST VIEW"
        self._hide_widgets()
        self._set_cards()

    def _hide_widgets(self):
        hide_widget(self.ids.list_view, hide=True if self.view_type == "grid" else False)
        hide_widget(self.ids.grid_view, hide=False if self.view_type == "grid" else True)

    def show_information(self):
        if not self.info_modal_view:
            self.info_modal_view = InfoModalView()
        self.info_modal_view.open()

    def show_status(self, status_type):
        if not self.status_modal_view:
            self.status_modal_view = StatusModalView()
        getattr(self.status_modal_view, status_type)()
        self.status_modal_view.open()