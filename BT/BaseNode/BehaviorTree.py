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
        
        begin_node = self.get_data("begin_node" )
        if begin_node:
            status = begin_node._execute(self)
        else:
            status =  self.root._execute(self)

        return status


        



    def set_begin_node( self, node):
        self.set_data("begin_node", node )



    def del_begin_node(self):
        begin_nodes = self.get_data('begin_node', self)
        if begin_nodes:
            self.set_data('is_enter', False, begin_nodes)

        self.set_data("begin_node", None)

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


    #node_path="name1,name2,name3,name4",以逗号分割
    def set_begin_node_by_path( self, node_path):
        if not isinstance(node_path, str):
            print("set begin node error: node path is not str")
            return

        node_path = node_path.split(",")
        begin_node = self.get_node_by_path(node_path)
        if begin_node:
            self.set_begin_node(begin_node)

    def set_extra_param(self, param):
        pass

    def set_extra_param_by_dict( self, param_dict):
        pass

    def set_node_extra_param_by_path( self, param, node_path):
        node = self.get_node_by_path(node_path)
        if node:
            self.set_data('extra_param', param, node.id)



    def set_data( self, key, value, node_id = None):
        self.black_board.set( key, value, node_id)

    def get_data( self, key, node_id = None):
        return self.black_board.get( key, node_id)