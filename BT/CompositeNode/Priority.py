# -*- coding: utf-8 -*
import BT

__all__ = ['Priority']

class Priority(BT.Composite):
    def __init__(self, children=None):
        super(Priority, self).__init__(children)

    def tick(self, tick):
        for node in self.children:
            status = node._execute(tick)

            if status != BT.FAILURE:
                return status

        return BT.FAILURE
