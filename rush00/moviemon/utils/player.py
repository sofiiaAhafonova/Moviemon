class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Player:
    def __init__(self, position:Position, movieballs = None):
        self.position = position
        self.movieballs = movieballs

    def move_left(self):
        self.x -= 1
    
    def move_right(self):
        self.x += 1
    
    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1
