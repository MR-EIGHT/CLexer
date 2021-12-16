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

    def __repr__(self):
        return "Type: {}, Literal: {}, Row: {}, Column: {}, Block-Number: {}".format(self.Type, self.Literal, self.Row,
                                                                                     self.Col, self.BlockNo)
