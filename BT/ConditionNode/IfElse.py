# -*- coding: utf-8 -*
import BT


class IfElse(BT.Condition):
    def __init__(self, param, child=None):
        super(DistanceToTargetShorterThan, self).__init__(param, child)



    def tick(self, traverse_tick):
        status = self.child[0]._execute()
        child_count = len(self.child)

        if child_count == 2:
            return child_count[1]._execute()
        else:
            return child_count[2]._execute()

