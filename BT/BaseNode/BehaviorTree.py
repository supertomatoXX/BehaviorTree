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

    def set_begin_node( self, node):
        self.black_board.set("begin_node", node, self)

    def del_begin_node(self):
        self.black_board.set("begin_node", None, self)

    def get_node_by_path( self, node_path ):
        begin_node = self.root

        for i in range(len(node_path)):
            node_name = node_path[i]["node_name"]
            node_idx = 0

            if "node_idx" in node_path[i]:
                node_idx = node_path[i]["node_idx"]
            
            if isinstance( begin_node, list):
                if node_name == begin_node[node_idx].name:
                    begin_node = begin_node[node_idx]
                else:
                    print("set begin node path error:", node_path[:i])
                    begin_node = None
                    break
  
            else:
                if node_name != begin_node.name:
                    print("set begin node path error:", node_path[:i])
                    begin_node = None
                    break

            if i < len(node_path ) -1 :
                begin_node = begin_node.child

        return begin_node

    def set_begin_node_by_path( self, node_path):
        begin_node = self.get_node_by_path(node_path)
        self.set_begin_node(begin_node)




