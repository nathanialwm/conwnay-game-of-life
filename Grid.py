from Gridnode import Gridnode

class Grid:
    def __init__(self, size):
        self.cell_size = 20
        self.rows = int(size[1]/self.cell_size)
        self.cols = int(size[0]/self.cell_size)
        self.size = (self.rows, self.cols) # index size of grid

        self.grid = [[Gridnode(x, y, x*self.cell_size, y*self.cell_size) for x in range(self.cols)] for y in range(self.rows)]

