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

    1. This is a single player battleship game        
    2. There are 10 enemy ships to be destroyed
    3. The gameboard consists of 64 squares
    4. You must chose which square to attack using coordinates
    5. Pick a row from 1 - 8 and Column A - H
    6. If you select correctly you destroy 1 enemy ship
    7. A direct hit is represented by X and a miss by -
    8. Unselected squares are represented by a blank space
    9. You have 25 attempts to destroy all ememy ships or you lose
    10. You gain 1 turn for direct hit & lose 1 turn for a miss
        
    Have fun!!!
    """
    )

def main ():

    # Global variable for your ship locations
    YOURBOARD = [[' '] * 8 for x in range(8)]
    # Global variable for enemy ship where hits and misses are displayed
    ENEMYBOARD = [[' '] * 8 for i in range(8)]

    # Converting letters to numbers
    convert_letters = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 
    'E': 4, 'F': 5, 'G': 6, 'H': 7,
    }

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
            print("")

    def random_ships(board):
        """
        Creates 10 enemy ships randomly on gameboard
        """
        for ship in range(10):
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
        If user hits 10 ships before using lives, they win.
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
                turns += 1
            else:
                print('Sorry, that was not a direct hit')
                ENEMYBOARD[row][column] = '-'
                turns -= 1
            if ship_hit_counter(ENEMYBOARD) == 10:
                print('Congratulations, you have hit all targets and won!!!')
                break
            print('You have ' + str(turns) + ' turns remaining')
            if turns == 0:
                print('Sorry, you ran out of turns, the game is over')
                print('Please press run program to restart game')
                break

def run_game():
    """
    Starts a new game
    """
    # Displays welcome message and battleship game rules
    start_menu()
    # Asks user if they are ready to play the game after reading game rules
    print('Are you ready to play the game?')
    answer = input('Enter Y or N: \n').upper()
    print('')
    while True:
        if answer == 'Y':
            # Runs the main game functions
            main()
        elif answer == 'N':
            print('Please read game rules once more and press run program again')
            return False
        else: 
            print('Please enter Y or N')
            answer = input('Enter Y or N: \n').upper() 

run_game()