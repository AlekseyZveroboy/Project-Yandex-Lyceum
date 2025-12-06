import pydub
from PyQt6.QtWidgets import QPushButton
from PIL import Image, ImageDraw


class Note():
    def __init__(self, chastota):
        self.chastota = chastota
        Count("")
        self.note = QPushButton(None)
        self.note.setText()

def Count(name):
    return 1


class Notes():
    def __init__(self, list=[["нота", "октава", "длительность"], ["до", "первая", "1"], ["ре", "первая", "1"]]):
        self.list_notes = list

    def Zvuk_to_notes(self):
        return Notes

    def Draw(self):
        notes = {"до":1, "ре":2, "ми":3, "фа":4, "соль":5, "ля":6, "си":7}
        octaves1 = {"субконтроктава":0, "контроктава":1, "большая":2, "малая":3, "первая":4, "вторая":5, "третья":6, "четвёртая":7, "пятая":8}
        x, y = 0, 0
        octaves = []
        for i in self.list_notes:
            octaves.append(i[1])
        octaves=set(octaves)
        image = Image.new("RGB", (1000, 1000))
        drawer= ImageDraw.Draw(image)
        drawer.rectangle((0, 0, 1000, 1000), (255, 255, 255), False)
        for i in range(len(octaves)*6):
            drawer.line((0, i*25, 1000, i*25), fill=(0, 0, 0), width=2)
        for note in self.list_notes[1:]:
            num = notes[note[0]]
            octave = octaves1[note[1]]

            dur = note[2]
            if dur == "1":
                drawer.ellipse((self.list_notes.index(note)*30, (num-1)*12.5, self.list_notes.index(note)*30 + 15, (num-1)*25), (0, 0, 0), True)
                drawer.line((self.list_notes.index(note)*30, (num-1)*12.5, self.list_notes.index(note)*30 + 15, (num-1)*25), (0, 0, 0), True)
        image.save("proba.png")
n = Notes()
n.Draw()