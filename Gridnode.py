

class Gridnode:
    """
    Gridnode represents one single square within the grid
    Must contain coordinates, neighbor information, and boolean representation of life
    Will also contain age for possible age monitorning of entities

    Must access the Grid
    """

    def __init__(self, x, y, xpos, ypos):
        self.alive = False
        self.age = 0
        self.x = x
        self.y = y
        self.xpos = xpos
        self.ypos = ypos
        self.neighbors = []
        self.color = "#d3d3d3" if self.alive else "#13191F"
        self.rect = None
    
    def get_neighbors(self):
        pass

