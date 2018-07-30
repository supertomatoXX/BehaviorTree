# -*- coding: utf-8 -*
import BT



class SubTree(BT.BaseNode):
    node_type = BT.SUBTREE

    def __init__(self, param, root ):
        super(SubTree, self).__init__( param )
        self.child = root

    def tick(self, tree):
        return self.child._execute(tree)
