class Player:
    def __init__(self, name, score, piece_type, turns):
        self.name = name
        self.score = score
        self.piece_type = piece_type
        self.turns = turns

def board_update(board : list[str], row : int, col : int, piece_type : str) -> bool:

    if col == len(board[row]):
        board[row] = board[row][:col] + piece_type + board[row][col+1]
    else:
        board[row] = board[row][:col] + piece_type + board[row][col+1:]

def check_board_win(board : list[str]) -> bool:

    win = False

    # each string is a coord (x,y) aka (row,col)
    ways_to_win = [
        ['00', '11', '22'],
        ['02', '11', '20'],
        ['00', '01', '02'],
        ['10', '11', '12'],
        ['20', '21', '22'],
        ['00', '10', '20'],
        ['01', '11', '21'],
        ['02', '12', '22'],
    ]

    for ways in ways_to_win:
        x_counter = 0
        o_counter = 0
        for way in ways:
            if board[int(way[0])][int(way[1])] == 'x':
                x_counter += 1
            elif board[int(way[0])][int(way[1])] == 'o':
                o_counter += 1
        if x_counter == 3 or o_counter == 3:
            win = True

    return win

def valid_player_input(board : list[str], s : str) -> bool:

    is_valid = True

    if len(s) != 2:
        is_valid = False
    else:
        for c in s:
            if c.isalpha():
                is_valid = False
            elif int(c) > 2 or int(c) < 0:
                is_valid = False
        
        if is_valid != False:
            if board[int(s[0])][int(s[1])] != '-':
                is_valid = False

    return is_valid

def print_board(board : list[str]):

    for row in board:
        print(row)

def main():

    player_one_name = input("Enter username for Player One: ")
    player_one_score = 0
    player_one_piece_type = 'x'
    player_one_turns = 0
    player_two_name = input("Enter username for Player Two: ")
    player_two_score = 0
    player_two_piece_type = 'o'
    player_two_turns = 0

    player_one = Player(player_one_name, player_one_score, player_one_piece_type, player_one_turns)
    player_two = Player(player_two_name, player_two_score, player_two_piece_type, player_two_turns)

    game_board = [
        '---',
        '---',
        '---'
    ]

    in_game = True
    player_turn = player_one

    print("Welcome to Tic Tac Toe!")

    while in_game:

        if player_one_turns <= player_two_turns:
            player_one_turns += 1
            player_turn = player_one
        else:
            player_two_turns += 1
            player_turn = player_two
        
        valid_input = True

        if player_turn == player_one:
            while valid_input:
                print(player_one.name + "'s turn: ")
                print_board(game_board)
                player_move = input("Enter a position to place your piece " + player_one.name + ": ")
                if valid_player_input(game_board, player_move):
                    valid_input = False
        else:
            while valid_input:
                print(player_two.name + "'s turn: ")
                print_board(game_board)
                player_move = input("Enter a position to place your piece " + player_two.name + ": ")
                if valid_player_input(game_board, player_move):
                    valid_input = False

        move_coords = []

        for c in player_move:
            move_coords.append(int(c))

        if player_turn == player_one:
            board_update(game_board, move_coords[0], move_coords[1], player_one_piece_type)
        else:
            board_update(game_board, move_coords[0], move_coords[1], player_two_piece_type)

        print_board(game_board)

        if check_board_win(game_board):
            if player_turn == player_one:
                print(player_one.name + ' has won!')
            else:
                print(player_two.name + ' has won!')
            in_game = False

if __name__ == "__main__":
    main()