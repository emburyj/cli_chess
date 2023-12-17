'''
Author: Josh Embury
GitHub username: emburyj
Date: 11/22/23
Description: Defines ChessVar, ChessBoard, and ChessPiece classes and subclasses
'''

class ChessVar(object):
    '''A class to represent a game of chess.'''
    def __init__(self):
        self._game_state = "UNFINISHED"
        self._gameboard = ChessBoard()
        self._mode = 2

    def get_game_state(self):
        '''Getter method for _game_state field'''
        return self._game_state

    def get_gameboard(self):
        '''Getter method for _gameboard field'''
        return self._gameboard.get_board()

    def get_turn(self):
        '''Getter method for current turn'''
        return self._gameboard.get_turn()

    def make_move(self, from_square, to_square):
        '''
        Method to make a move on the
        :param from_square: String representing from square
        :param to_square: String representing to square
        :return: Boolean
        '''
        # check if game has not been won
        if self._game_state == "UNFINISHED":
            move = self._gameboard.make_move(from_square, to_square)
            if move:
                self.update_game_state()
                return True
        return False

    def update_game_state(self):
        '''
        Method to update the _game_state field
        return: void
        '''
        if self._mode == 1:
            if self._gameboard.get_white()['KING'] == 0:
                self._game_state = "BLACK_WON"
            if self._gameboard.get_black()['KING'] == 0:
                self._game_state = "WHITE_WON"

        if self._mode == 2:
            # check if white pieces of any type is zero
            if 0 in self._gameboard.get_white().values():
                self._game_state = "BLACK_WON"
            # check if black pieces of any type is zero
            elif 0 in self._gameboard.get_black().values():
                self._game_state = "WHITE_WON"

    def set_mode(self, new_mode):
        '''Setter mode for _mode field.
        :new_mode: Integer representing new mode.
        :return: Void
        '''
        self._mode = new_mode

    def display_board(self):
        '''Displays current board'''
        self._gameboard.display_board()

class ChessBoard(object):
    '''Class to represent a chess board.'''
    def __init__(self):
        self._pieces = { # dict representing num of pieces on board
            'WHITE': {
                'KING': 1,
                'QUEEN': 1,
                'BISHOP': 2,
                'KNIGHT': 2,
                'ROOK': 2,
                'PAWN': 8
            },
            'BLACK': {
                'KING': 1,
                'QUEEN': 1,
                'BISHOP': 2,
                'KNIGHT': 2,
                'ROOK': 2,
                'PAWN': 8
            }
        }
        self._board = {} # dict - representing squares on board {str: Chesspiece obj}
        self._turn = "WHITE"
        # initialize board dict with pieces
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(1, 9):
            if i < 3:
                current_color = 'WHITE'
            else:
                current_color = 'BLACK'

            # construct the board
            for letter in alpha:
                if (i == 1 or i == 8) and (letter == 'a' or letter == 'h'):
                    self._board[f"{letter}{i}"] = ChessPiece("ROOK", current_color, f"{letter}{i}", self._board, ['V', 'H'])
                elif (i == 1 or i == 8) and (letter == 'b' or letter =='g'):
                    self._board[f"{letter}{i}"] = Knight("KNIGHT", current_color, f"{letter}{i}", self._board)
                elif (i == 1 or i == 8) and (letter == 'c' or letter == 'f'):
                    self._board[f"{letter}{i}"] = ChessPiece("BISHOP", current_color, f"{letter}{i}", self._board, ['D'])
                elif (i == 1 or i == 8) and letter == 'd':
                    self._board[f"{letter}{i}"] = ChessPiece("QUEEN", current_color, f"{letter}{i}", self._board, ['V', 'H', 'D'])
                elif (i == 1 or i == 8) and letter == 'e':
                    self._board[f"{letter}{i}"] = King("KING", current_color, f"{letter}{i}", self._board, ['V', 'H', 'D'])
                elif i == 2 or i == 7:
                    self._board[f"{letter}{i}"] = Pawn("PAWN", current_color, f"{letter}{i}", self._board, ['V'])
                else:
                    self._board[f"{letter}{i}"] = None

    def make_move(self, from_square, to_square):
        '''
        Method to update board for given move.
        :param from_square: String representing from square
        :param to_square: String representing to square
        :return: Boolean - False if invalid move is given
        '''
        # check if arguments are valid
        # check if intputs are squares on board, and check if inputs are equal to eachother
        if from_square not in self._board.keys() or to_square not in self._board.keys() or to_square == from_square:
            return False

        # get piece currently at the to_square for moving
        piece_to_move = self._board[from_square]

        # check if empty square or wrong color
        if not piece_to_move or piece_to_move.get_color() != self._turn:
            return False # nobody's there or wrong turn

        # checks if move is valid for piece
        if piece_to_move.validate_move(to_square):
            if self._board[to_square]: # check if this is a capture
                # update current piece count
                self.decrease_piece_count(self._board[to_square].get_name(), self._board[to_square].get_color())
            piece_to_move.update_current_position(to_square) # update piece location
            self._board[from_square] = None # update board from square
            self._board[to_square] = piece_to_move # update board to square
            self.update_turn() # update turn
            return True # move successful

        return False # not a valid move for that piece

    def display_board(self):
        '''Method to display pieces on board using ascii art'''
        board_string = "   a   b   c   d   e   f   g   h   \n"
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(8, 0, -1):
            current_row = f"{i}|"
            for letter in alpha:
                if self._board[f"{letter}{i}"]:
                    current_row += str(self._board[f"{letter}{i}"]) + "|"
                else:
                    current_row += '   |'
            board_string += current_row + '\n'
        print(board_string)

    def update_turn(self):
        '''Method to change turn from black/white or white/black'''
        if self._turn == "BLACK":
            self._turn = "WHITE"
        else:
            self._turn = "BLACK"

    def decrease_piece_count(self, name, color):
        '''
        Method to decrease number of pieces of certain type on board.
        :param name: String representing name of piece to decrement (ie PAWN etc)
        :param color: String representing color of piece to decrement ("BLACK" or "WHITE")
        :return: Void
        '''
        self._pieces[color][name] -= 1

    def get_turn(self):
        '''Getter method for _turn field'''
        return self._turn

    def get_white(self):
        '''Getter method for dict of white pieces on board'''
        return self._pieces['WHITE']

    def get_black(self):
        '''Getter method for dict of black pieces on board'''
        return self._pieces['BLACK']

    def get_board(self):
        '''Getter method for _board field'''
        return self._board

