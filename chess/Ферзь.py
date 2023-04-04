class Queen():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def char(self):
        return 'Q'
    
    def get_color(self):
        return self.color
    
    def can_move(self, row1, col1):
        if not (0 <= row1 < 8 and 0 <= col1 < 8):
            return False
        if abs(row1 - self.row) == abs(col1 - self.col) or not ((row1 != self.row) and (col1 != self.col)):
            return True
        return False
    
WHITE=1
BLACK=2

row0 = 4
col0 = 5
queen = Queen(row0, col0, BLACK)

print('white' if queen.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(queen.char(), end='')
        elif queen.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()

WHITE=1
BLACK=2

row0 = 7
col0 = 3
queen = Queen(row0, col0, BLACK)

print('white' if queen.get_color() == WHITE else 'black')
for row in range(8, -2, -1):
    for col in range(-1, 9):
        if row == row0 and col == col0:
            print(queen.char(), end='')
        elif queen.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
