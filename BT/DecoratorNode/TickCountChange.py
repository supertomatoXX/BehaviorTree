# -*- coding: utf-8 -*
import BT


class TickCountChange(BT.Decorator):
    def __init__(self, child, param ):
        param_type = ['count']
        super(TickCountChange, self).__init__(child, param, param_type)

        self.count = int(param['count'])

    def on_enter(self, traverse_tick):
        traverse_tick.blackboard.set('i', 0, traverse_tick.tree, self.id)



    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR

        extra_param = traverse_tick.blackboard.get('extra_param', traverse_tick.tree)

        if extra_param and ("tick_count_change" in extra_param):
            self.count = extra_param["tick_count_change"]

        i = traverse_tick.blackboard.get('i', traverse_tick.tree, self.id)
        if (i < self.count ):
            self.child._execute(traverse_tick)
            i += 1
            traverse_tick.blackboard.set('i', i, traverse_tick.tree, self.id)
            return BT.RUNNING

        return BT.SUCCESS
