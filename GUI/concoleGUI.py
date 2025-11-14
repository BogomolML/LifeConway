from os import system, name


clear = lambda: system('cls' if name == 'nt' else 'clear')

def draw_field(field):
    clear()
    for row in field:
        s = ' '.join(map(str, row.astype(int)))
        s = s.replace('0', '.')
        s = s.replace('1', '@')
        print(s)
