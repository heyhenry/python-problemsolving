board = [
    '----',
    '--Q-',
    '----'
]

# for row in board:
#     print(row)

counter = 0

while counter < 3:
    player_move = input("Choose a spot to place x (in numbers provide row,col (i.e. 01)): ")

    move_coords = []

    for c in player_move:
        move_coords.append(int(c))

    # color will represent what object to update board with
    def board_update(board : list[str], row : int, col : int, color : str) -> list[str]:

        if color == 'red':
            board[row] = board[row][:col] + 'x' + board[row][col+1:]
        else:
            board[row] = board[row][:col] + 'o' + board[row][col+1:]

        return board

    board_update(board, move_coords[0], move_coords[1], 'red')
    
    for row in board:
        print(row)
    counter += 1
