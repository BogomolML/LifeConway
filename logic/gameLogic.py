import numpy as np
from hashlib import sha256


class Field:
    def __init__(self, size, threshold):
        self._size = size
        self._field = np.random.random((size, size)) <= threshold
        self._new_generation = np.zeros_like(self._field)
        self._cnt_saves = 20
        self._hash_list = []
        self._is_limit = True

    @property
    def hash_list(self):
        return self._hash_list

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, new_field):
        self._field = new_field
        self._new_generation = np.zeros_like(self._field)

    @property
    def new_generation(self):
        return self._new_generation

    def create_generation(self):
        for i in range(self._field.shape[0]):
            for j in range(self._field.shape[1]):
                neighbors = self.count_neighbors(el=(i, j))
                if self._field[i, j] == 1:
                    self._new_generation[i, j] = 1 if neighbors in (2, 3) else 0
                else:
                    self._new_generation[i, j] = 1 if neighbors == 3 else 0
        self.save_old_generation()

    def count_neighbors(self, el: tuple) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        rows, cols = self._field.shape

        count = 0
        for dx, dy in directions:
            x, y = el[0] + dx, el[1] + dy
            if not self._is_limit:
                # TODO: добавить код для случая без ограничения
                pass
            if 0 <= x < rows and 0 <= y < cols:
                count += self._field[x, y]
        return count

    def save_old_generation(self):
        h = sha256(self._field.tobytes()).hexdigest()
        self._hash_list.append(h)
        if len(self._hash_list) > self._cnt_saves:
            self._hash_list.pop(0)
