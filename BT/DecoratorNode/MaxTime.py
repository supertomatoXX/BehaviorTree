# -*- coding: utf-8 -*
import BT
import time

__all__ = ['MaxTime']

class MaxTime(BT.Decorator):
    def __init__(self, child, max_time=0):
        super(MaxTime, self).__init__(child)

        self.max_time = max_time

    def enter(self, traverse_tick):
        t = time.time()
        traverse_tick.get_blackboard().set('startTime', t, traverse_tick.get_tree().id, self.id)

    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR

        currTime = time.time();
        startTime = traverse_tick.get_blackboard().get('startTime', traverse_tick.get_tree().id, self.id);
        
        status = self.child._execute(tick);
        if (currTime - startTime > self.max_time):
            return BT.FAILURE;
        
        return status;
        
