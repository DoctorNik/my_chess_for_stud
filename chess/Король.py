class Bishop:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row1, col1):
        if not (0 <= row1 < 8 and 0 <= col1 < 8):
            return False
        if abs(row1 - self.row) == abs(col1 - self.col):
            return True
        return False
        
    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def char(self):
        return 'B'
    
    def get_color(self):
        return self.color