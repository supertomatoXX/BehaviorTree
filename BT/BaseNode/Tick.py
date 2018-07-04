# -*- coding: utf-8 -*
__all__ = ['Tick']

class Tick(object):
    def __init__(self, tree=None, blackboard=None):
        self.tree = tree
        self.blackboard = blackboard

        self._open_nodes = []
        self._node_count = 0

    def _enter_node(self, node):
        print("tick enter node", node)
        self._node_count += 1
        self._open_nodes.append(node)

    def _open_node(self, node):
        pass

    def _tick_node(self, node):
        pass

    def _close_node(self, node):
        print("tick close node", node)
        self._open_nodes.pop()

    def _exit_node(self, node):
        pass