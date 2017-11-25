from seriousgame.effect import Effect
from seriousgame.effect import EffectDescriptor
from seriousgame.effect import Effects
from seriousgame.improvements import Improvement
from seriousgame.improvements import Improvements
from seriousgame.tree import ProgressionTree


def build_tree():
    effect_one = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=5)
    effect_two = Effect(effect_descriptor=EffectDescriptor.ECOLOGY, value=0.1)
    effect_three = Effect(effect_descriptor=EffectDescriptor.ECONOMY, value=0.1)
    effect_four = Effect(effect_descriptor=EffectDescriptor.SOCIAL, value=0.1)

    farming = Improvements('Farming', (Improvement(title='My Title', effects=Effects([effect_one])),
                                       Improvement(title='a', effects=Effects([effect_two, effect_three,
                                                                               effect_four]))))
    education = Improvements('Education', (Improvement(title='b', effects=Effects([effect_one])),
                                           Improvement(title='c', effects=Effects([effect_two, effect_three,
                                                                                   effect_four]))))
    energy = Improvements('Energy', (Improvement(title='d', effects=Effects([effect_one])),
                                     Improvement(title='e', effects=Effects([effect_two, effect_three, effect_four]))))
    politic = Improvements('Politic', (Improvement(title='f', effects=Effects([effect_one])),
                                       Improvement(title='g', effects=Effects([effect_two, effect_three,
                                                                               effect_four]))))
    economy = Improvements('Economy', (Improvement(title='h', effects=Effects([effect_one])),
                                       Improvement(title='i', effects=Effects([effect_two, effect_three,
                                                                               effect_four]))))
    return ProgressionTree((farming, education, energy, politic, economy))
