import time

from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use single list to represent (3x3) board
        self.current_winner = None

    def print_board(self):
        # this is just getting the rows
        for rows in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print(' | ' + ' | '.join(rows) + ' | ')

    @staticmethod
    def print_board_nums():
        # 0 |  1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')
        # return len(self.available_moves())

    def make_move(self, letter, square):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonals
        # but only if the square us an even number(0,2,4,6,8)
        # these are the only possible moves to win diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these checks fails
        return False


def play(game, x_player, o_player, print_game=True):
    # return the winner of the game(the letter)! or None for a tie

    if print_game:
        game.print_board_nums()
    letter = 'X'  # starting letter
    while game.empty_square():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to a make a move !!
        if game.make_move(letter, square):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

        # after we made the move, ew need alternate letters
        letter = 'O' if letter == 'X' else 'X'
        # add a tiny break
        time.sleep(0.7)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
