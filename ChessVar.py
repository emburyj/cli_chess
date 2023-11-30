'''
Author: Josh Embury
GitHub username: emburyj
Date: 11/22/23
Description: Defines ChessVar, ChessBoard, and ChessPiece classes and subclasses
'''
'''DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
1. Initializing the ChessVar class
The initilization of the ChessVar class will include creating a ChessBoard (cb) object.
When a cb object is initialized, ChessPiece objects of the appropriate subclass will be created and put in the correct
place on the chess board. These pieces are tracked in a data member in the ChessBoard object called _board.

2. Keeping track of turn order
Turn order will be kept track using a private data member in the ChessBoard class.
The _turn field will be updated from "Black" to "White" or vise versa if a valid move is made.

3. Keeping track of the current board position
Current board position will be kept track using a data member in the cb class. It will be a dictionary object named
_board with keys that are strings representing an index on the board (ex: A1) and keys being ChessPiece (or appropriate subclass)
objects. The _board object will be updated after a valid move is made.

4. Determining if a regular move is valid
Each ChessPiece (or appropriate subclass) will contain a data member called _possible_moves. When the make_move method 
is called on the ChessVar object, the _gameboard data member (ChessBoard) will call the get_valid_moves method on itself
with the from_square as the input. This will return a set object containing strings of valid to squares. The valid
to squares will be determined as follows:
- Get the ChessPiece object at the from square location in the _board data member
- Traverse through the possible_moves object starting from current position, moving away from piece.
- If you reach a possible move that has a piece of the same color, this and rest of the moves in that direction are not valid.
- If you reach a possible move that has a piece of a different color, this is a possible move that would be a capture.
- If the to_square argument is a valid move that would be a capture, the make_capture method would be called on the 
chessboard object.

5. Determining if a capture is valid
If the move is determined to be valid and the move is a capture, the make_capture method is called. During this method,
the _board data member of the chess board object is updated (piece moved, and piece removed). Also, the 
_white_pieces/_black_pieces data member is updated as required.

6. Determining the current state of the game
The chessboard object will have a two data members named _white_pieces/_black_pieces. These are used to keep track of
the number of pieces of each color remain on the board. When one of the data members reaches 0, the state of the game changes
as appropriate.

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
        # calls make_move method for _gameboard
        # checks for winner and updates _game_state a/r
        #
        pass

    def update_game_state(self):
        '''Method to update the _game_state field'''
        if self._gameboard.get_white() == 0:
            self._game_state = "BLACK_WINS"
        elif self._gameboard.get_black() == 0:
            self._game_state = "WHITE_WINS"

class ChessBoard(object):
    def __init__(self):
        self._gameover = False
        self._white_pieces = 16
        self._black_pieces = 16
        self._board = {} # dict - representing squares on board {str: Chesspiece obj}
        self._turn = "White"
        # initialize board dict with pieces

    def get_valid_moves(self, from_square):
        '''
        Method to determine valid moves for piece at given square
        :param from_square: String representing position on board
        :return: Set of strings representing valid moves
        '''
        pass

    def make_move(self, from_square, to_square):
        '''
        Method to update board for given move
        :param from_square: String representing from square
        :param to_square: String representing to square
        :return: Boolean - False if invalid move is given
        '''
        # checks if move is valid
        # if to_square in self.get_valid_moves(from_square):
        #   do something
        # checks if move is a capture
        # update turn
        pass

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
        # board_string = "   A   B   C   D   E   F   G   H   \n"
        # for i in range(8, 0, -1):
        #     current_row = f"{i|}"

    def update_turn(self):
        '''Method to change turn from black/white or white/black'''
        if self._turn == "Black":
            self._turn = "White"
        else:
            self._turn = "Black"

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

    def __init__(self, color, starting_position):
        self._color = color # String representing color of piece
        self._name = ' ' # String representing type of piece (ex: pawn, bishop, etc.)
        self._current_position = starting_position # String representing current position on board
        self._possible_moves = set() # Set of strings representing all possible moves for piece
        self._fwd_direction = 1 # integer representing direction piece moves on board
        if self._color == "Black":
            self._fwd_direction = -1

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
        self._get_possible_moves()

    def get_possible_moves(self):
        '''Placeholder method to determine and update all POSSIBLE moves for current location
        Needs to be overridden for each subclass of chesspiece'''
        pass

    def get_color(self):
        '''Getter method for _color field'''
        return self._color

    def get_name(self):
        '''Getter method for _name field'''
        return self._name

    def get_current_position(self):
        '''Getter method for _current_position field'''
        return self._current_position

    def get_possible_moves(self):
        '''Getter method for _valid_moves field'''
        return self._possible_moves


class King(ChessPiece):

    def __init__(self, color, starting_location):
        super().__init__(color, starting_location)
        self._name = 'King'

    def get_possible_moves(self):
        '''Method to determine all POSSIBLE moves for current location
            Updates _possible_moves field
            King can move one space in any direction'''
        pass

class Queen(ChessPiece):

    def __init__(self, color, starting_location):
        super().__init__(color, starting_location)
        self._name = 'Queen'

    def get_possible_moves(self):
        '''Method to determine all POSSIBLE moves for current location
            Updates _possible_moves field
            Queen can move any number of spaces in any one direction'''
        pass

class Bishop(ChessPiece):

    def __init__(self, color, starting_location):
        super().__init__(color, starting_location)
        self._name = 'Bishop'

    def get_possible_moves(self):
        '''Method to determine all POSSIBLE moves for current location
            Updates _possible_moves field
            Bishop can move any number of spaces in diagonal direction'''
        pass

class Knight(ChessPiece):

    def __init__(self, color, starting_location):
        super().__init__(color, starting_location)
        self._name = 'Knight'

    def __str__(self):
        '''Override str method because of duplicate initials with King..'''
        return f"{self._color} H" # H is for horse, okay?

    def get_possible_moves(self):
        '''Method to determine all POSSIBLE moves for current location
            Updates _possible_moves field
            Knight can move three paces: two in H/V dir, then one in V/H dir'''
        pass


class Rook(ChessPiece):

    def __init__(self, color, starting_location):
        super().__init__(color, starting_location)
        self._name = 'Rook'

    def get_possible_moves(self):
        '''Method to determine all POSSIBLE moves for current location
            Updates _possible_moves field
            Rook can move any number of spaces in horizontal or vertical direction'''
        pass

class Pawn(ChessPiece):

    def __init__(self, color, starting_location):
        super().__init__(color, starting_location)
        self._name = 'Pawn'
        self._first_turn = True

    def get_possible_moves(self):
        '''Method to determine all POSSIBLE moves for current location
            Updates _possible_moves field
            On first move, Pawn can move two spaces forward
            Otherwise, Pawn can move one space forward'''
        pass





