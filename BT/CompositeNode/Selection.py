# -*- coding: utf-8 -*
import BT

#__all__ = ['Selection']

class Selection(BT.Composite):

    def __init__(self, children, param ):
        super(Selection, self).__init__(children)


    def tick(self, tick):
        for node in self.children:
            status = node._execute(tick)

            if status == BT.SUCCESS:
                return status

        return status
