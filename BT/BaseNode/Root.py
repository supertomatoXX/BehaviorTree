# -*- coding: utf-8 -*
import BT

#__all__ = ['Root']


class Root(BT.BaseNode):
    node_type = BT.ROOT

    def __init__(self, param, child):
        super(Root, self).__init__( param )
        self.child = child

    def tick(self, tree):
        return self.child._execute(tree)
