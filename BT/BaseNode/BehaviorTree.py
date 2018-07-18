# -*- coding: utf-8 -*
import uuid
import itertools
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
            print("set begin node error: node path is not str")
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
        begin_node = self.get_node_by_path(node_path)
        if begin_node:
            self.set_begin_node(begin_node)


    def set_node_extra_param_by_dict( self, node, param_dict, cur_path):
        #结点名字收集
        child_map = {}
        if not isinstance(node, list):
            child_map[node.name] = node
        else:
            for child in node:
                child_map[child.name] = child


        for k in param_dict:
            cur_path = "%s.%s" %(cur_path, k)
            node = child_map.get(k)
            if node:
                v = param_dict[k]
                extra_param = v.get("extra_param")
                if extra_param:
                    #print("set node extra param", node.name, extra_param)
                    self.set_data("extra_param", extra_param, node.id)
                    del v["extra_param"]

                    if v:
                        self.set_node_extra_param_by_dict( node.child, v, cur_path)
            else:
                print(("set extra param by dict error: key %s error" %cur_path))
                return


#param_dict = {
#        "Root":{ 
#                "extra_param":"test1",                      #extra_param key为对应结点的参数
#
#                "Selection":{                               #其它key为其它结点的param dict
#                            "extra_param":"test",
#
#                                "TickCount":{
#                                                "extra_param":5,
#
#                                            "Sequence":{
#                                                "extra_param":6
#                                                }
#                                            },
#
#                                "Sequence":{
#                                            "extra_param":7,
#
#                                            "Wait":{
#                                                "extra_param":8
#                                                },
#
#                                            "MoveToPoint":{
#                                                "extra_param":9
#                                                }
#                                            },
#
#                            },
#                }
#    }



    def set_extra_param_by_dict( self, param_dict):
        self.set_node_extra_param_by_dict( self.root, param_dict, "")


    def set_extra_param_by_path( self, extra_param, path):
        node = self.get_node_by_path(path)
        if node:
            self.set_data("extra_param", extra_param, node.id)

    def set_data( self, key, value, node_id = None):
        self.black_board.set( key, value, node_id)

    def get_data( self, key, node_id = None):
        return self.black_board.get( key, node_id)