# -*- coding: utf-8 -*
import BT

__all__ = ['MemPriority']

class MemPriority(BT.Composite):
    def __init__(self, children=None):
        super(MemPriority, self).__init__(children)

    def enter(self, traverse_tick):
        traverse_tick.get_blackboard().set('running_child', 0, traverse_tick.get_tree().id, self.id)

    def tick(self, traverse_tick):
        idx = traverse_tick.get_blackboard().get('running_child', traverse_tick.get_tree().id, self.id)

        for i in xrange(idx, len(self.children)):
            node = self.children[i]
            status = node._execute(tick)

            if status != BT.FAILURE:
                if status == BT.RUNNING:
                    traverse_tick.get_blackboard().set('running_child', i, traverse_tick.get_tree().id, self.id)
                return status

        return BT.FAILURE
