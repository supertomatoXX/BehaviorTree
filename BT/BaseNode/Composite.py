# -*- coding: utf-8 -*
import BT

__all__ = ['Composite']


class Composite(BT.BaseNode):
    note_type = BT.COMPOSITE

    def __init__(self, children=None):
        super(Composite, self).__init__()

        self.children = children or []
