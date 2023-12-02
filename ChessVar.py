'''
Author: Josh Embury
GitHub username: emburyj
Date: 11/22/23
Description: Defines ChessVar, ChessBoard, and ChessPiece classes and subclasses
'''

class ChessVar(object):
    def __init__(self):
        self._game_state = "UNFINISHED"
        self._gameboard = ChessBoard()

    def get_game_state(self):
        '''Getter method for _game_state field'''
        return self._game_state

    def make_move(self, from_square, to_square):
        '''
        Method to make a move on the
        :param from_square: String representing from square
        :param to_square: String representing to square
        :return: Boolean
        '''
        # checks if game is over
        if self._game_state == "UNFINISHED":
            move = self._gameboard.make_move(from_square, to_square)
            self.update_game_state()
            if move:
                print("Move Successful")
                return True
        print("Invalid Move!")
        return False

    def update_game_state(self):
        '''
        Method to update the _game_state field
        return: void
        '''
        if self._gameboard.get_white() == 0:
            self._game_state = "BLACK_WON"
        elif self._gameboard.get_black() == 0:
            self._game_state = "WHITE_WON"

class ChessBoard(object):
    def __init__(self):
        self._gameover = False
        self._white_pieces = 16
        self._black_pieces = 16
        self._board = {} # dict - representing squares on board {str: Chesspiece obj}
        self._turn = "WHITE"
        # initialize board dict with pieces
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(1, 9):
            if i < 3:
                current_color = 'WHITE'
            else:
                current_color = 'BLACK'

            for letter in alpha:
                if (i == 1 or i == 8) and (letter == 'a' or letter == 'h'):
                    self._board[f"{letter}{i}"] = Rook(current_color, f"{letter}{i}", self._board)
                elif (i == 1 or i == 8) and (letter == 'b' or letter =='g'):
                    self._board[f"{letter}{i}"] = Knight(current_color, f"{letter}{i}", self._board)
                elif (i == 1 or i == 8) and (letter == 'c' or letter == 'f'):
                    self._board[f"{letter}{i}"] = Bishop(current_color, f"{letter}{i}", self._board)
                elif (i == 1 or i == 8) and letter == 'd':
                    self._board[f"{letter}{i}"] = King(current_color, f"{letter}{i}", self._board)
                elif (i == 1 or i == 8) and letter == 'e':
                    self._board[f"{letter}{i}"] = Queen(current_color, f"{letter}{i}", self._board)
                elif i == 2 or i == 7:
                    self._board[f"{letter}{i}"] = Pawn(current_color, f"{letter}{i}", self._board)
                else:
                    self._board[f"{letter}{i}"] = None

    def make_move(self, from_square, to_square):
        '''
        Method to update board for given move
        :param from_square: String representing from square
        :param to_square: String representing to square
        :return: Boolean - False if invalid move is given
        '''
        # check if arguments are valid
        # checking if intputs are squares on board, and check if inputs are equal to eachother
        if from_square not in self._board.keys() or to_square not in self._board.keys() or to_square == from_square:
            return False

        # get piece currently at the to_square for moving
        piece_to_move = self._board[from_square]

        # check if empty square
        if not piece_to_move or piece_to_move.get_color() != self._turn:
            return False # nobody's there

        # checks if move is valid for piece
        if piece_to_move.validate_move(to_square):
            if self._board[to_square]: # check if this is a capture
                self.make_capture()
            piece_to_move.update_current_position(to_square)
            self._board[from_square] = None
            self._board[to_square] = piece_to_move

            # update turn
            self.update_turn()
            return True # move successful

        return False # not a valid move for that piece

    def make_capture(self, from_square, to_square):
        '''
        Method to update board in case of a capture move.
        :param from_square: String representing from square
        :param to_square: String representing to square
        :return: Void
        '''
        # update board: move and remove pieces from board
        # decrease appropriate piece count
        # check if game is over; update gameover a/r
        pass

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

    def get_turn(self):
        '''Getter method for _turn field'''
        return self._turn

    def get_gameover(self):
        '''Getter method for _gameover field'''
        return self._gameover

    def get_white(self):
        '''Getter method for _white_pieces field'''
        return self._white_pieces

    def get_black(self):
        '''Getter method for _black_pieces field'''
        return self._black_pieces


