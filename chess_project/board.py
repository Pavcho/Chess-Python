class Board:
    def __init__(self):
        self.board = [
            [".", ".", ".", ".", ".", ".", "K", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", ".", ".", ".", ".", "q", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
        ]

    def print_board(self):
        for row in range(8):
            for col in range(8):
                print(self.board[row][col], end=" ")
            else:
                print()
        print()


c_board = Board()


