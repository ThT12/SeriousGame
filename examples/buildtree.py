from seriousgame.improvements import Improvement, Improvements
from seriousgame.tree import ProgressionTree
from seriousgame.effect import Effect, EffectDescriptor


def build_tree():
    effect_one = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=5)
    effect_two = Effect(effect_descriptor=EffectDescriptor.ECOLOGY, value=0.1)
    effect_three = Effect(effect_descriptor=EffectDescriptor.ECONOMY, value=0.1)
    effect_four = Effect(effect_descriptor=EffectDescriptor.SOCIAL, value=0.1)

    farming = Improvements('Farming', (Improvement(title='1', effects=[effect_one]),
                                       Improvement(title='2', effects=[effect_two, effect_three, effect_four])))
    education = Improvements('Education', (Improvement(title='3', effects=[effect_one]),
                                           Improvement(title='4', effects=[effect_two, effect_three, effect_four])))
    energy = Improvements('Energy', (Improvement(title='5', effects=[effect_one]),
                                     Improvement(title='6', effects=[effect_two, effect_three, effect_four])))
    politic = Improvements('Politic', (Improvement(title='7', effects=[effect_one]),
                                       Improvement(title='8', effects=[effect_two, effect_three, effect_four])))
    economy = Improvements('Economy', (Improvement(title='9', effects=[effect_one]),
                                       Improvement(title='10', effects=[effect_two, effect_three, effect_four])))
    return ProgressionTree((farming, education, energy, politic, economy))
