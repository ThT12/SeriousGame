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

    def get_improvements_available(self):
        """
        Returns:
            (list): return a list of improvement that are available to be done in the tree
        """
        return [improvement for improvements_in_tree in self.tree
                for improvement in improvements_in_tree.get_improvements_available()]
