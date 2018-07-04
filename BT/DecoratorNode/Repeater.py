# -*- coding: utf-8 -*
import BT

__all__ = ['Repeater']

class Repeater(BT.Decorator):
    def __init__(self, child, max_loop=-1):
        super(Repeater, self).__init__(child)

        self.max_loop = max_loop

    def open(self, tick):
        tick.blackboard.set('i', 0, tick.tree.id, self.id)

    def tick(self, tick):
        if not self.child:
            return BT.ERROR

        i = tick.blackboard.get('i', tick.tree.id, self.id)
        status = BT.SUCCESS

        while self.max_loop < 0 or i < self.max_loop:
            status = self.child._execute(tick)

            if status == BT.SUCCESS or status == BT.FAILURE:
                i += 1
            else:
                break

        tick.blackboard.set('i', i, tick.tree.id, self.id)
        return status

        
