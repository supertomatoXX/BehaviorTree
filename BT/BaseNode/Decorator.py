# -*- coding: utf-8 -*
import BT

__all__ = ['Decorator']


class Decorator(BT.BaseNode):
    node_type = BT.DECORATOR

    def __init__(self, child=None):
        super(Decorator, self).__init__()

        self.child = child or []
