from game import Game, Player
from time import sleep

game = Game()
while True:
    print("\n\n\n\n")


    for i in range(3):
        for ii in range(3):
            print(game.board[i][ii], end="|" if ii != 2 else "\n")
        print("-----" if i != 2 else "")

    if winner := game.won():
        print(f"{winner} won!")
        break

    move = game.bestMove()
    if move is None:
        print("No best move?")

    print(f"Putting {game.turn} in {move}.")
    row, column = move

    game.board[row][column] = game.turn
    game.turn = Player.O if game.turn == Player.X else Player.X

    sleep(0.5)