# -*- coding: utf-8 -*
import BT


class Parallel(BT.Composite):

    def __init__(self, param, child ):
        super(Parallel, self).__init__(param, child)


    def tick(self, tree):
        status = BT.SUCCESS
        for node in self.child:
            child_status = node._execute(tree)

            if child_status != BT.SUCCESS:
                status =  child_status

        return status
