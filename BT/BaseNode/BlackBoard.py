# -*- coding: utf-8 -*
__all__ = ['BlackBoard']

class BlackBoard(object):
    def __init__(self):
        self._normal_data = {}
        self._tree_data = {}

    def _get_tree_data(self, tree_id):
        if (tree_id not in self._tree_data):
            self._tree_data[tree_id] = {
                'node_data': {},
                'open_nodes': []
            }

        return self._tree_data[tree_id]

    def _get_node_data(self, tree_data, node_id):
        data = tree_data['node_data']

        if (node_id not in data):
            data[node_id] = {}

        return data[node_id]

    def _get_data(self, tree_id, node_id):
        data = self._normal_data

        if (tree_id is not None):
            data = self._get_tree_data(tree_id)

            if (node_id is not None):
                data = self._get_node_data(data, node_id)

        return data

    def set(self, key, value, tree_id=None, node_id=None):
        data = self._get_data(tree_id, node_id)
        data[key] = value

    def get(self, key, tree_id=None, node_id=None):
        data = self._get_data(tree_id, node_id)
        return data.get(key)