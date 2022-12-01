import numpy as np
import os
from games.connectFour.general_tools import GeneralRubric
from tools.connect_four_board_decode import trans_connect_four
import math
import random


def player_table_search(player, route):
    number_return = None
    s_compare = ''
    for i in range(len(route)):
        s_compare += str(int(route[i]) + 1)
    number_compare = len(route)
    if player == 1:
        # filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'depth_8_back.txt'))
        # with open(filename, 'r') as file:
        #     temp = file.read().splitlines()
        #     for line in temp:
        #         if line[:number_compare] == s_compare:
        #             number_return = int(line[number_compare]) - 1
        #             break
        # file.close()
        return number_return
    elif player == 2:
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'depth_8_back.txt'))
        with open(filename, 'r') as file:
            temp = file.read().splitlines()
            for line in temp:
                if line[:number_compare] == s_compare:
                    number_return = int(line[number_compare]) - 1
                    break
        file.close()
        return number_return


def check_table_input(board, player):
    rows = board.shape[0]
    column = board.shape[1]
    new_board = np.zeros((rows, column), dtype=int)
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gamePlayRecord.txt'))
    with open(filename, 'a+') as file:
            temp = file.read().splitlines()
            if temp:
                for i in temp[-1]:
                    GeneralRubric().make_move(new_board, int(i))
            wrong_spot = 0
            empty = 0
            for row in range(rows):
                for col in range(column):
                    if board[row][col] != new_board[row][col]:
                        wrong_spot += 1
                        opp_row = col
                    if board[row][col] != 0:
                        empty += 1
            if empty == 0:
                file.write("\n")
                file.close()
                return empty, ''
            elif empty == 1 and wrong_spot == 1:
                last_line = str(opp_row)
                file.write(str(opp_row))
                return empty, last_line
            elif wrong_spot == 1 and empty > 1:
                last_line = temp[-1] + str(opp_row)
                file.write(str(opp_row))
                file.close()
                return empty, last_line
            elif wrong_spot > 1 or wrong_spot < 1:
                file.close()
                return 10000, None
            else:
                file.write("")
                file.close()
                return 0, ''


class MaxMin(GeneralRubric):
    scoreEV = [100, 5, 2, 4]

    def __init__(self):
        super().__init__()
        self.player_to_play = None
        self.score = None
        self.output = None

    def runMinMax(self, board, depth, iteration=10000, play_route=None, number_to_win=4, http=False):
        self.initial_which_player(board)
        # if http:
        #     iteration, play_route = check_table_input(board, self.player_to_play)
        must_win = self.must_win_move(board, number_to_win)
        must_block = self.must_block_move(board, number_to_win)
        if must_win is not None:
            self.output = must_win
        elif must_block is not None:
            self.output = must_block
        else:
            if iteration == 0:
                self.output = 3
            elif iteration < 6:
                self.output = player_table_search(self.player_to_play, play_route)
                if self.output is None:
                    col, minimax_score = self.max_min(board, depth, True, -math.inf, math.inf, number_to_win)
                    self.score = minimax_score
                    self.output = col
            else:
                col, minimax_score = self.max_min(board, depth, True, -math.inf, math.inf, number_to_win)
                self.score = minimax_score
                self.output = col
        # if http:
        #     filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gamePlayRecord.txt'))
        #     with open(filename, 'a+') as file:
        #         print(self.output)
        #         file.write(str(self.output))

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