class ChessPiece(object):
    '''Class to represent a chess piece.'''
    def __init__(self, name, color, starting_position, board, valid_directions=None):
        self._name = name # String representing type of piece (ex: pawn, bishop, etc.)
        self._color = color # String representing color of piece
        self._current_position = starting_position # String representing current position on board
        self._board = board # ChessBoard object
        self._valid_directions = valid_directions # list of strings representing valid directions ex: ['V', 'H', 'D']

    def __repr__(self):
        '''Override repr to describe name, color, and current location of piece.
            Useful for testing...'''
        return f"{self._color} {self._name} moved to {self._current_position}"

    def __str__(self):
        '''Override str method to return short name for display on chessboard'''
        return f"{self._color[0]} {self._name[0]}"

    def update_current_position(self, new_position):
        '''
        Setter method for _current_position field.
        :param new_position: String representing new location for piece.
        :return: Void
        '''
        self._current_position = new_position

    def validate_move(self, to_square):
        '''Method to determine if move is valid for this piece.
        :to_square: String representing square to move to.
        :return: Boolean
        '''
        # check if piece of same color in destination square
        if self._board[to_square] and self._board[to_square].get_color() == self._color:
            return False

        # check if valid direction
        dir = self.check_direction(to_square)
        if dir not in self._valid_directions:
            return False

        return self.check_path(to_square, dir)

    def get_color(self):
        '''Getter method for _color field'''
        return self._color

    def get_name(self):
        '''Getter method for _name field'''
        return self._name

    def get_current_position(self):
        '''Getter method for _current_position field'''
        return self._current_position

    def check_direction(self, to_square):
        '''
        Method to determine direction piece to be moved in. Vertical, Horizontal, or Diagonal.
        :param to_square: String representing square on board to be moved.
        :return: String representing direction: 'V', 'H', 'D' or None
        '''
        from_row = int(self._current_position[1])
        from_col = self._current_position[0]
        to_row = int(to_square[1])
        to_col = to_square[0]
        row_diff = abs(from_row - to_row)
        col_diff = abs(ord(from_col) - ord(to_col))

        # check if vertical
        if from_col == to_col:
            return 'V'

        # check if horizontal
        if from_row == to_row:
            return 'H'

        # check if diagonal
        if row_diff == col_diff:
            return 'D'

        return None # not in a sanctioned direction

    def check_path(self, to_square, direction):
        '''
        Method to deterime if path on board is clear of other pieces.
        :param to_square: String representing square on board to move.
        :return: Boolean
        '''
        from_row = int(self._current_position[1])
        from_col = self._current_position[0]
        from_col_ord = ord(from_col)
        to_row = int(to_square[1])
        to_col = to_square[0]
        to_col_ord = ord(to_col)

        if direction == 'H':
            dir = (to_col_ord - from_col_ord) // abs(to_col_ord - from_col_ord)
            for i in range(from_col_ord + dir, to_col_ord, dir):
                if self._board[f"{chr(i)}{from_row}"]:
                    return False # someone is at {chr(i)}{from_row}
            return True

        if direction == 'V':
            dir = (to_row - from_row)//abs(to_row - from_row)
            for i in range(from_row + dir, to_row, dir):
                if self._board[f"{from_col}{str(i)}"]:
                    return False # someone is at {from_col}{str(i)}
            return True

        if direction == 'D':
            dirv = (to_row - from_row)//abs(to_row - from_row)
            dirh = (to_col_ord - from_col_ord) // abs(to_col_ord - from_col_ord)
            for u, i in enumerate(range(from_col_ord + dirh, to_col_ord, dirh)):
                for v, j in enumerate(range(from_row + dirv, to_row, dirv)):
                    if u == v and self._board[f"{chr(i)}{str(j)}"]:
                        return False # Someone is at {chr(i)}{str(j)}
            return True
        return False

