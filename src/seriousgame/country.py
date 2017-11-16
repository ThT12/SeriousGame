

class Country:
    INITIAL_REDUCTION = 0.01

    def __init__(self, name='France', init_ecology=0.5, init_social=0.5, init_economy=0.5):
        """ Constructor
        
        Args:
            name (str): country name 
            init_ecology (float): initial ecology level
            init_social (float): initial social level
            init_economy (float): initial economy level
        """
        self.name = name
        self.ecology = None
        self.set_ecology(init_ecology)
        self.social = None
        self.set_social(init_social)
        self.economy = None
        self.set_economy(init_economy)

    def set_ecology(self, value):
        """ set the property ecology after a value control
        
        Args:
            value (float): new ecology value 
        """
        verify_level_value(value)
        self.ecology = value

    def set_social(self, value):
        """ set the property social after a value control

        Args:
            value (float): new social value 
        """
        verify_level_value(value)
        self.social = value

    def set_economy(self, value):
        """ set the property economy after a value control

        Args:
            value (float): new economy value 
        """
        verify_level_value(value)
        self.economy = value

    def new_turn(self):
        """ make a country moved to the next turn"""
        self.set_ecology(max(self.ecology - Country.INITIAL_REDUCTION, 0))
        self.set_economy(max(self.economy - Country.INITIAL_REDUCTION, 0))
        self.set_social(max(self.social - Country.INITIAL_REDUCTION, 0))

    def is_win(self):
        """ Verifies if the country match the winning condition

        Returns:
            (bool): True if the country match the winning condition
        """
        return self.economy == 1 and self.ecology == 1 and self.social == 1

    def is_lost(self):
        """ Verifies if the country match the loosing condition
        
        Returns:
            (bool): True if the country match the loosing condition
        """
        return self.economy == 0 or self.ecology == 0 or self.social == 0


def verify_level_value(value):
    """ Verifies if a value can be set as a country level
        
    Args:
        value (float): value to test as a country level
    """
    if value < 0:
        raise KeyError('level value cannot be inferior to 0')
    if value > 1:
        raise KeyError('level value cannot be superior to 1')
