from seriousgame.country import Country
from seriousgame.player import Player


class Game:

    def __init__(self, player=Player(), country=Country()):
        self.player = player
        self.country = country

    def new_turn(self):
        self.player.new_turn()
        self.country.new_turn()

    def play(self):
        while not self.country.is_win() and not self.country.is_lost():
            self.new_turn()
