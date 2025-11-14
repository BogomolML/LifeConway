from time import sleep
from hashlib import sha256
from keyboard import is_pressed

from gameLogic import Field
from concoleGUI import draw_field


SIZE = 20
THRESHOLD = 0.3


field = Field(SIZE, THRESHOLD)
while True:
    draw_field(field.field)
    field.create_generation()
    field.field = field.new_generation
    sleep(0.1)

    if sha256(field.field.tobytes()).hexdigest() in field.hash_list or is_pressed('q'):
        break
