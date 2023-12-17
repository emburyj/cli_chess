'''
Author: Josh Embury
github username: emburyj
Date: 12/16/2023
Description: Main program for chess game.
'''
from ChessVar import *

def welcome_menu():
    print('''Welcome to the wonderful game of CLI Chess! Chess is a gentleman's\n
             game and we're pleased to present you with two modes of game play.\n
             Please enjoy your time in the command line playing chess!\n''')

def get_mode():
    print("Modes for chess game play:")
    print("1: Standard Chess")
    print("2: Catch 'em all Chess")
    mode = int(input("Which mode would you like to play (1 or 2)? "))
    return mode

def make_move(cv):
    '''
    '''
    from_square = input("Enter location of piece to move: ")
    to_square = input("Enter where you want to move: ")
    if from_square.lower() == 'q' or to_square.lower() == 'q':
        return [1, 1]
    return [cv.make_move(from_square, to_square), to_square]

if __name__ == "__main__":
    # display welcome screen
    welcome_menu()
    # get valid input
    mode = get_mode()
    while(mode != 1 and mode != 2):
        print("Please Select valid mode for game play!")
        mode = get_mode()
    #
    # initialize chessboard
    #
    cv = ChessVar()
    cv.set_mode(mode)
    while(cv.get_game_state() == "UNFINISHED"):
        cv.display_board()
        print(f"{cv.get_turn()}'s Turn!\n")
        move = make_move(cv)
        while(not move[0]):
            print("Enter a valid move!")
            move =make_move(cv)
        if move == [1, 1]:
            break
        print(cv.get_gameboard()[move[1]].__repr__())

    print(cv.display_board())
    print("Game over!")
    print(cv.get_game_state())