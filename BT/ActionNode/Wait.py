# -*- coding: utf-8 -*
import BT
import time

__all__ = ['Wait']

class Wait(BT.Action):
    def __init__(self, milliseconds=0):
        super(Wait, self).__init__()
        self.end_time = milliseconds/1000.

    def enter(self, traverse_tick):
        start_time = time.time()
        traverse_tick.get_blackboard().set('start_time', start_time, traverse_tick.get_tree().id, self.id)

    def tick(self, traverse_tick):
        curr_time = time.time()
        start_time = traverse_tick.get_blackboard().get('start_time', traverse_tick.get_tree().id, self.id)

        if (curr_time-start_time > self.end_time):
            return BT.SUCCESS

        return BT.RUNNING