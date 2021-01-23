
# The structure of the board    
    # o---o   o    [  [ True, False ],
    # |               [ True, False, False], 
    # o   o---o       [ False, True ],
    #     |           [ False, True, False],
    # o---o---o       [ True, True]           ]


def board_shape(board):
    rows = (len(board.split("\n"))+1)/2
    columns = rows[0].count("o")
    return rows, columns

class DotsAndBoxes(object):
    def __init__(self, starting_player=None, rows=None, columns=None, board=None):
        if board is not None:
            self._from_string(starting_player, board)
        else:
            self.rows, self.columns = rows, columns
            self.score = [0, 0]
            self.turn = starting_player
            self.borad = np.zeros((2*rows-1, 2*columns-1), dtype=np.int)
            self.r, self.c = self.board.shape
            self.num_boxes = (rows-1) * (cols-1)
    
    def _from_string(self, starting_player, board):
        #line = board.split("\n")
        rows, columns = board_shape(board)
        self.__init__(starting_player, rows, columns)