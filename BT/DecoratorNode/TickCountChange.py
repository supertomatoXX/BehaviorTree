# -*- coding: utf-8 -*
import BT


class TickCountChange(BT.Decorator):
    def __init__(self, param, child ):
        param_type = ['count']
        super(TickCountChange, self).__init__(param, param_type, child)

        self.count = int(param['count'])

    def on_first_enter(self, traverse_tick):
        traverse_tick.tree.set_data('i', 0, self.id)



    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR

        tree = traverse_tick.tree
        extra_param = tree.get_data('extra_param', self.id)

        if extra_param and ("tick_count_change" in extra_param):
            self.count = extra_param["tick_count_change"]

        i = tree.get_data('i', self.id)
        if (i < self.count ):
            self.child._execute(traverse_tick)
            i += 1
            tree.set_data('i', i, self.id)
            tree.set_begin_node( self )
            return BT.RUNNING

        return BT.SUCCESS
