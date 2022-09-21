from PyQt6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        # WICHTIG!! Die Superklasse muss
        # unbedingt aufgerufen werden.
        super().__init__()

        self.n_times_clicked = 0
        # Ab 2 Widgets muss ein
        # Layoutmanager verwendet werden.
        layout = QVBoxLayout()
        self.setWindowTitle("Signal & Slots2")
        self.label = QLabel()
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.setMinimumWidth(250)
        # Die Widgets werden dem Layout hinzugefügt
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        # Ein Widget wird erstellt und das Layout hinzugefügt
        container = QWidget()
        container.setLayout(layout)
        # Das Container-Widget wird als central widget
        # im QMainWindow gesetzt
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        self.n_times_clicked += 1
        self.label.setText("Der Button wurde bereits {} mal geklickt.".format(self.n_times_clicked))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
