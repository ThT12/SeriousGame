import random

from seriousgame.effect import Effects

PROBABILITY = 0.05


class Event(object):

    def __init__(self, name='Event name', description='Event description', effects=Effects(), condition_type=None,
                 condition_direction=None, condition_value=None):
        """ Constructor

        Args:
            name (str): Event name
            description (str): Event description
            effects (Effects): list of Effect
            condition_type (EffectDescriptor): country condition the condition will be tested
            condition_direction (str): 'inf' or 'sup' indicating if the condition_type must be '<' or '>'
                condition_value
            condition_value (float): value condition
        """
        if condition_direction is not None and condition_direction not in ['sup', 'inf']:
            raise KeyError('condition_direction must be "sup" or "inf"')

        self.name = name
        self.description = description
        self.effects = effects
        self.condition_type = condition_type
        self.condition_direction = condition_direction
        self.condition_value = condition_value

    def is_event_possible(self, country):
        """ test is the even can occurs in country

        Args:
            country (Country): Country in which the even will happen

        Returns:
            (bool): True if this event can happen
        """
        if (self.condition_direction == 'sup' and country.__getattr__(self.condition_type) > self.condition_value) or \
                (self.condition_direction == 'inf' and country.__getattr__(self.condition_type) < self.condition_value):
                return True
        return False

    def get_effects(self):
        """
        Returns:
            (dict): return event effect
        """
        return self.effects.get_current_effects()


class Events(object):

    def __init__(self, events=None):
        """ Constructor

        Args:
            events (list): list of Event
        """
        self.events = [] if events is None else events

    def get_event_possible(self, country):
        """ get the list of effect that can happen this turn

        Args:
            country (Country): Country in which an event can occurs

        Returns:
            (list): list of effect that can happen this turn
        """
        return [event for event in self.events if event.is_event_possible(country)]

    def get_event_effect(self, country):
        """ determine if an event occurs an return an possible event effect
        Args:
            country (Country): Country in which an event can occurs

        Returns:
            (dict): return an event effect if an event occurs
        """
        event_possible = self.get_event_possible(country)
        if len(event_possible) != 0 and is_event_occurs():
            # TODO: Add display event
            return random.choice(event_possible).get_effects()
        else:
            return {}


def is_event_occurs():
    """
    Returns:
        (bool): True if an event occurs
    """
    return True if random.random() < PROBABILITY else False
