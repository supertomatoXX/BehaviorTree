# -*- coding: utf-8 -*
import BT

__all__ = ['TickCount']

class TickCount(BT.Decorator):
    def __init__(self, child, param ):
        super(TickCount, self).__init__(child)

        self.count = int(param['count'])

    def enter(self, traverse_tick):
        traverse_tick.get_blackboard().set('i', 0, traverse_tick.get_tree().id, self.id)


    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR


        tree = traverse_tick.get_tree()
        blackboard = traverse_tick.get_blackboard()

        i = blackboard.get('i', tree.id, self.id)
        if (i < self.count ):
            self.child._execute(traverse_tick)
            i += 1
            blackboard.set('i', i, tree.id, self.id)
            return BT.RUNNING

        return BT.SUCCESS
