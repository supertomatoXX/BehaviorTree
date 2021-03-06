# -*- coding: utf-8 -*
import uuid
#__all__ = ['BlackBoard']

'''
#每棵行为树会有一个blackboard,用于行为树的数据缓存
blackboard.data = {
    "key":value,
    "key":value,
    ...

    ["node_datas"] = {
        [node_id] = {
            "key":value,
            "key":value,
             ...
        }
        [node_id] = {
            "key":value,
            "key":value,
             ...
        }
        ...
    }
}
'''

class BlackBoard(object):
    def __init__(self, behavior_tree):
        self.data = {
            "node_datas":{}
        }

    #def destory(self):
    #    del self.data


    def get_node_data(self, node_id):
        node_data =  self.data["node_datas"].get(node_id)
        if node_data is None:
            self.data["node_datas"][node_id]={}

        return self.data["node_datas"][node_id]


    def set(self, key, value, node_id=None):
        if node_id:
            node_data = self.get_node_data(node_id)
            node_data[key] = value
            return

        self.data[key] = value

    def get(self, key, node_id=None):
        if not node_id:
            return self.data.get(key)

        node_data = self.get_node_data(node_id)
        return node_data.get(key)


    def has( self, key, node_id=None):
        if not node_id:
            return key in self.data 

        node_data = self.get_node_data(node_id)
        return key in node_data


    def del_node_data( self, node_id):
        self.data["node_datas"][node_id]={}

    def dump(self):
        print("black_board:")
        from pprint import pprint
        pprint (vars(self))

        #for k in self.data:
        #    print("%s:%s" %(k, self.data[k]))
#
        #node_datas = self.data.get("node_datas")
        #if node_datas:
        #    for node_id in node_datas:
        #        node_data = node_datas[node_id]
        #        print("node %s data:" %node_id)
        #        for k in node_data:
        #            print("%s:%s" %(k, node_data[k]))
