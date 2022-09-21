# Die wesentlichen Imports für PyQt
from PyQt6.QtWidgets import QApplication, QWidget
# Import für die Commandline-Argumente und das
# Schließen der Applikation
import sys
# Wir erstellen eine Applikation auf Basis der
# Commandline-Argumente. # Falls diese nicht benötigt werden, wäre
# der Aufruf QApplication([]) möglich.
app = QApplication(sys.argv)
# Wir erstellen ein Qt Widget, welches unser
# erstes Fenster wird.
window = QWidget()
window.show()
# WICHTIG!! Fenster sind standardgemäß nicht
# sichtbar
# Start der Event-Loop mit Beendigung des
# Programmes.
sys.exit(app.exec())
