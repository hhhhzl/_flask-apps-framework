import numpy as np
import logging
from general_tools import GeneralRubric
from strategy.maxmin_alpha_pruning_connect4 import MaxMin
import math


class gameEngine(GeneralRubric):
    PLAYER_TYPE = {"human": True, "robot": False}

    def __init__(self, rows=6, columns=7, number_to_win=4, player1="human", player2="robot", player1S="max_min",
                 player2S="max_min"):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.number_to_win = number_to_win
        self.board = np.zeros((rows, columns), dtype=int)
        self.player1 = self.PLAYER_TYPE[player1.lower()]
        self.player2 = self.PLAYER_TYPE[player2.lower()]
        self.player1Steps = 0
        self.player2Steps = 0
        self.winner = None

        if self.player1:
            self.player1Strategy = None
        else:
            self.player1Strategy = player1S

        if self.player2:
            self.player2Strategy = None
        else:
            self.player2Strategy = player2S

    def start_game(self, d1, d2):
        which_player = 0
        while self.is_terminate(self.board, self.number_to_win, None, self.player1Steps, self.player2Steps) == 0:
            if self.player1Steps > self.player2Steps:
                which_player = 2
            elif self.player1Steps == self.player2Steps:
                which_player = 1

            if which_player == 1:
                # if player is human
                if self.player1:
                    valid_move = self.check_valid_position(self.board)
                    number = int(input("Player1 please enters a number to next move: ")) - 1
                    while number not in valid_move and valid_move != []:
                        number = int(input("inValid column, please reenter: ")) - 1

                    self.make_move(self.board, number)
                else:
                    if self.player1Strategy == "max_min":
                        player1 = MaxMin()
                        player1.runMinMax(self.board, d1, self.number_to_win)
                        number = player1.output
                        self.make_move(self.board, number)
                        # col, minimax_score = minimax(self.board, 8, -math.inf, math.inf, True)
                        # print(col)
                        # self.make_move(self.board, col)

                print(self.draw_aboard())
                self.player1Steps += 1

            else:
                if self.player2:
                    valid_move = self.check_valid_position(self.board)
                    number = int(input("Player2 please enters a number to next move: ")) - 1
                    while number not in valid_move and valid_move != []:
                        number = int(input("inValid column, please reenter: ")) - 1

                    self.make_move(self.board, number)

                else:

                    if self.player2Strategy == "max_min":
                        print(f"AI is thinking........")
                        player2 = MaxMin()
                        player2.runMinMax(self.board, d2, self.number_to_win)
                        number = player2.output
                        self.make_move(self.board, number)

                print(self.draw_aboard())
                self.player2Steps += 1

        if self.is_terminate(self.board, self.number_to_win, None, self.player1Steps, self.player2Steps) == 2:
            print("Tie Game!")
            self.winner = 0
        else:
            if which_player == 1:
                print("Player 1 win!")
                self.winner = 1
            elif which_player == 2:
                print("Player 2 win!")
                self.winner = 2

    def restart_game(self):
        self.board = np.zeros((self.rows, self.rows), dtype=int)
        self.player1Steps = 0
        self.player2Steps = 0
        self.winner = None
        self.start_game()

    def draw_aboard(self):
        s = ''
        s += "|"
        for i in range(self.columns):
            s += " " + str(i + 1) + " |"
        s += "\n"
        s += "="
        for i in range(self.columns):
            s += "===="
        s += "\n"
        for i in range(self.rows):
            s += "|"
            for j in range(self.columns):
                if self.board[i][j] == 1:
                    s += " " + "X" + " |"
                elif self.board[i][j] == -1:
                    s += " " + "O" + " |"
                else:
                    s += " " + " " + " |"
            s += "\n"
        return s

    # to do
    def redo_game(self):
        pass


if __name__ == "__main__":
    #  test
    # result = []
    # winner1 = 0
    # winner2 = 0
    # tie = 0
    # for i in range(1):
    #     game = gameEngine()
    #     game.start_game(5, 8)
    #     if game.winner == 1:
    #         winner2 += 1
    #     elif game.winner == 2:
    #         winner1 += 1
    #     else:
    #         tie += 1
    #
    # for i in range(1):
    #     game = gameEngine()
    #     game.start_game(8, 5)
    #     if game.winner == 1:
    #         winner1 += 1
    #     elif game.winner == 2:
    #         winner2 += 1
    #     else:
    #         tie += 1
    #
    # result.append(winner1)
    # result.append(tie)
    # result.append(winner2)
    # print(result)
    game = gameEngine()
    game.start_game(8, 5)