class ChessPiece(object):

    def __init__(self, color, starting_position, board):
        self._color = color # String representing color of piece
        self._board = board
        self._name = ' ' # String representing type of piece (ex: pawn, bishop, etc.)
        self._current_position = starting_position # String representing current position on board
        self._valid_directions = ['v', 'h', 'd']

    def __repr__(self):
        '''Override repr to describe name, color, and current location of piece.
            Useful for testing...'''
        return f"{self._color} {self._name} located at {self._current_position}"

    def __str__(self):
        '''Override str method to return short name for display on chessboard'''
        return f"{self._color[0]} {self._name[0]}"

    def update_current_position(self, new_position):
        '''
        Setter method for _current_position field; calls
        :param new_position: String representing current location of
        :return:
        '''
        self._current_position = new_position
        # self.get_possible_moves()

    def validate_move(self, to_square):
        '''Placeholder method to determine if move is valid for this piece.
        Needs to be overridden for each subclass of chesspiece
        :to_square: String representing square to move to
        :return: Boolean
        '''
        return False # for now

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
        :return: 'v', 'h', 'd' or None
        '''
        from_row = int(self._current_position[1])
        from_col = self._current_position[0]
        to_row = int(to_square[1])
        to_col = to_square[0]

        row_diff = abs(from_row - to_row)
        col_diff = abs(ord(from_col) - ord(to_col))

        # check if vertical
        if from_col == to_col:
            return 'v'

        # check if horizontal
        if from_row == to_row:
            return 'h'

        # check if diagonal
        if row_diff == col_diff:
            return 'd'

        return None # not in a sanctioned direction

    def check_path(self, to_square, direction):
        '''
        Method to deterime if path on board is clear of other pieces
        :param to_square: String representing square on board to move
        :return: Boolean
        '''
        # check if horizontal
        if direction == 'h':
            pass
        if direction == 'v'
            pass
        if direction == 'd':
            pass
        # check if diag
        return False

class King(ChessPiece):

    def __init__(self, color, starting_location, board):
        super().__init__(color, starting_location, board)
        self._name = 'King'


class Queen(ChessPiece):

    def __init__(self, color, starting_location, board):
        super().__init__(color, starting_location, board)
        self._name = 'Queen'



class Bishop(ChessPiece):

    def __init__(self, color, starting_location, board):
        super().__init__(color, starting_location, board)
        self._name = 'Bishop'



class Knight(ChessPiece):

    def __init__(self, color, starting_location, board):
        super().__init__(color, starting_location, board)
        self._name = 'Knight'

    def __str__(self):
        '''Override str method because of duplicate initials with King..'''
        return f"{self._color[0]} H" # H is for horse, okay?


class Rook(ChessPiece):

    def __init__(self, color, starting_location, board):
        super().__init__(color, starting_location, board)
        self._name = 'Rook'


class Pawn(ChessPiece):

    def __init__(self, color, starting_location, board):
        super().__init__(color, starting_location, board)
        self._name = 'Pawn'
        self._first_turn = True
        self._fwd_direction = 1 # integer representing direction pawn moves on board
        if self._color == "BLACK":
            self._fwd_direction = -1

    def validate_move(self, to_square):
        '''
        Method to validate move for pawn.
        On first move, Pawn can move two spaces forward
        Otherwise, Pawn can move one space forward
        Captures opponents if they are 1 fwd space to the diagonal l/r
        :to_square: String representing square to move to
        :return: Boolean
        '''
        # check if valid capture - special case for pawn
        cap_piece = self._board[to_square]
        col = self._current_position[0]
        row = int(self._current_position[1])
        cap_row = row + self._fwd_direction * 1
        if cap_piece and cap_piece.get_color() != self._color:
            cap_col1 = chr(ord(col) + 1)
            cap_col2 = chr(ord(col) - 1)
            cap1 = cap_col1 + str(row)
            cap2 = cap_col2 + str(row)
            if to_square == cap1 or to_square == cap2:
                return True

        # check if piece in path
        # special case - first turn
        if int(to_square[1]) - row == 2:
            if self._first_turn:
                for i in range(1, 3): # check if any pieces in path
                    offset_square = row + self._fwd_direction * i
                    if self._board[f"{col}{str(offset_square)}"]:
                        return False
                self._first_turn = False # no longer first turn
                return True
            else: # if not first turn
                return False
        if int(to_square[1]) - row == 1:
            offset_square = row + self._fwd_direction

        return False




