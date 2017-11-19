

class Country(object):
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
        self.ecology = init_ecology
        self.social = init_social
        self.economy = init_economy

    def __setattr__(self, name, value):
        if name != 'name':
            verify_level_value(value)
        super(Country, self).__setattr__(name, value)

    def new_turn(self, effects=None):
        """ make a country moved to the next turn

        Args:
            effects (dict): list of effect that are currently applied. Only the Key Ecology, Economy and Social are used
        """
        bonus_ecology = 0
        bonus_economy = 0
        bonus_social = 0
        if effects is not None:
            if 'Ecology' in effects.keys():
                bonus_ecology = effects['Ecology']
            if 'Economy' in effects.keys():
                bonus_economy = effects['Economy']
            if 'Social' in effects.keys():
                bonus_social = effects['Social']
        self.ecology = min(max(self.ecology - Country.INITIAL_REDUCTION + bonus_ecology, 0), 1)
        self.economy = min(max(self.economy - Country.INITIAL_REDUCTION + bonus_economy, 0), 1)
        self.social = min(max(self.social - Country.INITIAL_REDUCTION + bonus_social, 0), 1)

    def is_win(self):
        """ Verifies if the country match the winning condition

        Returns:
            (bool): True if the country match the winning condition
        """
        return self.economy == 1 and self.ecology == 1 and self.social == 1

    def is_lost(self):
        """ Verifies if the country match the loosing condition
        
        Returns:
            (bool): True if the country match one loosing condition
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
