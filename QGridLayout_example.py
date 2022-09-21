import sys
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabellarische Darstellung")

        layout = QGridLayout()

        for y in range(1, 11):
            for x in range (1, 11):
                label = QLabel(str(x*y))
                layout.addWidget(label, y, x)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
