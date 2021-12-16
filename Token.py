class Token:
    Type = None
    Literal = None
    Row = None
    Col = None
    BlockNo = None

    def __init__(self, Type, literal, row, col, blockno):
        self.Type = Type
        self.Literal = literal
        self.Row = row
        self.Col = col
        self.BlockNo = blockno
