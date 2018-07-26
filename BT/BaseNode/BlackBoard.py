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
            node_data = self.data["node_datas"][node_id]

        return node_data

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
        if node_data:
            return node_data.get(key)

        return None

    def del_node_data( self, node_id):
        self.data["node_datas"][node_id]={}

