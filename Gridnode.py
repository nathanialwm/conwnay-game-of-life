

class Gridnode:
    """
    Gridnode represents one single square within the grid
    Must contain coordinates, neighbor information, and boolean representation of life
    Will also contain age for possible age monitorning of entities

    Must access the Grid
    """

    def __init__(self, alive, age, x, y):
        self.alive = alive
        self.age = age
        self.x = x
        self.y = y
        self.neighbors = []
    
    def get_neighbors(self):
        pass

