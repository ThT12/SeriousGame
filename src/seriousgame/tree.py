from seriousgame import improvements
from seriousgame.improvements import Improvements


class ProgressionTree(object):

    def __init__(self, tree=None):
        """ Constructor

        Args:
            tree (tuple): tuple of Improvements
        """
        if tree is None:
            tree = (Improvements(name='Name1'), Improvements(name='Name2'))
        self.tree = tree

    def get_current_effects(self):
        """
        Returns:
            (dict): return all effects currently applied from all Improvements in ProgressionTree. If two improvement
                have the same type of effects then their values are summed
        """
        effects = {}
        for improvements_obj in self.tree:
            effects = improvements.merge_effects(effects, improvements_obj.get_current_effects())
        return effects
