# -*- coding: utf-8 -*
import BT

#__all__ = ['Root']


class SubTree(BT.BaseNode):
    node_type = BT.SUBTREE

    def __init__(self, root, param):
        super(SubTree, self).__init__( param )
        self.root = root

    def tick(self, tree):
        return self.root._execute(tree)
