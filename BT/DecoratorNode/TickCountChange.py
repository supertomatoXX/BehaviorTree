# -*- coding: utf-8 -*
import BT


class TickCountChange(BT.Decorator):
    def __init__(self, param, child ):
        param_type = ['count']
        super(TickCountChange, self).__init__(param, param_type, child)

        self.count = int(param['count'])

    def on_first_enter(self, tree):
        tree.set_data('i', 0, self.id)



    def tick(self, tree):
        if not self.child:
            return BT.ERROR

        extra_param = tree.get_data('extra_param', self.id)

        count = self.count
        if extra_param and ("tick_count_change" in extra_param):
            count = extra_param["tick_count_change"]

        i = tree.get_data('i', self.id)
        if (i < count ):
            self.child._execute(tree)
            i += 1
            tree.set_data('i', i, self.id)
            return BT.RUNNING

        return BT.SUCCESS
