"""
15 puzzle

"""
from random import randint
import tkinter
# todo timer and move count and mps

class Puzzle:
    def __init__(self, board=None, srow=3, scol=3):
        if board is None:
            board = [[' 1', ' 2', ' 3', ' 4'], [' 5', ' 6', ' 7', ' 8'], [' 9', '10', '11', '12'],
                     ['13', '14', '15', '  ']]
        self.start = [[' 1', ' 2', ' 3', ' 4'], [' 5', ' 6', ' 7', ' 8'], [' 9', '10', '11', '12'],
                     ['13', '14', '15', '  ']]
        self.board = board
        self.row = srow
        self.col = scol
        self.moves = 0
        # super(Puzzle, self).__init__()
        self.is_scrambling = False

    def print_board(self):
        print('-------------')
        for i in range(4):
            print(f"|{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}|{self.board[i][3]}|")
        print('-------------')

    def swap(self, a, b):
        self.board[a][b], self.board[self.col][self.row] = self.board[self.col][self.row], self.board[a][b]

    def right(self):
        if self.row > 0:
            self.swap(self.col, self.row - 1)
            self.row -= 1
            if not self.is_scrambling:
                self.print_board()

    def left(self):
        if self.row < 3:
            self.swap(self.col, self.row + 1)
            self.row += 1
            if not self.is_scrambling:
                self.print_board()

    def down(self):
        if self.col > 0:
            self.swap(self.col - 1, self.row)
            self.col -= 1
            if not self.is_scrambling:
                self.print_board()

    def up(self):
        if self.col < 3:
            self.swap(self.col + 1 , self.row)
            self.col += 1
            if not self.is_scrambling:
                self.print_board()

    def scramble(self, length=1000):
        self.is_scrambling = True
        for i in range(length):
            num = randint(1, 4)
            if num == 1:
                self.right()
            if num == 2:
                self.left()
            if num == 3:
                self.up()
            if num == 4:
                self.down()
        else:
            self.is_scrambling = False
            self.print_board()


dude = Puzzle()
dude.print_board()

dude.scramble()
print('end')
dude.right()
dude.up()
while dude.board != dude.start:
    move = input('Enter your move: ')
    if move == 'd':
        dude.right()
        dude.moves += 1
    if move == 'a':
        dude.left()
        dude.moves += 1
    if move == 'w':
        dude.up()
        dude.moves += 1
    if move == 's':
        dude.down()
        dude.moves += 1

print('you win!'.title())
print('Total number of moves'.title(), dude.moves)