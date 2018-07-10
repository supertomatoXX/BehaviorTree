# -*- coding: utf-8 -*
import BT

#__all__ = ['RepeatUntilSuccess']

class RepeatUntilSuccess(BT.Decorator):
    def __init__(self, child, param):
        param_type = ['max_loop']
        super(RepeatUntilSuccess, self).__init__(child, param, param_type)

        self.max_loop = int(param['max_loop'])

    def on_enter(self, traverse_tick):
        traverse_tick.blackboard.set('i', 0, traverse_tick.tree.id, self.id)

    #to do
    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR
        
        i = traverse_tick.blackboard.get('i', traverse_tick.tree.id, self.id)
        while self.max_loop < 0 or i < self.max_loop:
            status = self.child._execute(traverse_tick)

            if status != BT.SUCCESS:
                i += 1
            else:
                break

        traverse_tick.blackboard.set('i', i, traverse_tick.tree.id, self.id)
        return status

        
