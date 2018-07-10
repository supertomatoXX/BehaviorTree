# -*- coding: utf-8 -*
#__all__ = ['TraverseTick']



class TraverseTick(object):
    __slots__ = ('tree', 'blackboard')
    
    def __init__(self, tree, blackboard):
        self.tree = tree
        self.blackboard = blackboard
