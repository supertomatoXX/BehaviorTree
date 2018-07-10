import BT
import time

__all__ = ['Wait']

class Wait(BT.Action):
    def __init__(self, param):
        super(Wait, self).__init__()
        self.end_time = int(param['seconds'])

    def enter(self, traverse_tick):
        start_time = time.time()
        traverse_tick.get_blackboard().set('start_time', start_time, traverse_tick.get_tree().id, self.id)

    def tick(self, traverse_tick):
        curr_time = time.time()
        tree = traverse_tick.get_tree()
        blackboard = traverse_tick.get_blackboard()

        start_time = blackboard.get('start_time', tree.id, self.id)

        print("wait tick:", curr_time, start_time, self.end_time, curr_time-start_time)
        if (curr_time-start_time > self.end_time):
            return BT.SUCCESS

        return BT.RUNNING