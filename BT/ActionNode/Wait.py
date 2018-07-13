import BT
import time

#__all__ = ['Wait']

class Wait(BT.Action):
    def __init__(self,  param ):
        param_type = ['seconds']
        super(Wait, self).__init__(param, param_type)
        self.end_time = int(param['seconds'])

    def on_enter(self, traverse_tick):
        start_time = time.time()
        traverse_tick.blackboard.set('start_time', start_time, traverse_tick.tree, self.id)

    def tick(self, traverse_tick):
        curr_time = time.time()

        start_time = traverse_tick.blackboard.get('start_time', traverse_tick.tree, self.id)

        print("wait tick:", curr_time, start_time, self.end_time, curr_time-start_time)
        if (curr_time-start_time > self.end_time):
            return BT.SUCCESS

        return BT.RUNNING