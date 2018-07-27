# -*- coding: utf-8 -*
import uuid
import itertools
import copy
import BT

#__all__ = ['BehaviorTree']

class BehaviorTree(object):
    def __init__(self, root ):
        self.root = root                        #行为树根结点
        self.black_board = BT.BlackBoard(self)      #行为树黑板用于行为树的数据缓存

    def destory(self):
        del self.black_board
    

    def execute(self ):
        begin_node = self.get_data("begin_node" )
        if begin_node:
            return begin_node._execute(self)
        else:
            return  self.root._execute(self)




    def set_begin_node( self, node):
        self.set_data("begin_node", node )



    def del_begin_node(self):
        begin_nodes = self.get_data('begin_node', self)
        if begin_nodes:
            self.set_data('is_enter', False, begin_nodes)

        self.set_data("begin_node", None)

    def get_node_by_path( self, node_path ):
        if not isinstance(node_path, str):
            print("get node by path error: node path is not str")
            return

        node_path = node_path.split(".")
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
                    print("get node by path error:", node_path[:i])
                    node = None
                    break
            else:
                if node_name != node.name:
                    print("get node by path error:", node_path[:i])
                    node = None
                    break

            if i < len(node_path ) -1 :
                node = node.child

        return node


    #node_path="name1.name2.name3.name4",以.分割
    def set_begin_node_by_path( self, node_path):
        begin_node = self.get_node_by_path(node_path)
        if begin_node:
            self.set_begin_node(begin_node)


#    def set_node_param_by_dict( self, node, param_dict, cur_path):
#        #结点名字收集
#        child_map = {}
#
#        if not isinstance(node, list):
#            child_map[node.name] = node
#        else:
#            for child in node:
#                child_map[child.name] = child
#
#
#
#        for k in param_dict:
#            if k == "extra_param":
#                continue
#
#            node = child_map.get(k)
#            if node:
#                v = param_dict[k]
#                extra_param = v.get("extra_param")
#                if extra_param:
#                    node.set_param_by_dict( extra_param)
#                    
#
#                if hasattr(node, "child"):
#                    self.set_node_param_by_dict( node.child, v, ("%s.%s" %(cur_path, k)))
#            else:
#                path = "%s.%s" %(cur_path, k)
#                print(("set extra param by dict error: key %s error" %path))
#                return


#    def set_node_param_by_dict( self, node, param_dict, cur_path):
#        for k in param_dict:
#            if k == "extra_param":
#                node.set_param_by_dict( param_dict["extra_param"])
#                continue
#
#            child = node.get_child_by_name(k)
#            if child is not None:
#                self.set_node_param_by_dict( child, param_dict[k], ("%s.%s" %(cur_path, k)))
#            else:
#                path = "%s.%s" %(cur_path, k)
#                print(("set extra param by dict error: key %s error" %path))



#    test_dict = {
#        "Root":{ 
#                "extra_param":{"test1":1},                      #extra_param key为对应结点的参数
#
#                "Selection":{                               #其它key为其它结点的param dict
#                                "extra_param":{"test2":2},
#
#                                    "TickCount":{
#                                            "extra_param":{"count":5},
#
#                                            "Sequence":{
#                                                "extra_param":{
#                                                }
#                                            },
#                                    },
#
#                                "Sequence":{
#                                            "extra_param":{"test4":7},
#
#                                            "Wait":{
#                                                "extra_param":{"end_time":8},
#                                                },
#
#                                            "MoveToPoint":{
#                                                "extra_param":{"x":9}
#                                                }
#                                            },
#
#                            },
#                }
#    


    def set_param( self, param_dict):
        root_param = param_dict.get(self.root.name)
        if root_param is None:
            print("set extra param by dict error: cannot get root param" )
            return
        
        self.root.set_param_by_dict( self, root_param, self.root.name)


    def set_param_by_path( self, param_dict, path):
        node = self.get_node_by_path(path)
        if node:
            node_param = param_dict.get(node.name)
            if node_param is None:
                print("set extra param by dict error: cannot get not param %s" %path )
                return
            node.set_param_by_dict( self, node_param, path)
        else:
            print("set param by path error:cannot get node by path %s" %path)

    def reset_node_by_path( self, path):
        node = self.get_node_by_path(path)
        if node:
            node.reset(self)

                        

    def set_data( self, key, value, node_id = None):
        self.black_board.set( key, value, node_id)

    def get_data( self, key, node_id = None):
        return self.black_board.get( key, node_id)

    def del_node_data( self, node_id):
        self.black_board.del_node_data(node_id)

    def reset(self):
        del self.black_board
        self.black_board = BT.BlackBoard(self)
    
    def dump(self):
        print("BehaviorTree:", self )
        self.black_board.dump()
        #self.root.dump()