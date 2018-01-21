import game_map
import ship
import player

class Game():

    MAX_TURNS = 15

    def __init__(self):
        self.game_map = game_map.Game_map()
        self.player = player.Player()
        self.ship = ship.Ship(self.game_map)

    def get_user_input(self):
        return self.player.ask_user_input()

    def game(self):
        self.game_map.print_board()
        for turn in range(self.MAX_TURNS):
            self.get_user_input()
            if self.player.get_player_row() == self.ship.get_ship_row() and self.player.get_player_col() == self.ship.get_ship_col():
                print "\nCongratulations! You sank my battleship!\n\n"
                break
            else:
                if self.player.get_player_row() not in range(self.game_map.get_map_width()) or self.player.get_player_col() not in range(self.game_map.get_map_height()):
                    print "\nOops, that's not even on the board.\n\n"
                elif self.game_map.get_game_map()[self.player.get_player_row()][self.player.get_player_col()] == "X":
                    print "\nYou guessed that one already.\n\n"
                else:
                    print "\nYou missed my battleship!\n\n"
                    self.game_map.get_game_map()[self.player.get_player_row()][self.player.get_player_col()] = "X"
                if turn == (self.MAX_TURNS - 1):
                    print "\n\nGame Over!\n\n"
                else:
                    self.game_map.print_board()
                    print "This was turn ", turn + 1, " out of %d turns\n\n" % self.MAX_TURNS

if __name__ == "__main__":
    g = Game()
    g.game()
