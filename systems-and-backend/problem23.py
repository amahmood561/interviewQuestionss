'''
This problem was asked by Salesforce.

Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid. The game ends either when one player creates a line of four consecutive discs of their color (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.

Design and implement Connect 4.
'''


class Connect4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'Red'  # Alternates between 'Red' and 'Black'
    
    def print_board(self):
        for row in self.board:
            print("|", end="")
            for cell in row:
                if cell is None:
                    print(" . ", end="")
                else:
                    print(f" {cell[0]} ", end="")  # Print the first letter of the player's color
            print("|")
        print(" " + "   ".join([str(i) for i in range(self.cols)]))

    def drop_disc(self, col):
        for row in reversed(range(self.rows)):
            if self.board[row][col] is None:
                self.board[row][col] = self.current_player
                return row, col
        return None, None  # Column is full

    def check_win(self, row, col):
        return (self.check_direction(row, col, 1, 0) + self.check_direction(row, col, -1, 0) >= 3 or  # Horizontal
                self.check_direction(row, col, 0, 1) + self.check_direction(row, col, 0, -1) >= 3 or  # Vertical
                self.check_direction(row, col, 1, 1) + self.check_direction(row, col, -1, -1) >= 3 or  # Diagonal \
                self.check_direction(row, col, 1, -1) + self.check_direction(row, col, -1, 1) >= 3)    # Diagonal /
    
    def check_direction(self, row, col, row_dir, col_dir):
        count = 0
        color = self.board[row][col]
        r, c = row + row_dir, col + col_dir
        while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == color:
            count += 1
            r += row_dir
            c += col_dir
        return count
    
    def is_full(self):
        return all(self.board[0][col] is not None for col in range(self.cols))
    
    def switch_player(self):
        self.current_player = 'Black' if self.current_player == 'Red' else 'Red'
    
    def play_game(self):
        print("Welcome to Connect 4!")
        self.print_board()
        
        while True:
            col = int(input(f"{self.current_player}'s turn. Choose a column (0-{self.cols-1}): "))
            
            if col < 0 or col >= self.cols or self.board[0][col] is not None:
                print("Invalid move. Try again.")
                continue
            
            row, col = self.drop_disc(col)
            self.print_board()

            if self.check_win(row, col):
                print(f"{self.current_player} wins!")
                break
            elif self.is_full():
                print("It's a draw!")
                break
            
            self.switch_player()

if __name__ == "__main__":
    game = Connect4()
    game.play_game()


'''
Board Initialization:

The board is initialized as a 6x7 grid with all cells set to None to represent empty spots.
Move Execution:

The drop_disc function places a disc in the lowest available row of the chosen column.
Win Check:

The check_win function checks if the last move resulted in four consecutive discs. It checks in four directions: horizontal, vertical, and the two diagonal directions.
Switching Players:

The switch_player function alternates between 'Red' and 'Black' after each turn.
Game Loop:

The play_game function runs the game loop where players take turns until there is a winner or the board is full (resulting in a draw).

'''