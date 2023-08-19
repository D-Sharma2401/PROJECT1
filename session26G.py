class ChessGame:
    def __init__(self):
        self.board = self.setup_board()
        self.current_player = 'white'

    def setup_board(self):
        board = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
        return board

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def make_move(self, move):
        from_pos, to_pos = move
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = ' '

        self.current_player = 'white' if self.current_player == 'black' else 'black'

    def play(self):
        while True:
            self.display_board()
            print(f"{self.current_player.capitalize()}'s turn")

            from_square = input("Enter the source square (e.g., 'e2'): ")
            to_square = input("Enter the target square (e.g., 'e4'): ")

            from_pos = self.square_to_position(from_square)
            to_pos = self.square_to_position(to_square)

            move = (from_pos, to_pos)
            self.make_move(move)

    def square_to_position(self, square):
        col = ord(square[0]) - ord('a')
        row = int(square[1]) - 1
        return row, col


if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.play()
