from queue import Queue
from utils.score import Score

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.score = Score()
        self.pos = [[], []]
    
    def connected(self):
        return self.ready

    def update_score(self, player):
        self.score.update(player)
    
    def add_pos(self, player, data):
        self.pos[player].append(data)
    
    def del_pos(self, player):
        self.pos[player].pop(0)

    def get_pos(self):
        return self.pos
    
    def reset(self):
        self.score.reset_score()
        self.pos = [[], []]
    

