# -*- coding: utf-8 -*
import BT

#__all__ = ['Composite']


class Composite(BT.BaseNode):
    node_type = BT.COMPOSITE

    def __init__(self, child ):
        super(Composite, self).__init__()

        self.child = child
