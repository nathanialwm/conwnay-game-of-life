import random

class Gridnode:
    """
    Gridnode represents one single square within the grid
    Must contain coordinates, neighbor information, and boolean representation of life
    Will also contain age for possible age monitorning of entities

    Must access the Grid
    """

    def __init__(self, x, y, xpos, ypos, spawn_rate):
        self.alive = self.init_alive(spawn_rate)
        self.age = 0
        self.x = x
        self.y = y
        self.xpos = xpos
        self.ypos = ypos
        self.neighbors = []
        self.color = "#b9e4a0" if self.alive else "#13191F"
        self.rect = None
        
    def init_alive(self, spawn_rate) -> bool:
        if random.random() * 100 >= spawn_rate:
            return False
        else:
            return True
        
    def get_neighbors(self):
        pass

