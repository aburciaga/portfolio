import time
import random  # Importing the random module

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]
        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[1][1] == self.current_state[2][2]):
            return self.current_state[0][0]
        
        # Anti-diagonal win
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[1][1] == self.current_state[2][0]):
            return self.current_state[0][2]

        return None  # No winner yet

    def max(self):
        maxv = -2
        px = None
        py = None
        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '.'
        return (maxv, px, py)

    def min(self):
        minv = 2
        qx = None
        qy = None
        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'
        return (minv, qx, qy)

    def computer_move(self):
        random_number = random.random()  # Generates a number between 0 and 1
        print(f"Generated random number: {random_number}")

        if random_number <= 0.4:
            # Make a random (suboptimal) move using min
            print("AI is making a random (suboptimal) move!")
            (m, qx, qy) = self.min()  # Call min for a suboptimal move
        else:
            # Make an optimal move using max
            print("AI is making an optimal move!")
            (m, qx, qy) = self.max()  # Call max for the optimal move

        # Make the chosen move
        self.current_state[qx][qy] = 'O'
        print(f"AI placed 'O' at ({qx}, {qy})")

    def play(self):
        while True:
            self.draw_board()
            # Assume player input here, for example:
            px, py = map(int, input("Enter your move (row and column): ").split())
            if self.is_valid(px, py):
                self.current_state[px][py] = 'X'  # Player X
                if self.is_end():
                    print("Player X wins!")
                    break
                self.computer_move()  # Computer's turn
                if self.is_end():
                    print("Computer O wins!")
                    break

# To run the game
if __name__ == "__main__":
    game = Game()
    game.play()
