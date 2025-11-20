import sys
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

    def InitUI(self):
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Преобразование звука в ноты')
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Преобразование звука в ноты')
        self.file_name = "File"
        self.tabs = QTabWidget(self)
        self.file_window = QWidget()
        self.noty_window = QWidget()

        self.tabs.addTab(self.file_window, "")
        self.tabs.addTab(self.noty_window, "")
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
        notes = Notes()
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(len(notes.list_notes) - 1)
        self.table.setHorizontalHeaderLabels(notes.list_notes[0])
        for num, row in enumerate(notes.list_notes[1:]):
            for id, val in enumerate(row):
                self.table.setItem(num, id, QTableWidgetItem(val))
        self.page2_layout = QVBoxLayout()
        self.page2_layout.addWidget(self.table)

    def download_file(self):
        self.file_name = QFileDialog.getOpenFileName(self, "Выберите звуковой файл", "",
                                                     "Звуковой файл (*.mp3);;Звуковой файл (*.wav);;Звуковой файл (*.ogg);;Все файлы (*)")[
            0]
        self.file_title.setText(self.file_name)

    def Play(self):
        try:
            signal = AudioSegment.from_file(self.file_name)
            pydub.play(signal)
        except:
            print(self.file_name)


class Note_Window(QWidget):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    sys.exit(app.exec())
