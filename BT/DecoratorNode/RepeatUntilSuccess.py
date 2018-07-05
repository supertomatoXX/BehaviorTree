# -*- coding: utf-8 -*
import BT

__all__ = ['RepeatUntilSuccess']

class RepeatUntilSuccess(BT.Decorator):
    def __init__(self, child, max_loop=-1):
        super(RepeatUntilSuccess, self).__init__(child)

        self.max_loop = max_loop

    def enter(self, traverse_tick):
        traverse_tick.get_blackboard().set('i', 0, traverse_tick.get_tree().id, self.id)

    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR

        i = traverse_tick.get_blackboard().get('i', traverse_tick.get_tree().id, self.id)
        while self.max_loop < 0 or i < self.max_loop:
            status = self.child._execute(traverse_tick)

            if status == BT.FAILURE:
                i += 1
            else:
                break

        traverse_tick.get_blackboard().set('i', i, traverse_tick.get_tree().id, self.id)
        return status

        
