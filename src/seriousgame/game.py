from seriousgame.country import Country
from seriousgame.improvements import Improvement
from seriousgame.improvements import Improvements
from seriousgame.io import inputs
from seriousgame.io import outputs
from seriousgame.player import Player


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
        current_effect = self.improvements.get_current_effects()
        self.player.new_turn(current_effect)
        self.let_player_play()
        self.country.new_turn(current_effect)

    def play(self):
        """ Launch the game until it is finish"""
        while not self.country.is_win() and not self.country.is_lost():
            self.new_turn()

    def let_player_play(self):
        """ Let the player do all improvement he want/can"""
        improvement = Improvement()
        while improvement is not None:
            outputs.display_influence_available(self.player)
            outputs.display_improvements(self.improvements.get_improvements_available(), self.player.influence)
            improvement_available = self.improvements.get_improvements_available()
            if len(improvement_available) != 0:
                improvement = inputs.ask_improvements_to_make(improvement_available, self.player)
                if improvement is not None:
                    improvement.develop()
                    self.player.use_influence(improvement.influence_cost)
            else:
                improvement = None
