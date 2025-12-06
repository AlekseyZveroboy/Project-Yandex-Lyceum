import sys

from PyQt6.QtGui import QWindow
from pydub import AudioSegment
# import librosa
import IPython
from IPython.core.display_functions import display
from PyQt6.QtWidgets import QLabel, QFileDialog, QPushButton, QApplication, QWidget, QTabWidget, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QMainWindow

from Note import Notes


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.InitUI()
#
#
#     def InitUI(self):
#         self.setGeometry(50, 50, 500, 500)
#         self.setWindowTitle('Преобразование звука в ноты')


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
        self.signal = AudioSegment.silent(1)
        try:
            with open("cash.txt", "r") as file:
                reader = list(file.read())
                self.file_name = reader[0]
                self.notes = list(reader[1])
        except:
            pass

    def InitUI(self):
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Преобразование звука в ноты')
        self.file_name = "File"
        self.tabs = QTabWidget(self)
        self.file_window = QWidget()
        self.noty_window = QWidget()

        self.tabs.addTab(self.file_window, "Звуковой файл")
        self.tabs.addTab(self.noty_window, "Ноты")
        self.Page1()
        self.Page2()
        self.file_window.setLayout(self.page1_layout)
        self.noty_window.setLayout(self.page2_layout)
        self.setCentralWidget(self.tabs)

    def Page1(self):
        self.download_file_button = QPushButton("загрузить файл", self)
        self.download_file_button.clicked.connect(self.download_file)
        self.file_title = QPushButton(self.file_name, self)
        self.file_title.move(100, 100)
        self.file_title.clicked.connect(self.Play)
        self.page1_layout = QVBoxLayout()
        self.page1_layout.addWidget(self.download_file_button)
        self.page1_layout.addWidget(self.file_title)

    def Page2(self):
        self.notes = Notes()
        self.note_image = QLabel(self)
        self.page2_layout = QVBoxLayout()
        self.page2_layout.addWidget(self.note_image)
        self.remake_note_button = QPushButton(self)
        self.make_note_button = QPushButton(self)
        self.save_button = QPushButton(self)
        self.remake_note_button.setText("Редактировать ноты")
        self.make_note_button.setText("Создать ноты")
        self.save_button.setText("Сохранить")
        self.remake_note_button.clicked.connect(self.remake_note)
        self.make_note_button.clicked.connect(self.make_note)
        self.save_button.clicked.connect(self.save)
        self.page2_layout.addWidget(self.save_button)
        self.page2_layout.addWidget(self.remake_note_button)
        self.page2_layout.addWidget(self.make_note_button)




    def download_file(self):
        self.file_name = QFileDialog.getOpenFileName(self, "Выберите звуковой файл", "",
                                                     "Звуковой файл (*.mp3);;Звуковой файл (*.wav);;Звуковой файл (*.ogg);;Все файлы (*)")[0]
        self.file_title.setText(self.file_name)
        self.signal = AudioSegment.from_file(self.file_name)

    def Play(self):
        try:
            pydub.play(self.signal)
        except:
            print(self.file_name)

    def remake_note(self):
        note_window = Note_Window(self, self.notes)
        note_window.show()

    def make_note(self):
        notes = self.notes
        self.notes = Notes()
        self.remake_note()
        self.notes=notes
    def save(self):
        self.save_name = QFileDialog.getSaveFileName(self, "Сохранить ноты", "ноты",
                                                     "Звуковой файл (*.mp3);;Звуковой файл (*.wav);;Звуковой файл (*.ogg);;Все файлы (*)")
    def closeEvent(self):
        with open("cash.txt", "w") as file:
            print(self.file_name, file=file)
            print(self.notes, file=file)


class Note_Window(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.notes = args[1]
        self.InitUI(args)

    def InitUI(self, args):
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Преобразование звука в ноты')
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setRowCount(len(self.notes.list_notes) - 1)
        self.table.setHorizontalHeaderLabels(self.notes.list_notes[0])
        for num, row in enumerate(self.notes.list_notes[1:]):
            for id, val in enumerate(row):
                self.table.setItem(num, id, QTableWidgetItem(val))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())
