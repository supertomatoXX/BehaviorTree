# -*- coding: utf-8 -*
#__all__ = ['TraverseTick']



class TraverseTick(object):
    def __init__(self, tree, blackboard):
        self.tree = tree
        self.blackboard = blackboard

    def get_tree(self):
        return self.tree

    def get_blackboard(self):
        return self.blackboard