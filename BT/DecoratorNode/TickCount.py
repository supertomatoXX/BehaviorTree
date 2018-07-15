# -*- coding: utf-8 -*
import BT

#__all__ = ['TickCount']

class TickCount(BT.Decorator):
    def __init__(self, param, child ):
        param_type = ['count']
        super(TickCount, self).__init__(param, param_type, child)

        self.count = int(param['count'])

    def on_first_enter(self, traverse_tick):
        traverse_tick.blackboard.set('i', 0, traverse_tick.tree, self.id)


    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR

        i = traverse_tick.blackboard.get('i', traverse_tick.tree, self.id)
        if (i < self.count ):
            self.child._execute(traverse_tick)
            i += 1
            traverse_tick.blackboard.set('i', i, traverse_tick.tree, self.id)
            traverse_tick.tree.set_begin_node( self )
            return BT.RUNNING 

        return BT.SUCCESS
