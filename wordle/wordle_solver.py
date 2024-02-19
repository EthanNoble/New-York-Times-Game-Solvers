import argparse

YELLOW = 0 # The letter is in the word but is not in the correct position
GREEN = 1 # The letter is in the word and is in the correct position
BLACK = 2 # The letter is not in the word
BLANK = 3 # The tile is empty

# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Wordle Solver')

    parser.add_argument('-w', type=str, nargs='+',
        help='List of the words that have already been played')

    parser.add_argument('-r', type=str, nargs='+',
        help='''List of the rule sets for each word specified
        in -w (e.g. if word has two yellow letters in positions
        1 & 2, one green tile in 3, and two black tiles in 4 & 
        5 -> "yygbb")''')

    parser.add_argument('-o', type=str,
        help='''Output file to write the valid words to. If no output
        file is specified, the valid words will be printed to the console.''')

    return parser.parse_args()


# Validate command line arguments
def validate_args(args) -> None:
    if not args.w or not args.r:
        raise ValueError('-w and -r arguments are required.')
    if len(args.w) != len(args.r):
        raise ValueError('The number of words and rule sets strings must be equal.')
    if len(args.w) > 6 or len(args.r) > 6:
        raise ValueError('6 words!? You\'v already lost! ;)')
    
# Take a list of ['bbgyb', 'bggyy'] and convert it to a list of
# [[BLACK, BLACK, GREEN, YELLOW, BLACK], [BLACK, GREEN, GREEN, YELLOW, YELLOW]]
def convert_rules_to_consts(rules: list) -> list:
    consts = []

    for index, rule_set in enumerate(rules):
        consts.append([])
        for rule in rule_set:
            if rule == 'y':
                consts[index].append(YELLOW)
            elif rule == 'g':
                consts[index].append(GREEN)
            elif rule == 'b':
                consts[index].append(BLACK)
    
    return consts


# Return a set of words matching the yellow, green, and grey tile constraints
def get_next_valid_words(board: list, words: set) -> set:
    yellow_letters = set() # Contains tuples of (letter, index)
    green_letters = set() # Contains tuples of (letter, index)
    grey_letters = set() # Contains just letters

    for row in board:
        for index, tile in enumerate(row):
            if (tile[1] == YELLOW):
                yellow_letters.add((tile[0], index))
            elif (tile[1] == GREEN):
                green_letters.add((tile[0], index))
            elif (tile[1] == BLACK):
                grey_letters.add(tile[0])
    
    next_valid_words = set()
    for word in words:
        valid_word = True

        for letter in grey_letters:
            if letter in word:
                valid_word = False
                break
        for tile in yellow_letters:
            letter = tile[0]
            index = tile[1]
            if letter not in word or index == word.index(letter):
                valid_word = False
                break
        for tile in green_letters:
            letter = tile[0]
            index = tile[1]
            if letter not in word or index != word.index(letter):
                valid_word = False
                break

        if valid_word:
            next_valid_words.add(word)
    
    return next_valid_words


# Insert word and tile constraints into the board
def update_board(board: list, word: list, rules: list) -> None:
    # Find the first empty row
    row_index = None
    for i in range(len(board)):
        if board[i][0][1] == BLANK:
            row_index = i
            break
    
    # Insert the word and rules into the board
    board[row_index] = list(zip(word, rules))


def print_board(board: list) -> None:
    print('-' * 9)
    for row in board:
        print(' '.join([f'{element[0]}' for element in row]))
    print('-' * 9)


if __name__ == '__main__':
    args = parse_args()
    validate_args(args)

    with open('./../english_words.txt', 'r') as file:
        words = set(file.read().split())
        words = {word for word in words if len(word) == 5}
    
    # Setup Wordle board
    game_board = [ [('', BLANK) for _ in range(5)] for _ in range(6)]

    # Define the word and word rules of the played words based on
    # the command line arguments passed by the user
    # --- Example of played_words ---
    # played_words = [
    #     (list('audio'), [BLACK, BLACK, GREEN, YELLOW, BLACK]),
    #     (list('cider'), [BLACK, GREEN, GREEN, YELLOW, YELLOW])
    # ]
    played_words = list(
        zip(
            [list(word) for word in args.w],
            convert_rules_to_consts(args.r)
        )
    )

    # Insert the word and rules of each played_words entry into the board
    for word, rules in played_words:
        update_board(game_board, word, rules)

    # Return a set of valid words conforming to the game board's rules
    valid_words = get_next_valid_words(game_board, words)
    
    # Output the possible solution words to a file if -o is specified
    print(f'Found {len(valid_words)} possible solution words.')
    if args.o:
        print('Writing to file...')
        with open(args.o, 'w') as file:
            for word in valid_words:
                file.write(f'{word}\n')
    else: # -o not specified, write to console
        print(f'Words: {valid_words if len(valid_words) > 0 else "No valid words found"}')
