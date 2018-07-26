# -*- coding: utf-8 -*
import BT

#__all__ = ['TickCount']

class TickCount(BT.Decorator):
    def __init__(self, param, child ):
        param_type = ['count']
        super(TickCount, self).__init__(param, param_type, child)

        self.init_param()

    def init_param(self):
        self.count = int(self.param['count'])

    def on_enter(self, tree):
        tree.set_data('i', 0,  self.id)


    def tick(self, tree):
        if not self.child:
            return BT.ERROR

        i = tree.get_data('i', self.id)
        if (i < self.count ):
            self.child._execute(tree)
            i += 1
            tree.set_data('i', i, self.id)
            return BT.RUNNING 

        return BT.SUCCESS
