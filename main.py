"""A two-player terminal tic-tac-toe game."""

WINS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def show(board):
    for row in range(0, 9, 3):
        print(" | ".join(board[row:row + 3]))
        if row < 6:
            print("---------")


def main():
    board = [str(number) for number in range(1, 10)]
    player = "X"
    moves = 0
    while moves < 9:
        show(board)
        try:
            position = int(input(f"{player}, choose 1-9: ")) - 1
            if position not in range(9) or board[position] in "XO":
                raise ValueError
        except ValueError:
            print("Choose an open position from 1 to 9.")
            continue
        board[position] = player
        moves += 1
        if any(all(board[index] == player for index in line) for line in WINS):
            show(board)
            print(f"{player} wins!")
            return
        player = "O" if player == "X" else "X"
    show(board)
    print("It is a draw.")


if __name__ == "__main__":
    main()
