from PyQt6 import QtCore, QtGui, QtWidgets


class GridWidget(QtWidgets.QWidget):
    def __init__(self, field_size, cell_size):
        super().__init__()
        self.setFixedSize(field_size * cell_size, field_size * cell_size)
        self._field_size = field_size
        self._cell_size = cell_size
        self._cells = [[False for _ in range(self._field_size)] for _ in range(self._field_size)]

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        painter.setPen(QtGui.QPen(QtGui.QColor('black'), 1))
        for i in range(self._field_size + 1):
            painter.drawLine(0, self._cell_size * i, self.width(), self._cell_size * i)
            painter.drawLine(self._cell_size * i, 0, self._cell_size * i, self.height())

        painter.setBrush(QtGui.QBrush(QtGui.QColor('black')))
        for i in range(self._field_size):
            for j in range(self._field_size):
                if self._cells[i][j]:
                    painter.drawRect(j * self._cell_size, i * self._cell_size, self._cell_size, self._cell_size)

    def update_grid(self, field):
        self._cells = field
        self.update()
