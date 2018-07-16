# -*- coding: utf-8 -*
import BT

#__all__ = ['Composite']


class Composite(BT.BaseNode):
    node_type = BT.COMPOSITE

    def __init__(self, param, child ):
        super(Composite, self).__init__(param)

        self.child = child
