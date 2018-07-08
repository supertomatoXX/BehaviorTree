# -*- coding: utf-8 -*
import BT

__all__ = ['Root']


class Root(BT.BaseNode):
    node_type = BT.ROOT

    def __init__(self, children=None, param=None):
        super(Root, self).__init__()

        self.children = children or []
