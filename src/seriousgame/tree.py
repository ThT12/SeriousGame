from seriousgame.improvements import Improvements


class ProgressionTree(object):

    def __init__(self, tree=None):
        if tree is None:
            tree = (Improvements(name='Name1'), Improvements(name='Name2'))
        self.tree = tree

