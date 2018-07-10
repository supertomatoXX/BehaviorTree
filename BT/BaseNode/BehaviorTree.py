# -*- coding: utf-8 -*
import uuid
import itertools
import BT

#__all__ = ['BehaviorTree']

class BehaviorTree(object):
    def __init__(self):
        self.id = str(uuid.uuid1())
        self.node_title = 'BehaviorTree'
        self.root = None
        #self.blackboard = None

    def __del__(self):
        if self.blackboard:
            self.blackboard.del_tree_data(self.id)

    def get_id(self):
        return self.id


    def execute(self,  blackboard):
        self.blackboard = blackboard
        traverse_tick = BT.TraverseTick(self, blackboard)
        # Tick node
        state = self.root._execute(traverse_tick)

        return state
