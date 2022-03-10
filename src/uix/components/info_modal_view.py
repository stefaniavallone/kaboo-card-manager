from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.modalview import ModalView

Builder.load_file("uix/components/kv/info_modal_view.kv")


class InfoModalView(ModalView):

    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.size_hint = (0.8, 0.7)
        self.text = "[b]ABOUT THIS TOOL[/b]\n\nThis project aims to provide a convenient tool to manipulate and enlarge the Kaboo game cards.\nIt is intended to help us and anyone who wants to increase the card base for Kaboo and support the game.\n\n"
        self.text += "[b]FEATURES[/b]\n\n It provides the following functionalities:\n   - loading a card file from FileSystem of creating a new one; \n   - [b]viewing cards[/b] in a [i]list[/i] or [i]grid[/i] manner;\n   - [b]inserting[/b], [b]updating[/b] or [b]deleting[/b] cards;\n   - [b]searching cards[/b] by name;\n   - [b]filtering cards[/b] by some conditions, e.g. cards with less than 5 words for forbidden words or with duplicates.\n   - It automatically saves the modifications on the file.\n\n"
        self.text += "[b]SENDING US RESULTS[/b]\n\nOnce you have obtained a modified card file or a new one, to send it to us you can follow 2 ways:\n    - make a pull request at https://github.com/stefaniavallone/kaboo;\n    - send the file via email to the email address [b]stefaniaavallone3@gmail.com[/b].\n\nWe will take care of doing integrity checks on the new words. All help and contributions are welcome!"