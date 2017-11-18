from seriousgame.country import Country
from seriousgame.player import Player
from seriousgame.improvements import Improvements
from seriousgame.io import outputs


class Game(object):

    def __init__(self, player=Player(), country=Country(), improvements=Improvements()):
        """ Constructor

        Args:
            player (Player): player information
            country (Country): country information
            improvements (Improvements): improvement available for this game
        """
        self.player = player
        self.country = country
        self.improvements = improvements

    def new_turn(self):
        """ Makes a new turn in the game"""
        self.player.new_turn()
        outputs.display_influence_available(self.player)
        outputs.display_improvements(self.improvements.get_improvements_available(), self.player.influence)
        self.country.new_turn()

    def play(self):
        """ Launch the game until it is finish"""
        while not self.country.is_win() and not self.country.is_lost():
            self.new_turn()
