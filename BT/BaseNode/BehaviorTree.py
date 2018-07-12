# -*- coding: utf-8 -*
import uuid
import itertools
import BT

#__all__ = ['BehaviorTree']

class BehaviorTree(object):
    def __init__(self, black_board, data_id = None):
        self.id = str(uuid.uuid1())
        self.node_title = 'BehaviorTree'
        self.root = None
        self.black_board = black_board
        if data_id:
            self.data_id = data_id
        else:
            self.data_id = black_board.gen_data(self)


    def destory(self):
        if self.black_board:
            self.black_board.del_data(self)        
        

    def execute(self ):
        traverse_tick = BT.TraverseTick(self, self.black_board)
        
        begin_node = self.black_board.get("begin_node", self)
        if begin_node:
            return begin_node._execute(traverse_tick)
        
        return self.root._execute(traverse_tick)

    def set_data_id( self, data_id ):
        self.data_id = data_id

    def set_extra_param( self, param):
        self.black_board.set('extra_param', param, self)
