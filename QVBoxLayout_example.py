import sys
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets Auswahl")

        layout = QVBoxLayout()
        widgets = (QLabel, QPushButton, QCheckBox, QRadioButton, QComboBox, QDateEdit, QSpinBox, QDoubleSpinBox, QFontComboBox, QLineEdit, QProgressBar)

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
