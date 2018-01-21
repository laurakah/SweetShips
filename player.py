class Player():

    def __init__(self):
        self.player_row = None
        self.player_col = None

    def _ask_player_row(self):
        self.player_row = int(raw_input("Guess a Row: ")) - 1

    def _ask_player_col(self):
        self.player_col = int(raw_input("Guess a Col: ")) - 1

    def ask_user_input(self):
        self._ask_player_row()
        self._ask_player_col()

    def get_player_row(self):
        return self.player_row

    def get_player_col(self):
        return self.player_col
