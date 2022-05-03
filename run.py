# Your ship locations
YOURBOARD = [[' '] * 10 for x in range(10)]
# Enemy ship where hits and misses are displayed
ENEMYBOARD = [[' '] * 10 for i in range(10)]

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
    'I': 8,
    'J': 9,
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
