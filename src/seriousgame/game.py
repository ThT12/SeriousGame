from seriousgame.country import Country
from seriousgame.player import Player


class Game(object):

    def __init__(self, player=Player(), country=Country()):
        """ Constructor

        Args:
            player (Player): player information
            country (Country): country information
        """
        self.player = player
        self.country = country

    def new_turn(self):
        """ Makes a new turn in the game"""
        self.player.new_turn()
        self.country.new_turn()

    def play(self):
        """ Launch the game until it is finish"""
        while not self.country.is_win() and not self.country.is_lost():
            self.new_turn()
