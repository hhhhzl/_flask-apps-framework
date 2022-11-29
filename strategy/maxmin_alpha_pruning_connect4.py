import numpy as np

from games.connectFour.general_tools import GeneralRubric
from tools.connect_four_board_decode import trans_connect_four
import math
import random


class MaxMin(GeneralRubric):
    scoreEV = [100, 5, 2, 4]

    def __init__(self):
        super().__init__()
        self.player_to_play = None
        self.score = None
        self.output = None

    def runMinMax(self, board, depth, number_to_win=4):
        self.initial_which_player(board)

        must_win = self.must_win_move(board, number_to_win)
        must_block = self.must_block_move(board, number_to_win)
        if must_win is not None:
            self.output = must_win
        elif must_block is not None:
            self.output = must_block
        # else:
        #     self.output = random.choice([0,1,2,3,4,5,6])
        else:
            col, minimax_score = self.max_min(board, depth, True, -math.inf, math.inf, number_to_win)
            self.score = minimax_score
            self.output = col

    def initial_which_player(self, board):
        self.check_which_player(board)
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
            self.player_to_play = 2
        elif player1 == player2:
            self.player_to_play = 1

    def max_min(self, board, depth, maxingPlayer, alpha, beta, number_to_win=4):
        valid_positions = self.check_valid_position(board)
        is_terminal = self.is_terminate(board, number_to_win)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.is_terminate(board, number_to_win, player=self.player_to_play):
                    return [None, 100000000000000]
                elif self.is_terminate(board, number_to_win, player=3 - self.player_to_play):
                    return [None, -10000000000000]
                else:  # Game is over, no more valid moves
                    return None, 0
            elif depth == 0:  # Depth is zero
                return [None, self.score_position(board, self.player_to_play, number_to_win)]

        if maxingPlayer:
            value = -math.inf
            column = random.choice(valid_positions)
            for col in valid_positions:
                b_copy = board.copy()
                self.make_move(b_copy, col)
                new_score = self.max_min(b_copy, depth - 1, False, alpha, beta, number_to_win)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_positions)
            for col in valid_positions:
                b_copy = board.copy()
                self.make_move(b_copy, col)
                new_score = self.max_min(b_copy, depth - 1, True, alpha, beta, number_to_win)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def score_position(self, board, playerCheck, number_to_win):
        score = 0
        rows = board.shape[0]
        columns = board.shape[1]

        ## Score center column
        center_array = [int(i) for i in list(board[:, columns // 2])]
        center_count = center_array.count(self.player[playerCheck])
        score += center_count * 3

        ## Score Horizontal
        for r in range(rows):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(columns - number_to_win + 1):
                window = row_array[c:c + number_to_win]
                score += self.evaluate_window(window, playerCheck)

        ## Score Vertical
        for c in range(columns):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(rows - number_to_win + 1):
                window = col_array[r:r + number_to_win]
                score += self.evaluate_window(window, playerCheck)

        ## Score posiive sloped diagonal
        for r in range(rows - number_to_win + 1):
            for c in range(columns - number_to_win + 1):
                window = [board[r + i][c + i] for i in range(number_to_win)]
                score += self.evaluate_window(window, playerCheck)

        for r in range(rows - number_to_win + 1):
            for c in range(columns - number_to_win + 1):
                window = [board[r + 3 - i][c + i] for i in range(number_to_win)]
                score += self.evaluate_window(window, playerCheck)

        return score

    def evaluate_window(self, window, playerCheck):
        score = 0

        if window.count(self.player[playerCheck]) == 4:
            score += self.scoreEV[0]
        elif window.count(self.player[playerCheck]) == 3 and window.count(0) == 1:
            score += self.scoreEV[1]
        elif window.count(self.player[playerCheck]) == 2 and window.count(0) == 2:
            score += self.scoreEV[2]

        if window.count(self.player[playerCheck]) == 3 and window.count(0) == 1:
            score -= self.scoreEV[3]

        return score

    def must_win_move(self, board, number_to_win):
        valid_positions = self.check_valid_position(board)
        col = None
        for each_position in valid_positions:
            b_copy = board.copy()
            self.make_move(b_copy, each_position)
            gameState = self.is_terminate(b_copy, number_to_win, self.player_to_play)
            if gameState == 1:
                col = each_position
                break
        return col

    def must_block_move(self, board, number_to_win):
        valid_positions = self.check_valid_position(board)
        col = None
        for each_position in valid_positions:
            b_copy = board.copy()
            trans_connect_four(b_copy)
            self.make_move(b_copy, each_position)
            gameState = self.is_terminate(b_copy, number_to_win, self.player_to_play)
            if gameState == 1:
                col = each_position
                break
        return col


if __name__ == "__main__":
    board = np.zeros((6, 7), dtype=int)
    board[3][2] = 1
    game = MaxMin()
