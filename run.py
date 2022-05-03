# Your ship locations
YOURBOARD = [[' '] * 10 for x in range(10)]
# Enemy ship where hits and misses are displayed
ENEMYBOARD = [[' '] * 10 for x in range(10)]

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