import pydub
from PyQt6.QtWidgets import QPushButton


class Note():
    def __init__(self, chastota):
        self.chastota = chastota
        Count("")
        self.note = QPushButton(None)
        self.note.setText()

def Count(name):
    return 1


class Notes():
    def __init__(self):
        self.list_notes=[["нота", "октава", "длительность"], ["до", "первая", "1"], ["ре", "первая", "1"]]

    def Zvuk_to_notes(self):
        pass
