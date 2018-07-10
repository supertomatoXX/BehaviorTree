# -*- coding: utf-8 -*
import BT
import uuid

#__all__ = ['BaseNode']

class BaseNode(object):
    node_type = None
    node_title = None


    def __init__(self, param = None, param_type = None):
        if param and param_type:
            if not self.param_check(param, param_type):
                return 

        self.id = str(uuid.uuid1())
        self.node_title = self.node_title or self.__class__.__name__


    @property
    def name(self):
        return self.__class__.__name__

    def _execute(self, traverse_tick):
        print("execute node", self.name)

        self._enter(traverse_tick)
        status = self.tick(traverse_tick)
        self._exit(traverse_tick, status)

        return status

    def _enter(self, traverse_tick):
        tree = traverse_tick.tree
        black_board = traverse_tick.blackboard

        if (not black_board.get('is_enter', tree.id, self.id)):
            black_board.set('is_enter', True, tree.id, self.id)
            self.on_enter(traverse_tick)


    def _exit(self, traverse_tick, status):
        if (status != BT.RUNNING):
            tree = traverse_tick.tree
            black_board = traverse_tick.blackboard

            black_board.set('is_enter', False, tree.id, self.id)
            self.on_exit(traverse_tick)

    def param_check(self, param, param_type):
        for param_name in param_type:
            if param_name not in param:
                print "%s param error: %s" %(self.name, param_name)
                return False

        return True

    def tick(self, traverse_tick): pass
    def on_enter(self, traverse_tick): pass
    def on_exit(self, traverse_tick): pass