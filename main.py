import numpy as np


class TicTacToe:
    def __init__(self) -> None:
        self.dim = 3
        self.player_symbols = ('X', 'O')
        self.active_player = 1
        self.name = 'Player B'
        self.play_field = [
            ['□', '□', '□'],
            ['□', '□', '□'],
            ['□', '□', '□'],
        ]
        self.allowed_positions = range(1, self.dim * self.dim + 1)
        self.draws_left = len(self.allowed_positions)
        self.input_positions = np.array(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
        self.game_over = False

    def display_allowed_positions(self):
        print(f"Input Positions: \n{self.input_positions}")

    def display_field(self):
        for line in range(self.dim):
            print(self.play_field[line])

    def switch_player(self):
        if self.active_player == 0:
            self.active_player = 1
        else:
            self.active_player = 0

    def translate_user_input(self, pos):
        for x in range(self.dim):
            for y in range(self.dim):
                if pos == self.input_positions[x][y]:
                    return x, y

    def evaluate_input(self, pos):
        if pos not in self.allowed_positions:
            print('Invalid position!')
            return False
        else:
            x, y = self.translate_user_input(pos)
            if self.play_field[x][y] != '□':
                print('Input at selected position not possible!')
                return False
            else:
                self.play_field[x][y] = self.player_symbols[self.active_player]
                self.draws_left -= 1
                return True

    def allow_input(self):
        if (self.active_player == 0):
            self.name = 'Player A'
        else:
            self.name = 'Player B'

        input_valid = False
        while (not input_valid):
            pos = int(input(f"{self.name}: Please enter position 1-9 for symbol {
                self.player_symbols[self.active_player]}: "))
            input_valid = self.evaluate_input(pos)

    def find_winner(self):
        act_symbol = self.player_symbols[self.active_player]
        win_conditions = [
            # rows
            self.play_field[0][0] == act_symbol and self.play_field[0][
                0] == self.play_field[0][1] and self.play_field[0][0] == self.play_field[0][2],
            self.play_field[1][0] == act_symbol and self.play_field[1][
                0] == self.play_field[1][1] and self.play_field[1][0] == self.play_field[1][2],
            self.play_field[2][0] == act_symbol and self.play_field[2][
                0] == self.play_field[2][1] and self.play_field[2][0] == self.play_field[2][2],
            # colums
            self.play_field[0][0] == act_symbol and self.play_field[0][
                0] == self.play_field[1][0] and self.play_field[0][0] == self.play_field[2][0],
            self.play_field[0][1] == act_symbol and self.play_field[0][
                1] == self.play_field[1][1] and self.play_field[0][1] == self.play_field[2][1],
            self.play_field[0][2] == act_symbol and self.play_field[0][
                2] == self.play_field[1][2] and self.play_field[0][2] == self.play_field[2][2],
            # diagonals
            self.play_field[0][0] == act_symbol and self.play_field[0][
                0] == self.play_field[1][1] and self.play_field[0][0] == self.play_field[2][2],
            self.play_field[2][0] == act_symbol and self.play_field[2][
                0] == self.play_field[1][1] and self.play_field[2][0] == self.play_field[0][2],
        ]

        for cond in win_conditions:
            if (cond is True):
                print(f"Player {self.name} won!")
                return True
        else:
            return False

    def verify_game(self):
        if self.find_winner() == True:
            self.game_over = True
        if self.draws_left <= 0:
            print("Game over! It's a draw! There's no winner!")
            self.game_over = True


game = TicTacToe()


def play():
    game.display_allowed_positions()
    while game.game_over is False:
        game.switch_player()
        game.allow_input()
        game.display_field()
        game.verify_game()


if __name__ == "__main__":
    play()
