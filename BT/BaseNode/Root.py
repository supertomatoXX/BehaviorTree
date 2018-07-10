# -*- coding: utf-8 -*
import BT

#__all__ = ['Root']


class Root(BT.BaseNode):
    node_type = BT.ROOT

    def __init__(self, children, param):
        super(Root, self).__init__()
        self.children = children

    def tick(self, tick):
        self.children._execute(tick)

'''        if not isinstance( self.children, list):
            self.children._execute(tick)
            return 

        for node in self.children:
            node._execute(tick)
'''