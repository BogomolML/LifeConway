import sys
from PyQt6.QtWidgets import QApplication

from GUI.mainWindow import MainWindow


SIZE = 20
CELL_SIZE = 40
THRESHOLD = 0.3

app = QApplication(sys.argv)
win = MainWindow(SIZE, CELL_SIZE, THRESHOLD)
win.setup_ui(win)
win.show()

sys.exit(app.exec())
