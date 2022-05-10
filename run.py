from random import randint

def start_menu():
    """
    This prints out the rules of battleship to explain
    to players how the games works
    """
    print(
    """
    Welcome to Battleship
        
    The rules of battleship are as follows:
        
    1. There are 5 enemy ships to be destroyed
    2. The gameboard consists of 64 squares
    3. You must chose which sqaure to attack using coordinates
    4. Pick a row from 1 - 8 and Column A - H
    5. If you select correctly you destroy 1 enemy ship
    6. A direct hit is represented by X and a miss by -
    7. Unselected squares are represented by a blank space
    8. Destroy all enemy ships to win
    9. You have 25 attempts to destroy ememy ships or you lose
        
    Have fun!!!
    """
    )

# Global variable for your ship locations
YOURBOARD = [[' '] * 8 for x in range(8)]
# Global variable for enemy ship where hits and misses are displayed
ENEMYBOARD = [[' '] * 8 for i in range(8)]

# Converting letters to numbers
convert_letters = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 
    'E': 4, 'F': 5, 'G': 6, 'H': 7,
    }

def main():

    def print_gameboard(board):
        """
        Displays gameboard which is lettered and 
        numbered to allow user to attack enemy ships
        """
        print('   A  B   C   D   E   F   G   H  ')
        print(' --------------------------------')
        row_number = 1
        for row in board:
            print("%d|%s" % (row_number, " | ".join(row)))
            row_number += 1

    def random_ships(board):
        """
        Creates 5 ships randomly on user and enemy boards
        """
        for ship in range(5):
            ship_row, ship_column = randint(0,7), randint(0,7)
            while board[ship_row][ship_column] == 'X':
                ship_row, ship_column = ship_location()
            board[ship_row][ship_column] = 'X'

    def ship_location():
        """
        Ask the user which row (1-8) and column (A-H) they wish to guess.
        """
        row = input('Please enter ship row number from 1 - 8: ')
        while row not in '12345678':
            print('Please enter a vaid number')
            row = input('Please enter ship row number from 1 - 8: ')
        column = input ('Please enter a ship column letter A - H: ').upper()
        while column not in 'ABCDEFGH':
            print('Please enter a valid letter')
            column = input('Please enter a ship column letter A - H: ').upper()
        return int(row) - 1, convert_letters[column]

    def ship_hit_counter(board): 
        """
        Counts how many ships user has hit.
        If user hits 5 ships before computer, they win.
        """
        count = 0
        for row in board:
            for column in row:
                if column == 'X':
                    count += 1
        return count

    if __name__ == "__main__":
        random_ships(YOURBOARD)
        turns = 25
        while turns > 0:
            print_gameboard(ENEMYBOARD)
            row, column = ship_location()
            if ENEMYBOARD[row][column] == '-':
                print('You have already guessed that')
            elif YOURBOARD[row][column] == 'X':
                print(' Congratulations, that is a direct hit')
                ENEMYBOARD[row][column] = 'X'
                turns -= 1
            else:
                print('Sorry, that was not a direct hit')
                ENEMYBOARD[row][column] = '-'
                turns -= 1
            if ship_hit_counter(ENEMYBOARD) == 5:
                print('Congratulations, you are the winner')
                break
            print('You have ' + str(turns) + ' turns remaining')
            if turns == 0:
                print('Sorry, you ran out of turns, the game is over')
                break

while True:
    start_menu()
    main()