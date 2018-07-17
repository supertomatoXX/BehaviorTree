# -*- coding: utf-8 -*
import BT

#__all__ = ['Selection']

class Selection(BT.Composite):

    def __init__(self, param, child ):
        super(Selection, self).__init__(param, child)


    def tick(self, tree):
        for node in self.child:
            status = node._execute(tree)

            if status == BT.SUCCESS:
                return status

        return status
