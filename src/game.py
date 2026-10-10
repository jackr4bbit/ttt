import math
from typing import Literal

class Player:
    X: Literal["X"] = "X"
    O: Literal["O"] = "O"

class Cell:
    X = Player.X
    O = Player.O
    Empty: Literal[" "] = " "

def minimax(game: Game, depth: int, maximizing: bool) -> float:
    if game.won():
        if game.won() == game.turn:
            return 1
        else:
            return -1

    if not all(cell == Cell.Empty for row in game.board for cell in row):
        return 0

    if maximizing:
        bestScore = -math.inf
        for row in range(3):
            for column in range(3):
                if game.board[row][column] == Cell.Empty:
                    game.board[row][column] = game.turn
                    score = minimax(game, depth + 1, False)
                    game.board[row][column] = Cell.Empty
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for row in range(3):
            for column in range(3):
                if game.board[row][column] == Cell.Empty:
                    game.board[row][column] = game.turn
                    score = minimax(game, depth + 1, True)
                    game.board[row][column] = Cell.Empty
                    bestScore = min(score, bestScore)
        return bestScore

class Game:
    def __init__(self):
        self.board = [[Cell.Empty for _ in range(3)] for _ in range(3)]
        self.turn = Player.X

    def won(self) -> Literal["X", "O"] | None:
        for row in self.board:
            if all(cell == row[0] for cell in row) and row[0] != Cell.Empty:
                return row[0]

        for column in range(3):
            check = self.board[0][column]
            if all(row[column] == check for row in self.board) and check != Cell.Empty:
                return check


        check = self.board[0][0]
        if all(self.board[i][i] == check for i in range(3)) and check != Cell.Empty:
            return check

        check = self.board[2][2]
        if all(self.board[-(i + 1)][-(i + 1)] == check for i in range(3)) and check != Cell.Empty:
            return check

        return None

    def bestMove(self) -> tuple[int, int] | None:
        move = None
        bestScore = -math.inf
        score = 0
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == Cell.Empty:
                    self.board[row][column] = self.turn
                    score = minimax(self, 0, False)
                    self.board[row][column] = Cell.Empty

                    if score > bestScore:
                        bestScore = score
                        move = (row, column)
        return move