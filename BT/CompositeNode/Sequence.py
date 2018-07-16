# -*- coding: utf-8 -*
import BT

#__all__ = ['Sequence']

class Sequence(BT.Composite):

    def __init__(self, param, child ):
        super(Sequence, self).__init__(param, child)


    def tick(self, tick):
        for node in self.child:
            status = node._execute(tick)

            if status != BT.SUCCESS:
                return status

        return BT.SUCCESS
