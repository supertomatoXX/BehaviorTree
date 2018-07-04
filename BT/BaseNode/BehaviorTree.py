# -*- coding: utf-8 -*
import uuid
import itertools
import BT

__all__ = ['BehaviorTree']

class BehaviorTree(object):
    def __init__(self):
        self.id = str(uuid.uuid1())
        self.node_title = 'BehaviorTree'
        self.node_desc = ''
        self.properties = {}
        self.root = None



    def execute(self,  blackboard):

        tick = BT.Tick()
        tick.blackboard = blackboard
        tick.tree = self

        # Tick node
        state = self.root._execute(tick)

        # Close node from last tick, if needed
        last_open_nodes = blackboard.get('open_nodes', self.id)
        curr_open_nodes = tick._open_nodes

        start = 0
        for node1, node2 in itertools.izip(last_open_nodes, curr_open_nodes):
            start += 1
            if node1 != node2:
                break

        # - close nodes
        for i in xrange(len(last_open_nodes)-1, start-1, -1):
            last_open_nodes[i]._close(tick);

        # Populate blackboard
        blackboard.set('open_nodes', curr_open_nodes, self.id)
        blackboard.set('node_count', tick._node_count, self.id)