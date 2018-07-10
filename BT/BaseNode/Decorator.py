# -*- coding: utf-8 -*
import BT

#__all__ = ['Decorator']


class Decorator(BT.BaseNode):
    node_type = BT.DECORATOR

    def __init__(self, child, param, param_type):
        super(Decorator, self).__init__(param, param_type)

        self.child = child 
