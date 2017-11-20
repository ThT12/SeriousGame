from seriousgame.improvements import Improvement, Improvements
from seriousgame.tree import ProgressionTree


def build_tree():
    farming = Improvements('Farming', (Improvement(title='1', effects={'Influence': 5}),
                                       Improvement(title='2', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                       'Social': 0.1})))
    education = Improvements('Education', (Improvement(title='3', effects={'Influence': 5}),
                                           Improvement(title='4', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                           'Social': 0.1})))
    energy = Improvements('Energy', (Improvement(title='5', effects={'Influence': 5}),
                                     Improvement(title='6', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                     'Social': 0.1})))
    politic = Improvements('Politic', (Improvement(title='7', effects={'Influence': 5}),
                                       Improvement(title='8', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                       'Social': 0.1})))
    economy = Improvements('Economy', (Improvement(title='9', effects={'Influence': 5}),
                                       Improvement(title='10', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                        'Social': 0.1})))
    return ProgressionTree((farming, education, energy, politic, economy))
