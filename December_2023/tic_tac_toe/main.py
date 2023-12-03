class Player:
    def __init__(self, name, score, piece_type, turns):
        self.name = name
        self.score = score
        self.piece_type = piece_type
        self.turns = turns

def is_valid_move(board : list[str], row : str, col : str) -> bool:

    valid_move = True

    if row.isalpha() or col.isalpha():
        valid_move = False
    else:
        row = int(row)
        col = int(col)
        if row > 2 or row < 0 or col > 2 or col < 0:
            valid_move = False
        elif board[row][col] != '-':
            valid_move = False

    return valid_move

def board_update(board : list[str], row : int, col : int, piece_type : str) -> bool:

    if col == len(board[row]):
        board[row] = board[row][:col] + piece_type + board[row][col+1]
    else:
        board[row] = board[row][:col] + piece_type + board[row][col+1:]

def check_board_win(board : list[str]) -> bool:

    win = False

    # ways_to_win = [
    #     [[0,0], [1,1], [2,2]],
    #     [[0,2], [1,1], [2,0]],
    #     [[0,0], [0,1], [0,2]],
    #     [[1,0], [1,1], [1,2]],
    #     [[2,0], [2,1], [2,2]],
    #     [[0,0], [1,0], [2,0]],
    #     [[0,1], [1,1], [2,1]],
    #     [[0,2], [1,2], [2,2]],
    # ]

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
            print(player_one.name + "'s turn: ")
            player_one_turns += 1
            player_turn = player_one
        else:
            print(player_two.name + "'s turn: ")
            player_two_turns += 1
            player_turn = player_two

        print_board(game_board)
        
        if player_turn == player_one:
            player_move = input("Enter a position to place your piece " + player_one.name + ": ")
        else:
            player_move = input("Enter a position to place your piece " + player_two.name + ": ")

        move_coords = []

        for c in player_move:
            move_coords.append(c)

        if is_valid_move(game_board, move_coords[0], move_coords[1]):
            
            temp_coords = []
            for i in move_coords:
                temp_coords.append(int(i))
            move_coords.clear()
            move_coords += temp_coords

            if player_turn == player_one:
                board_update(game_board, move_coords[0], move_coords[1], player_one_piece_type)
            else:
                board_update(game_board, move_coords[0], move_coords[1], player_two_piece_type)
        else:
            print("That's not a valid move! You lost a turn RIP")

        print_board(game_board)

        if check_board_win(game_board):
            print('Game done')
            in_game = False

if __name__ == "__main__":
    main()