from PyQt6 import QtCore, QtGui, QtWidgets

from logic.gameThread import GameThread
from GUI.grid import GridWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, field_size, cell_size, threshold):
        super().__init__()
        self._field_size = field_size
        self._cell_size = cell_size

        self._grid = GridWidget(self._field_size, self._cell_size)

        self._game_thread = GameThread(field_size, threshold)
        self._game_thread.generation_signal.connect(self._grid.update_grid)

    def set_field(self, field):
        self._grid = GridWidget(self._field_size, self._cell_size)
        self._grid.update_grid(field)

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)
        main_window.setStyleSheet('background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(140, 140, 140, 255), stop:0.527447 rgba(90, 90, 90, 220), stop:1 rgba(140, 140, 140, 255));'
                                  'font-family: Comic Sans MS;')
        central_widget = QtWidgets.QWidget()
        central_widget.setObjectName("central_widget")
        layout = QtWidgets.QVBoxLayout(central_widget)

        layout.addWidget(self._grid, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        main_window.setCentralWidget(central_widget)

        self._game_thread.start()

    def closeEvent(self, event):
        self._game_thread.stop()
        self._game_thread.wait()
        super().closeEvent(event)
