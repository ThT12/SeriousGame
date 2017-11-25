from seriousgame.country import Country
from seriousgame.effect import merge_effects
from seriousgame.event import Events
from seriousgame.improvements import Improvement
from seriousgame.io import inputs
from seriousgame.io import outputs
from seriousgame.player import Player
from seriousgame.tree import ProgressionTree


class Game(object):

    def __init__(self, player=Player(), country=Country(), tree=ProgressionTree(), events=Events()):
        """ Constructor

        Args:
            player (Player): player information
            country (Country): country information
            tree (ProgressionTree): Tree that contain improvement available for this game
            events (Events): Events possible in this game
        """
        self.player = player
        self.country = country
        self.tree = tree
        self.events = events

    def new_turn(self):
        """ Makes a new turn in the game """
        self.tree.set_improvement_numbers()
        self.country.display()
        self.let_player_play()
        current_effect = self.tree.get_current_effects()
        event_effect = self.events.get_event_effect(self.country)
        effects = merge_effects(current_effect, event_effect)
        self.country.new_turn(effects)
        self.player.new_turn(effects)
        self.tree.new_turn()

    def play(self):
        """ Launch the game until it is finish """
        self.game_introduction()
        while not self.country.is_win() and not self.country.is_lost():
            self.new_turn()
        self.country.display()
        if self.country.is_win():
            outputs.display_win()
        else:
            outputs.display_lost()

    def let_player_play(self):
        """ Let the player do all improvement he want/can """
        improvement = Improvement()
        while improvement is not None:
            outputs.display_influence_available(self.player)
            outputs.display_tree_available(self.tree, self.player.influence)
            improvement_available = self.tree.get_improvements_available()
            if len(improvement_available) != 0:
                improvement = inputs.ask_improvements_to_make(improvement_available, self.player)
                if improvement is not None:
                    improvement.develop()
                    self.player.use_influence(improvement.influence_cost)
            else:
                improvement = None

    def game_introduction(self):
        """ Make the game introduction: ask player name and country and display context """
        outputs.display_context_part_one()
        [player_name, country_name] = inputs.ask_player_name_and_country()
        self.player.name = player_name
        self.country.name = country_name
        outputs.display_context_part_two()
