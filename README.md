# CLI Chess
## Description of the program
This command line interface (CLI) chess game was developed by Josh Embury for CS162 Section 400 at Oregon State University. There are two options for gameplay: standard chess, and "catch 'em all." The rules for "Catch 'em All" is follows: As in standard chess, white moves first. The winner is the first player to capture all of an opponent's pieces of one type, for example capturing all of the opponent's knights (of which there are two) would win the game, or all of the opponent's pawns (of which there are eight), or all of the opponent's kings (of which there is only one), etc. The king isn't a special piece in this game - there is no check or checkmate. Pieces move and capture the same as in standard chess, except that there is no castling, en passant, or pawn promotion. As in standard chess, each pawn should be able to move two spaces forward on its first move (but not on subsequent moves.
Locations on the board are specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8.

## Description of the code
This program was built with python using OOP. The ChessVar.py file defines several classes including ChessVar (which represents a game of chess used to track whose turn it is and if the game is over), a ChessBoard class, and a ChessPiece class along with various subclasses. The program includes input validation and error handling to ensure the user inputs legal moves for gameplay.

## Example output
    Modes for chess game play:
    1: Standard Chess
    2: Catch 'em all Chess
    Which mode would you like to play (1 or 2)? 1
       a   b   c   d   e   f   g   h
    8|B R|B H|B B|B Q|B K|B B|B H|B R|
    7|B P|B P|B P|B P|B P|B P|B P|B P|
    6|   |   |   |   |   |   |   |   |
    5|   |   |   |   |   |   |   |   |
    4|   |   |   |   |   |   |   |   |
    3|   |   |   |   |   |   |   |   |
    2|W P|W P|W P|W P|W P|W P|W P|W P|
    1|W R|W H|W B|W Q|W K|W B|W H|W R|
    
    WHITE's Turn!
    
    Enter location of piece to move: a2
    Enter where you want to move: a4
    WHITE PAWN moved to a4
       a   b   c   d   e   f   g   h
    8|B R|B H|B B|B Q|B K|B B|B H|B R|
    7|B P|B P|B P|B P|B P|B P|B P|B P|
    6|   |   |   |   |   |   |   |   |
    5|   |   |   |   |   |   |   |   |
    4|W P|   |   |   |   |   |   |   |
    3|   |   |   |   |   |   |   |   |
    2|   |W P|W P|W P|W P|W P|W P|W P|
    1|W R|W H|W B|W Q|W K|W B|W H|W R|
    
    BLACK's Turn!
    
    Enter location of piece to move: d7
    Enter where you want to move: d6
    BLACK PAWN moved to d6
       a   b   c   d   e   f   g   h
    8|B R|B H|B B|B Q|B K|B B|B H|B R|
    7|B P|B P|B P|   |B P|B P|B P|B P|
    6|   |   |   |B P|   |   |   |   |
    5|   |   |   |   |   |   |   |   |
    4|W P|   |   |   |   |   |   |   |
    3|   |   |   |   |   |   |   |   |
    2|   |W P|W P|W P|W P|W P|W P|W P|
    1|W R|W H|W B|W Q|W K|W B|W H|W R|
    
    WHITE's Turn!
    
    Enter location of piece to move:
