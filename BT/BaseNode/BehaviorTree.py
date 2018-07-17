# -*- coding: utf-8 -*
import uuid
import itertools
import BT

#__all__ = ['BehaviorTree']

class BehaviorTree(object):
    def __init__(self, root ):
        self.id = str(uuid.uuid1())
        self.root = root                        #行为树根结点
        self.black_board = BT.BlackBoard(self)      #行为树黑板用于行为树的数据缓存


    def destory(self):
        if self.black_board:
            self.black_board.destory()        
    

    def execute(self ):
        traverse_tick = BT.TraverseTick(self)
        
        begin_node = self.get_data("begin_node" )
        if begin_node:
            status = begin_node._execute(traverse_tick)
        else:
            status =  self.root._execute(traverse_tick)

        return status

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
        
        



    def set_begin_node( self, node):
        self.set_data("begin_node", node, self)
        '''
        running_nodes = self.black_board.get('running_nodes', self)
        if running_nodes:
            for i in xrange(len(running_nodes)-1):
                black_board.set('is_enter', False, self, running_nodes[i])
        '''


    def del_begin_node(self):
        begin_nodes = self.get_data('begin_node', self)
        if begin_nodes:
            self.set_data('is_enter', False, begin_nodes)

        self.set_data("begin_node", None, self)

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
            self.set_data('extra_param', param, node.id)



    def set_data( self, key, value, node_id = None):
        self.black_board.set( key, value, node_id)

    def get_data( self, key, node_id = None):
        return self.black_board.get( key, node_id)