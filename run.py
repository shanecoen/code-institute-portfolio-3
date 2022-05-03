# Legend
# X for placing ship and hit battlehsip
# ' ' for available space
# '-' for missed shot

from random import randint

# Your ship locations
YOURBOARD = [[' '] * 8 for x in range(8)]
# Enemy ship where hits and misses are displayed
ENEMYBOARD = [[' '] * 8 for i in range(8)]

# Converting letters to numbers
convert_letters = {
    'A': 0, 
    'B': 1, 
    'C': 2, 
    'D': 3, 
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    }

def print_gameboard(board):
    """
    Displays gameboard which is lettered and 
    numbered to allow user to attack enemy ships
    """
    print(' A B C D E F G H I J')
    print(' -------------------')
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1

def random_ships(board):
    """
    Creates ships randonly on user and enemy boards
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'

def ship_location():
    """
    Ask the user which row (1-8) and column (A-H) they wish to guess.
    """
    row = input('Please enter ship row number from 1 - 8')
    while row not in '12345678':
        print('Please enter a vaid number')
        row = input('Please enter ship row number from 1 - 8')
    column = input ('Please enter a ship column letter A - H').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid letter')
        column = input('Please enter a ship column letter A - H').upper()
    return int(row) - 1, convert_letters[column]
