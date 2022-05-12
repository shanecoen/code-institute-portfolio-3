from random import randint
import os
import sys

# Global variables for ship locations
YOURBOARD = [[' '] * 8 for x in range(8)]
ENEMYBOARD = [[' '] * 8 for i in range(8)]


def reset_display():
    """
    Used to reset the game and begin from the start
    with a clear gameboard once player chooses to
    restart a new game after a game ends.
    """
    # os.system("cls" if os.name == "nt" else "clear") *** DELETE DELETE
    python = sys.executable
    os.execl(python, python, *sys.argv)


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
        3. Each enemy ship consists of 1 square only
        4. The gameboard consists of 64 squares
        5. You must chose which square to attack using coordinates
        6. Pick a row from 1 - 8 and Column A - H
        7. If you select correctly you destroy 1 enemy ship
        8. A direct hit is represented by X and a miss by -
        9. Unselected squares are represented by a blank space
        10. You have 25 turns to destroy all ememy ships or you lose
        11. You gain 2 turns for direct hit & lose 1 turn for a miss
            
        Have fun!!!
        """
    )

    # Asks player if they are ready to play the game after reading game rules
    print('Are you ready to play the game?')
    answer = input('Enter Y or N: \n').upper()
    print('')

    while True:
        if answer == 'Y':
            # Runs the main game functions
            main()
            break         
        elif answer == 'N':
            print('Please read game rules again and press run program')
            return False
        else: 
            print('Please enter Y or N')
            answer = input('Enter Y or N: \n').upper()


def main():
    """
    Runs all the main battleship game functions including the 
    printing of the gameboard, the creation of randonly placed
    enemy ships, which locations the player will attack and 
    counts the number of ships the player has hit.
    """

    # Converting letters to numbers
    convert_letters = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
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
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            while board[ship_row][ship_column] == 'X':
                ship_row, ship_column = ship_location()
            board[ship_row][ship_column] = 'X'

    def ship_location():
        """
        Ask the player which row (1-8) and column (A-H) they wish to guess.
        """
        row = input('Please enter ship row number from 1 - 8: ')
        while row not in '12345678':
            print('Please enter a vaid number')
            row = input('Please enter ship row number from 1 - 8: ')
        column = input('Please enter a ship column letter A - H: ').upper()
        while column not in 'ABCDEFGH':
            print('Please enter a valid letter')
            column = input('Please enter a ship column letter A - H: ').upper()
        return int(row) - 1, convert_letters[column]

    def ship_hit_counter(board): 
        """
        Counts how many ships player has hit.
        If player hits 10 ships before using all turns, they win.
        """
        count = 0
        for row in board:
            for column in row:
                if column == 'X':
                    count += 1
        return count

    """
    While loop where player has 25 turns to guess ship locations.
    Messages are displayed depending on whether player has guessed
    correctly or incorrectly. Loop will run until player has used
    all 25 turns.
    """
    if __name__ == "__main__":
        random_ships(YOURBOARD)
        turns = 25
        while turns > 0:
            print_gameboard(ENEMYBOARD)
            row, column = ship_location()
            if ENEMYBOARD[row][column] == '-':
                print(' ')
                print('You have already guessed that')
                print(' ')
            elif YOURBOARD[row][column] == 'X':
                print(' ')
                print('Well Done, that is a direct hit!!!')
                print('You have gained 2 turns!!!')
                print(' ')
                ENEMYBOARD[row][column] = 'X'
                turns += 2
            else:
                print(' ')
                print('Sorry, that was not a direct hit!!!')
                print('You have lost 1 turn!!! ')
                print(' ')
                ENEMYBOARD[row][column] = '-'
                turns -= 1
            if ship_hit_counter(ENEMYBOARD) == 10:
                print(' ')
                print('Congratulations, you have hit all targets!!!')
                print('You are the winner!!! ')
                print(' ')
                break
            print('You have ' + str(turns) + ' turns remaining')
            print(' ')
            if turns == 0:
                print(' ')
                print('Sorry, you ran out of turns, the game is over')
                print(' ')
                break


def restart():
    """
    Asks the user if they would like to replay the game once finished.
    Different messages are displayed depending on their decision.
    """
    print(' ')
    print('Would you like to play once more?')
    answer = input('Enter Y or N: \n').upper()
    while True:        
        if answer == "N":
            print(' ')
            print('Thank you for playing and goodbye!!!')
            print(' ')
            sys.exit(0)
        elif answer == "Y":
            reset_display()
            print("Starting new game")        
            run_game()
        else: 
            print('Please Enter Y or N')
            answer = input('Enter Y or N: \n').upper()


def run_game():
    """
    Starts a new game and runs main function
    """
    # Displays welcome message, battleship game rules and begins game
    start_menu()
    
    # Asks the user if they would like to replay the game once finished
    restart()


run_game()
