# -*- coding: utf-8 -*
import BT


class IfElse(BT.Condition):
    def __init__(self, param, child):
        super(IfElse, self).__init__(param, child)



    def tick(self, tree):
        status = self.child[0]._execute(tree)
        child_count = len(self.child)
        
        if status == BT.SUCCESS:
            if child_count >1 :
                status = self.child[1]._execute(tree)
        else:
            if child_count >2 :
                status = self.child[2]._execute(tree)

        return status

