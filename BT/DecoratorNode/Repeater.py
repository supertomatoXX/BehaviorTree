# -*- coding: utf-8 -*
import BT

#__all__ = ['Repeater']

class Repeater(BT.Decorator):
    def __init__(self, child, param ):
        super(Repeater, self).__init__(child)

        self.max_loop = int(param['max_loop'])

    def enter(self, traverse_tick):
        traverse_tick.get_blackboard().set('i', 0, traverse_tick.get_tree().id, self.id)

    #to do
    def tick(self, traverse_tick):
        if not self.child:
            return BT.ERROR


        tree = traverse_tick.get_tree()
        blackboard = traverse_tick.get_blackboard()
        
        i = blackboard.get('i', tree.id, self.id)
        status = BT.SUCCESS

        while self.max_loop < 0 or i < self.max_loop:
            status = self.child._execute(traverse_tick)


            if status == BT.SUCCESS or status == BT.FAILURE:
                i += 1
            else:
                break

        blackboard.set('i', i, tree.id, self.id)
        return status

        
