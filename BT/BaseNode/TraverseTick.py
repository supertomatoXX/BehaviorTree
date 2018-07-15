# -*- coding: utf-8 -*
#__all__ = ['TraverseTick']



class TraverseTick(object):
    __slots__ = ('tree', 'blackboard', 'node_count','running_nodes')
    
    def __init__(self, tree, blackboard):
        self.tree = tree
        self.blackboard = blackboard
        self.node_count = 0
        self.running_nodes = []

    def append_running_node(self, node):
        self.node_count += 1
        self.running_nodes.append(node)

    def pop_running_node(self, node):
        self.running_nodes.pop()