from os import system, name

board = [' '] * 10
player1_marker = ''
player2_marker = ''
player1_turn = True
player1_won = False
player2_won = False


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def make_marker_selection():
    global player1_marker
    global player2_marker
    while player1_marker != 'x' and player1_marker != 'o':
        player1_marker = input(
            "Please choose marker for player 1 ('x' or 'o') --> ")
        if player1_marker == 'x':
            player2_marker = 'o'
        elif player1_marker == 'o':
            player2_marker = 'x'


def dispay_board(board):
    clear()
    print()
    print(f"{board[1]} | {board[2]} | {board[3]} ")
    print(f"{board[4]} | {board[5]} | {board[6]} ")
    print(f"{board[7]} | {board[8]} | {board[9]} ")
    print()


def game_in_progress():
    result = False
    if player1_won or player2_won:
        return False
    for selection in board:
        if selection == ' ':
            result = True
            break
    return result


def is_valid_position(position):
    return position > 0 and position <= len(board) - 1 and board[position] == ' '


def update_board(position):
    global player1_turn
    global player1_won
    global player2_won

    if player1_turn:
        board[position] = player1_marker
        player1_won = check_game_result_for_marker(player1_marker)
        player1_turn = False
    else:
        board[position] = player2_marker
        player2_won = check_game_result_for_marker(player2_marker)
        player1_turn = True
    dispay_board(board)


def check_if_anybody_won():
    if player1_turn:
        pass


def check_game_result_for_marker(marker):
    # Vertical check
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True

    # Horizontal check
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True

    # Diagonal check
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


def reset_game():
    global board
    global player1_marker
    global player2_marker
    global player1_turn
    global player1_won
    global player2_won

    board = [' '] * 10
    player1_marker = ''
    player2_marker = ''
    player1_turn = True
    player1_won = False
    player2_won = False


def want_to_replay():
    choice = False
    replay = ''
    while replay != 'yes' and replay != 'no':
        replay = input("Do you wan't to play again? --> yes / no: ")
    if replay == 'yes':
        choice = True
    elif replay == 'no':
        choice = False
    return choice


def game_entry_point():
    global player1_marker
    global player2_marker
    global player1_won
    global player2_won

    while(game_in_progress()):

        if player1_marker == '':
            make_marker_selection()
            print(f"player 1 -> {player1_marker}")
            print(f"player 2 -> {player2_marker}")

        next_position = -1
        try:
            if player1_turn:
                next_position = int(input('Player1 turn [1 - 9]: '))
            else:
                next_position = int(input('Player2 turn [1 - 9]: '))
        except ValueError:
            pass

        if is_valid_position(next_position):
            update_board(next_position)
        else:
            print('Invalid postion! Retry.')

        if player1_won:
            print('Congrats! Player1 won the game')
        elif player2_won:
            print('Congrats! Player2 won the game')

        if player1_won or player2_won:
            choice = want_to_replay()
            if choice:
                reset_game()
            else:
                print('Good Bye! See you soon.')
    else:
        if player1_won != True and player2_won != True:
            print('Game is Tie!')
            choice = want_to_replay()
            if choice:
                reset_game()
                game_entry_point()
            else:
                print('Good Bye! See you soon.')


while(game_in_progress()):
    game_entry_point()
