from PyQt6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        # WICHTIG!! Die Superklasse muss
        # unbedingt aufgerufen werden.
        super().__init__()

        self.n_times_clicked = 0
        self.setWindowTitle("Signal & Slots1")
        self.button = QPushButton("Press Me!")
        # Das Clicked-Signal wird mit einem Slot verbunden
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.setMinimumWidth(250)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.n_times_clicked += 1
        print("Der Button wurde bereits {} mal geklickt.".format(self.n_times_clicked))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
