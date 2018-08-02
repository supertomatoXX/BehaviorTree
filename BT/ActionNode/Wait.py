import BT
import time

#__all__ = ['Wait']

class Wait(BT.Action):
    def __init__(self,  param , child=None):
        param_type = ['seconds']
        super(Wait, self).__init__(param, param_type, child)

    def init_param(self, tree):
        tree.set_data('end_time', int(self.param['seconds']), self.id)

    def on_enter(self, tree):
        start_time = time.time()
        tree.set_data('start_time', start_time, self.id)

    def tick(self, tree):
        curr_time = time.time()

        start_time = tree.get_data('start_time', self.id)

        print("wait tick:", curr_time, start_time, tree.get_data('end_time', self.id), curr_time-start_time)
        if (curr_time-start_time > tree.get_data('end_time', self.id)):
            return BT.SUCCESS

        return BT.RUNNING