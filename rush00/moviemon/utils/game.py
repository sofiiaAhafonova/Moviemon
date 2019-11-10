from .player import Player

class Game:
    def __init__(self, height, length, player: Player):
        self.height = height
        self.length = length
        self.player = player

    def move_left(self):
        if self.player.position.x > 0:
            self.player.move_left()
    
    def move_right(self):
        if self.player.position.x < self.length:
            self.player.move_right()
    
    def move_up(self):
        if self.player.position.y > 0:
            self.player.move_up()

    def move_down(self):
        if self.player.position.y < self.height:
            self.player.move_down()
