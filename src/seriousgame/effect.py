from enum import Enum


class EffectDescriptor(str, Enum):
    LOBBYING = 'Lobbying'
    INFLUENCE = 'Influence'
    ECOLOGY = 'Ecology'
    ECONOMY = 'Economy'
    SOCIAL = 'Social'


class Effect(object):

    def __init__(self, effect_descriptor=EffectDescriptor.INFLUENCE, value=0, start_effect=0, end_effect=float('inf')):
        """ Constructor

        Args:
            effect_descriptor (EffectDescriptor): effect descriptor
            value (float): effect value
            start_effect (int): number of turn after which the effect is applied
            end_effect (float): number of turn after which the effect is not applied anymore
        """
        if effect_descriptor == EffectDescriptor.LOBBYING:
            start_effect = 0
            end_effect = 1
        self.turn_since_done = 0
        self.effect_descriptor = effect_descriptor
        self.value = value
        self.start_effect = start_effect
        self.end_effect = end_effect

    def __str__(self):
        if self.end_effect == float('inf'):
            str_duration = ', and stay permanently'
        else:
            str_duration = ' '.join([', and stay during', str(self.end_effect - self.start_effect), 'turn(s)'])
        return ''.join([self.effect_descriptor.value, ': ', str(self.value), ' in ', str(self.start_effect),
                        ' turn(s)', str_duration])

    def new_turn(self):
        """ Makes a new turn to an Effect"""
        self.turn_since_done += 1

    def get_current_effect(self):
        """
        Returns:
            (dict): return a dictionary with the effect_descriptor as key and value as value. Empty dictionary if the
                Effect has currently no effect
        """
        if self.start_effect <= self.turn_since_done < self.end_effect:
            return {self.effect_descriptor: self.value}
        else:
            return {}


class Effects(object):

    def __init__(self, effects=None):
        self.effects = [] if effects is None else effects

    def get_current_effects(self):
        """
        Returns:
            (dict): return all effects. If two improvement have the same EffectDescriptor then their values are summed
        """
        effects = {}
        for effect in self.effects:
            effects = merge_effects(effects, effect.get_current_effect())
        return effects

    def new_turn(self):
        """ Apply a new turn on all effects """
        for effect in self.effects:
            effect.new_turn()


def merge_effects(effects1, effects2):
    """ merge two dictionary. If two improvement have the same type of effects then their values are summed

    Args:
        effects1 (dict): first dictionary to merge
        effects2 (dict): second dictionary to merge

    Returns:
        (dict): merged dictionaries
    """
    effects = effects1
    for key in effects2.keys():
        if key in effects:
            effects[key] += effects2[key]
        else:
            effects.update({key: effects2[key]})
    return effects
