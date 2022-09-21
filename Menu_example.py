import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mein erstes Menü")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        menubar = self.menuBar()

        file_menu = menubar.addMenu("&File")
        open_action = self.menu_open()
        save_action = self.menu_save()

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        self.setStatusBar(QStatusBar(self))

    def menu_open(self) -> QAction:
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogStart)
        a = QAction(icon, "&Open", self)
        a.setStatusTip("Öffne ein File")
        a.setShortcut(QKeySequence.StandardKey.Open)
        a.triggered.connect(self.onClickFileOpen)
        return a

    def menu_save(self) -> QAction:
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton)
        a = QAction(icon, "&Save", self)
        a.setStatusTip("Speichere ein File")
        a.setShortcut(QKeySequence.StandardKey.Save)
        a.triggered.connect(self.onClickFileSave)
        return a

    def onClickFileOpen(self):
        print("File Open geklickt!")

    def onClickFileSave(self):
        print("File Save geklickt!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
