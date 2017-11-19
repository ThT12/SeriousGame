from seriousgame.game import Game
from seriousgame.improvements import Improvement, Improvements
from seriousgame.tree import ProgressionTree


improvements = Improvements('Farming', (Improvement(title='1', effects={'Influence': 5}),
                                        Improvement(title='2', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                        'Social': 0.1})))
improvements_2 = Improvements('Education', (Improvement(title='3', effects={'Influence': 5}),
                                            Improvement(title='4', effects={'Ecology': 0.1, 'Economy': 0.1,
                                                                            'Social': 0.1})))
tree = ProgressionTree((improvements, improvements_2))
game = Game(tree=tree)
game.play()
