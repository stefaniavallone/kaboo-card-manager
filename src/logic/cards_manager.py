import json


class CardsManager(dict):

    def __init__(self, path_file):
        super().__init__()
        self.path_file = path_file
        self._read_file()

    def _read_file(self):
        with open(self.path_file, 'r') as file:
            elements = json.load(file)
        for key, value in elements.items():
            self[key.lower()] = [f.lower() for f in value]

    def update_card(self, word, forbidden):
        self[word.lower()] = [f.lower().strip() for f in forbidden]

    def add_card(self, word, forbidden):
        forbidden = forbidden.split(",")
        v = self.get(word.lower())
        if v is None:
            self[word.lower()] = [f.lower().strip() for f in forbidden]
            return True
        else:
            return False

    def remove_card(self, word):
        v = self.get(word.lower())
        if v is None:
            return False
        else:
            del self[word.lower()]
            return True

    def save(self):
        with open(self.path_file, 'w', encoding='utf-8') as f:
            json.dump({word: forbidden for word, forbidden in self.items()}, f, indent=4)

    def filter(self, filter_funct=""):
        if filter_funct == "<5 VALUES":
            return {word: forbidden for word, forbidden in self.items()
                    if len(forbidden) < 5}
        elif filter_funct == "DUPLICATES":
            return {word: forbidden for word, forbidden in self.items()
                    if len(forbidden) != len(set(forbidden))}
        else:
            return self
