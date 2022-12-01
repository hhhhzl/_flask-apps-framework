import numpy as np


def decode_connect_four(board_string):
    rows = int(board_string[0])
    string = board_string[1:]
    column = int(len(string) / rows)
    board = np.zeros((rows, column), dtype=int)
    for i in range(len(string)):
        row = i // column
        col = i % column
        if string[i] == '1':
            board[row][col] = 1
        elif string[i] == '2':
            board[row][col] = -1
    return board


def trans_connect_four(board):
    rows = board.shape[0]
    cols = board.shape[1]
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                board[i][j] = -1
            elif board[i][j] == -1:
                board[i][j] = 1


if __name__ == "__main__":
    print(decode_connect_four("000000000000000000000000000000000000011200", 6))
