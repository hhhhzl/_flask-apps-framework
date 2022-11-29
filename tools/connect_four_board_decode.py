import numpy as np


def decode_connect_four(board_string, rows):
    column = int(len(board_string) / rows)
    board = np.zeros((rows, column), dtype=int)
    for i in range(len(board_string)):
        row = i // column
        col = i % column
        if board_string[i] == '1':
            board[row][col] = 1
        elif board_string[i] == '2':
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
