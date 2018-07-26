# -*- coding: utf-8 -*
import BT



class SubTree(BT.BaseNode):
    node_type = BT.SUBTREE

    def __init__(self, root, param):
        super(SubTree, self).__init__( param )
        self.child = root

    def tick(self, tree):
        return self.child._execute(tree)
