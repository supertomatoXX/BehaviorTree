import BT
import time

#__all__ = ['Wait']

class Wait(BT.Action):
    def __init__(self,  param , child=None):
        param_type = ['seconds']
        super(Wait, self).__init__(param, param_type)
        self.end_time = int(param['seconds'])

    def on_first_enter(self, traverse_tick):
        start_time = time.time()
        traverse_tick.tree.set_data('start_time', start_time, self.id)

    def tick(self, traverse_tick):
        curr_time = time.time()

        start_time = traverse_tick.tree.get_data('start_time', self.id)

        print("wait tick:", curr_time, start_time, self.end_time, curr_time-start_time)
        if (curr_time-start_time > self.end_time):
            return BT.SUCCESS

        return BT.RUNNING