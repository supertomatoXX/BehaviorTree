# -*- coding: utf-8 -*
import uuid
import itertools
import BT

#__all__ = ['BehaviorTree']

class BehaviorTree(object):
    def __init__(self, black_board, data_id = None):
        self.id = str(uuid.uuid1())
        self.root = None
        self.black_board = black_board

        self.data_id = black_board.gen_data(self, data_id)


    def destory(self):
        if self.black_board:
            self.black_board.del_tree(self)        
    
    def del_tree(self):
        if self.black_board:
            self.black_board.del_tree_scope(self)  

    def execute(self ):
        traverse_tick = BT.TraverseTick(self, self.black_board)
        
        begin_node = self.black_board.get("begin_node", self)
        if begin_node:
            status = begin_node._execute(traverse_tick)
        else:
            status =  self.root._execute(traverse_tick)


        '''
        running_nodes = traverse_tick.running_nodes
        if running_nodes :
            running_nodes_stack_len = len(running_nodes)
            self.set_begin_node(running_nodes[running_nodes_stack_len-1])

            print( "the running node", running_nodes)
            for i in xrange(len(running_nodes)-1):
                print("node enter false", i, running_nodes[i])
                self.black_board.set('is_enter', False, self, running_nodes[i])
        else:
            self.del_begin_node()
        '''
        
        return status


    def set_data_id( self, data_id ):
        self.data_id = data_id

    def set_extra_param( self, param):
        self.black_board.set('extra_param', param, self)

    def set_begin_node( self, node):
        running_nodes = self.black_board.get('running_nodes', self)
        if running_nodes:
            for i in xrange(len(running_nodes)-1):
                black_board.set('is_enter', False, self, running_nodes[i])

        self.black_board.set("begin_node", node, self)

    def del_begin_node(self):
        begin_nodes = self.black_board.get('begin_node', self)
        if begin_nodes:
            self.black_board.set('is_enter', False, self, begin_nodes)

        self.black_board.set("begin_node", None, self)

    def get_node_by_path( self, node_path ):
        node = self.root

        for i in xrange(len(node_path)):
            node_name = node_path[i]
            
            if isinstance( node, list):
                child = None
                for c in node:
                    if c.name == node_name:
                        child = c
                        break  

                if child is not None:
                    node = child
                else:
                    print("set begin node path error:", node_path[:i])
                    node = None
                    break
            else:
                if node_name != node.name:
                    print("set begin node path error:", node_path[:i])
                    node = None
                    break

            if i < len(node_path ) -1 :
                node = node.child

        return node

    def set_begin_node_by_path( self, node_path):
        begin_node = self.get_node_by_path(node_path)
        if begin_node:
            self.set_begin_node(begin_node)

    def set_node_extra_param_by_path( self, param, node_path):
        node = self.get_node_by_path(node_path)
        if node:
            self.black_board.set('extra_param', param, self, node.id)



