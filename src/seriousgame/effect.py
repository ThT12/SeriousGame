from enum import Enum


class EffectDescriptor(Enum):
    LOBBYING = 'Lobbying'
    INFLUENCE = 'Influence'
    ECOLOGY = 'Ecology'
    ECONOMY = 'Economy'
    SOCIAL = 'Social'


class Effect(object):

    def __init__(self, effect_descriptor=EffectDescriptor.INFLUENCE, value=0, start_effect=0, end_effect=float('inf')):
        if effect_descriptor == EffectDescriptor.LOBBYING:
            start_effect = 0
            end_effect = 1

        self.turn_since_done = 0
        self.effect_descriptor = effect_descriptor
        self.value = value
        self.start_effect = start_effect
        self.end_effect = end_effect

    def new_turn(self):
        self.turn_since_done += 1

    def get_current_effect(self):
        if self.start_effect <= self.turn_since_done < self.end_effect:
            return {self.effect_descriptor: self.value}
        else:
            return {}
