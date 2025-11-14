from PyQt6 import QtCore
from hashlib import sha256

from logic.gameLogic import Field


class GameThread(QtCore.QThread):
    generation_signal = QtCore.pyqtSignal(object)

    def __init__(self, size, threshold):
        super().__init__()
        self.field = Field(size, threshold)
        self._running = True

    def run(self):
        while self._running:
            self.field.create_generation()
            self.field.field = self.field.new_generation
            self.generation_signal.emit(self.field.field)

            is_loop = sha256(self.field.field.tobytes()).hexdigest() in self.field.hash_list
            if is_loop:
                print("Обнаружена зацикленность")
                break

            self.msleep(100)

    def stop(self):
        self._running = False
