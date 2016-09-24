from random import randint

class Board:

    def __init__(self,size,living):
        if size*size < living:
            raise Exception("This amount of cells can't fit into this board size")
        self.board = [[' ' for x in range(size)] for y in range(size)]
        self.size = size
        self.numberOfCells = 0
        self.placeLivingCells(living)

    def placeLivingCells(self,amount):
        placedCells = 0
        while placedCells < amount:
            x = randint(0, self.size - 1)
            y = randint(0, self.size - 1)
            if self.board[x][y] != 'X':
                self.board[x][y] = 'X'
                placedCells += 1
                self.numberOfCells += 1

