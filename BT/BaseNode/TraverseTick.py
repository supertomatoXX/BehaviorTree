# -*- coding: utf-8 -*
#__all__ = ['TraverseTick']



class TraverseTick(object):
    __slots__ = ('tree')
    
    def __init__(self, tree):
        self.tree = tree

    '''
    def append_running_node(self, node):
        self.running_nodes.append(node)

    def pop_running_node(self, node):
        if len( self.running_nodes ) > 0:
            self.running_nodes.pop()
    '''