class King(ChessPiece):
    '''Class to represent a King chess piece.'''
    def __init__(self, name, color, starting_location, board, valid_directions):
        super().__init__(name, color, starting_location, board, valid_directions)

    def validate_move(self, to_square):
        '''
        Method to validate move for King. King can move one space in any direction.
        :param to_square: String representing square to move to
        :return: Boolean
        '''
        # check length of move
        diff_col = abs(int(self._current_position[1]) - int(to_square[1]))
        diff_row = abs(ord(self._current_position[0]) - ord(to_square[0]))

        # check if more than one space
        if diff_row > 1 or diff_col > 1:
            return False
        else:
            return super().validate_move(to_square)

class Knight(ChessPiece):
    '''Class to represent a Knight chess piece.'''
    def __init__(self, name, color, starting_location, board):
        super().__init__(name, color, starting_location, board)

    def validate_move(self, to_square):
        '''
        Method to validate move for knight.
        :param to_square: String representing square to move to.
        :return: Boolean
        '''
        diff_col = abs(int(self._current_position[1]) - int(to_square[1]))
        diff_row = abs(ord(self._current_position[0]) - ord(to_square[0]))

        # check if teammate is at to_square
        to_piece = self._board[to_square]
        if to_piece and to_piece.get_color() == self._color:
            return False

        # check if valid destination
        if (diff_col == 2 and diff_row == 1) or (diff_col == 1 and diff_row == 2):
            return True

        return False

    def __str__(self):
        '''Override str method because of duplicate initials with King...'''
        return f"{self._color[0]} H" # H is for horse, okay?

class Pawn(ChessPiece):
    '''Class to represent a Pawn chess piece.'''
    def __init__(self, name, color, starting_location, board, valid_directions):
        super().__init__(name, color, starting_location, board, valid_directions)
        self._first_turn = True
        self._fwd_direction = 1 # integer representing direction pawn moves on board
        if self._color == "BLACK":
            self._fwd_direction = -1

    def validate_move(self, to_square):
        '''
        Method to validate move for pawn. On first move, Pawn can move two spaces forward.
        Otherwise, Pawn can move one space forward. Captures opponents if they are 1 fwd space to the diagonal l/r
        :to_square: String representing square to move to
        :return: Boolean
        '''
        # check if valid capture - special case for pawn
        cap_piece = self._board[to_square]
        col = self._current_position[0]
        row = int(self._current_position[1])
        cap_row = row + self._fwd_direction
        # check if opponent in to_square
        if cap_piece and cap_piece.get_color() != self._color:
            cap_col1 = chr(ord(col) + 1)
            cap_col2 = chr(ord(col) - 1)
            cap1 = cap_col1 + str(cap_row)
            cap2 = cap_col2 + str(cap_row)
            # check if to_square is 1 space diagonal
            if to_square == cap1 or to_square == cap2:
                if self._first_turn:
                    self._first_turn = False
                return True

        from_row = int(self._current_position[1])
        to_row = int(to_square[1])

        # check if piece in path
        if self._board[to_square]:
            return False

        # first turn check
        if self._first_turn and abs(from_row - to_row) > 2:
            return False

        # direction check
        if self.check_direction(to_square) not in self._valid_directions:
            return False
        dir = (to_row - from_row)//abs(to_row - from_row)
        if dir != self._fwd_direction:
            return False
        # check if one move if not first move
        if not self._first_turn and abs(from_row - to_row) > 1:
            return False
        # check path
        if self.check_path(to_square, self.check_direction(to_square)):
            self._first_turn = False
            return True

        return False
if __name__ == '__main__':
    pass