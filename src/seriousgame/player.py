

class Player(object):
    INITIAL_INFLUENCE_BY_TURN = 1

    def __init__(self, name='Player', influence=0):
        """ Constructor
        
        Args:
            name (str): Player name 
            influence (int): Initial influence
        """
        self.name = name
        self.influence = influence

    def new_turn(self):
        """ make a player moved to the next turn"""
        self.influence += Player.INITIAL_INFLUENCE_BY_TURN

    def use_influence(self, amount):
        """ make a player use is influence. Return an error if a player use more influence than he has.
        
        Args:
            amount (int): Amount of influence the player want to use
        """
        if amount < self.influence:
            self.influence -= amount
        else:
            raise KeyError('You cannot use more influence that you have')
