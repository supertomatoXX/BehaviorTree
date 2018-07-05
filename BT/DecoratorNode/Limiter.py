# -*- coding: utf-8 -*
import BT

__all__ = ['Limiter']

class Limiter(BT.Decorator):
    def __init__(self, child, max_loop):
        super(Limiter, self).__init__(child)

        self.max_loop = max_loop

    def enter(self, traverse_tick):
        traverse_tick.get_blackboard().set('i', 0, traverse_tick.get_tree().id, self.id)

    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR

        i = traverse_tick.get_blackboard().get('i', traverse_tick.get_tree().id, self.id)
        if i < self.max_loop:
            status = self.child._execute(tick)

            if status == BT.SUCCESS or status == BT.FAILURE:
                traverse_tick.get_blackboard().set('i', i+1, traverse_tick.get_tree().id, self.id)

            return status

        return BT.FAILURE
        
