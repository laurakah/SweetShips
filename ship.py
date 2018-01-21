import game_map
from random import randint

class Ship():

    def __init__(self, game_map):
        self.game_map = game_map
        self.ship_col = self.create_ship_col(self.game_map.board)
        self.ship_row = self.create_ship_row(self.game_map.board)

    def create_ship_row(self, board):
        self.ship_rol = randint(0, len(board) - 1)

    def create_ship_col(self, board):
        self.ship_col = randint(0, len(board[0]) - 1)

    def get_ship_col(self):
        return self.ship_col

    def get_ship_row(self):
        return self.ship_row
