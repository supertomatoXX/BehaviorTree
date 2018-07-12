# -*- coding: utf-8 -*
import uuid
#__all__ = ['BlackBoard']

'''
blackboard = {
    normal_data = {}
    datas = {
        [tree_id] = {}
            [data_id] = {
                    node_data = {
                        [node_id] = {
                            key = value
                        }
                    }

                    key = value

            }
        }
    }
}
'''

class BlackBoard(object):
    def __init__(self):
        self.datas = {}

    def _get_tree_data(self, tree_scope):
        if tree_scope.id in self.datas:
            return self.datas[tree_scope.id][tree_scope.data_id]

        return self.gen_data( tree_scope )

    def _get_node_data(self, tree_scope, node_scope):
        data = tree_scope['node_data']

        if (node_scope not in data):
            data[node_scope] = {}

        return data[node_scope]

    def _get_data(self, tree_scope=None, node_scope=None):
        data = None

        if (tree_scope is not None):
            data = self._get_tree_data(tree_scope)

            if (node_scope is not None):
                data = self._get_node_data(data, node_scope)

        return data

    def set(self, key, value, tree_scope=None, node_scope=None):
        data = self._get_data(tree_scope, node_scope)
        data[key] = value

    def get(self, key, tree_scope=None, node_scope=None):
        data = self._get_data(tree_scope, node_scope)
        return data.get(key)

    def del_data(self, tree_scope, data_id=None):
        if data_id is None:
            del self.datas[tree_scope.id]
            return

        del self.datas[tree_scope.id][data_id]

    def gen_data(self, tree_scope, data_id = None):
        if data_id is None:
            data_id = str(uuid.uuid1())

        if not tree_scope.id in self.datas:
            self.datas[tree_scope.id] = {
                    data_id:{
                        'node_data': {},
                    }
                }

            return data_id

        if data_id in self.datas[tree_scope.id]:
            return None

        self.datas[tree_scope.id][data_id] = {
                'node_data': {},
            }
        return data_id

