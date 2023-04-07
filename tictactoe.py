BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}

COL_WHITE = '\033[1;97m'
COL_RED = '\033[1;91m'
COL_GREEN = '\033[1;92m'


def render(player):
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    board_state = " "
    
    for i in range(9):
        cell = BOARD[i + 1]
        board_state += cell + (" | " if (i + 1) % 3 != 0 else "\n - + - + - \n ")
            
    #return board_state
    
    #returns board state with current player color
    return board_state.replace(
            player,(COL_RED if player == 'X' else COL_GREEN) + player + COL_WHITE)



def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    space = -1
    while True:
        space = int(input("Which space for "  + player + " (1-9)? "))
        if(space >= 1 and space <= 9 and BOARD[space] == ' '):
            break
        else:
            print("Invalid input")
    
    return space

def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    return render(player) + "Congratulations, Player " + player + ", you win!"

def check_win(player, scores):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'
    scores : list of scores

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    #Make sets for each line
    lines = []
    lines.append({BOARD[1], BOARD[2], BOARD[3]})
    lines.append({BOARD[4], BOARD[5], BOARD[6]})
    lines.append({BOARD[7], BOARD[8], BOARD[9]})
    lines.append({BOARD[1], BOARD[4], BOARD[7]})
    lines.append({BOARD[2], BOARD[5], BOARD[8]})
    lines.append({BOARD[3], BOARD[6], BOARD[9]})
    lines.append({BOARD[1], BOARD[5], BOARD[9]})
    lines.append({BOARD[3], BOARD[5], BOARD[7]})
    
    #If any line has only 1 element, the game is over
    for line in lines:
        if len(line) == 1 and ' ' not in line:
            print(victory_message(player))
            scores[0 if player == 'X' else 1] += 1
            return True
        
    return False
    

def play_t3(scores):
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    player = 'X'
    game_round = 0
    game_over = False

    while not game_over:
        print(render(player))

        action = get_action(player)

        BOARD[action] = player

        game_round += 1 
        print(f"Round {game_round}")

        if game_round >= 4 and check_win(player, scores):

                game_over = True
                break

        if(game_round == 9 and ' ' not in BOARD):
            print(render(player) + "Tie")
            game_over = True
            break

        player = 'X' if player == 'O' else 'O'


    restart = input("restart? y/n: ").lower()
    if(restart == "y"):
        for i in range(9):
            BOARD[i + 1] = ' '
        play_t3(scores)
    else:
        return scores
