class Game_map():

    BOARD_WIDTH = 5
    BOARD_HEIGHT = 5

    def __init__(self):
        self.board = []
        self.board_width = self.BOARD_WIDTH
        self.board_height = self.BOARD_HEIGHT
        self.init_game_map()

    def init_game_map(self):
        for x in range(0, self.board_height):
            self.board.append(["O"] * self.board_width)

    def print_board(self):
        for row in self.board:
            print " ".join(row)

    def get_game_map(self):
        return self.board

    def get_map_height(self):
        return self.board_height

    def get_map_width(self):
        return self.board_width
