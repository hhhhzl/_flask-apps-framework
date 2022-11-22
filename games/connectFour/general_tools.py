import numpy as np


class GeneralRubric:
    FIRST_PLAYER = 1
    SECOND_PLAYER = -1
    player = {2: -1, 1: 1}
    gameState = {"FIND_WINNER": 1, "CONTINUE": 0, "TIE": 2}

    def __init__(self):
        self.whichPlayer = None

    def is_terminate(self, board, number_to_win, player1Steps=None, player2Steps=None):
        if player2Steps is None or player2Steps is None:
            self.check_which_player(board)
        elif player2Steps is not None and player2Steps is not None:
            self.check_which_player(board, player1Steps, player2Steps)

        if self.is_horizontal_win(board, number_to_win) or self.is_vertical_win(board, number_to_win) or self.is_upDiagonal_win(board, number_to_win) or self.is_downDiagonal_win(board, number_to_win):
            return self.gameState["FIND_WINNER"]
        else:
            if self.is_board_full(board):
                return self.gameState["TIE"]
            else:
                return self.gameState["CONTINUE"]

    def check_valid_position(self, board):
        valid_locations = []
        column = board.shape[1]
        for col in range(column):
            if board[0][col] == 0:
                valid_locations.append(col)
        return valid_locations

    def check_col_valid(self, board, col):
        if board[0][col] == 0:
            return True
        else:
            return False

    def winning_move(self):
        pass

    def make_move(self, board, column):
        if self.whichPlayer is None:
            self.check_which_player(board)

        if self.check_col_valid(board, column):
            rows = board.shape[0]
            iteration = 1
            while board[rows - iteration][column] != 0:
                iteration += 1
            board[rows - iteration][column] = self.player[self.whichPlayer]


    def redo_last_step(self):
        pass

    def check_which_player(self, board, first_player_count=None, second_player_count=None):
        if first_player_count is None and second_player_count is None:
            rows = board.shape[0]
            column = board.shape[1]
            player1 = 0
            player2 = 0
            for i in range(rows):
                for j in range(column):
                    if board[i][j] == self.FIRST_PLAYER:
                        player1 += 1
                    elif board[i][j] == self.SECOND_PLAYER:
                        player2 += 1

            if player1 > player2:
                self.whichPlayer = 2
            elif player1 == player2:
                self.whichPlayer = 1

        else:
            if first_player_count > second_player_count:
                self.whichPlayer = 2
            elif first_player_count == second_player_count:
                self.whichPlayer = 1

    def is_horizontal_win(self, board, number_to_win):
        if self.whichPlayer is None:
            self.check_which_player(board)
        rows = board.shape[0]
        column = board.shape[1]
        for i in range(rows):
            for j in range(column-number_to_win):
                total_sum = 0
                if board[rows-1-i][j] != 0:
                    for item in range(number_to_win):
                        total_sum += board[rows - 1 - i][j + item]
                    if total_sum == number_to_win * self.player[3 - self.whichPlayer]:
                        return True
        return False

    def is_vertical_win(self, board, number_to_win):
        if self.whichPlayer is None:
            self.check_which_player(board)
        rows = board.shape[0]
        column = board.shape[1]
        for i in range(rows-number_to_win+1):
            for j in range(column):
                total_sum = 0
                if board[rows - 1 - i][j] != 0:
                    for item in range(number_to_win):
                        total_sum += board[rows - 1 - i - item][j]
                    if total_sum == number_to_win * self.player[3 - self.whichPlayer]:
                        return True
        return False

    def is_downDiagonal_win(self, board, number_to_win):
        if self.whichPlayer is None:
            self.check_which_player(board)
        rows = board.shape[0]
        column = board.shape[1]
        for i in range(rows - number_to_win + 1):
            for j in range(column - number_to_win + 1):
                total_sum = 0
                if board[i][j] != 0:
                    for item in range(number_to_win):
                        total_sum += board[i + item][j + item]
                    if total_sum == number_to_win * self.player[3 - self.whichPlayer]:
                        return True
        return False

    def is_upDiagonal_win(self, board, number_to_win):
        if self.whichPlayer is None:
            self.check_which_player(board)
        rows = board.shape[0]
        column = board.shape[1]
        for i in range(rows - number_to_win):
            for j in range(column - number_to_win):
                total_sum = 0
                if board[rows - 1 - i][j] != 0:
                    for item in range(number_to_win):
                        total_sum += board[rows - 1 - i - item][j + item]
                    if total_sum == number_to_win * self.player[3 - self.whichPlayer]:
                        return True
        return False

    def is_board_full(self, board):
        rows = board.shape[0]
        column = board.shape[1]
        for i in range(rows):
            for j in range(column):
                if board[i][j] == 0:
                    return False
        return True


if __name__ == "__main__":
    Board = np.zeros((6, 7), dtype=int)
    for i in '0616263':
        GeneralRubric().make_move(Board, int(i))
    print(Board)
    print(GeneralRubric().is_terminate(Board, 4))
    pass
