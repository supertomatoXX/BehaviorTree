# -*- coding: utf-8 -*
import BT

#__all__ = ['Condition']


class Condition(BT.BaseNode):
    node_type = BT.CONDITION

    def __init__(self,  param, param_type, child):
        super(Condition, self).__init__( param, param_type)
        self.child = child
        
