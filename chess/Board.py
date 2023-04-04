WHITE = 1
BLACK = 2

def oppnent(color):
    if color == WHITE:
        return BLACK
    return WHITE

color = WHITE

if color == BLACK:
    do_something()

color == other_color

oppnent_color = oppnent(color)



class ChessBoard:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[1][4] = Pawn(1, 4, WHITE)

    def current_palyer_color(self):
        return self.color
    
    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()
    
    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True
    
    def print_board(board):
        print(' +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', board.cell(row, col), end='  ')
            print('|')
            print(' +----+----+----+----+----+----+----+----+')
        print(end = '        ')
        for col in range(8):
            print(col, end = '        ')
        print()