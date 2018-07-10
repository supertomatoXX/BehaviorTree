# -*- coding: utf-8 -*
import BT
import uuid

#__all__ = ['BaseNode']

class BaseNode(object):
    node_type = None
    node_title = None


    def __init__(self):
        self.id = str(uuid.uuid1())
        self.node_title = self.node_title or self.__class__.__name__


    @property
    def name(self):
        return self.__class__.__name__

    def _execute(self, traverse_tick):
        print("execute node", self.name)

        self._enter(traverse_tick)

        status = self.tick(traverse_tick)

        if (status != BT.RUNNING):
            self._exit(traverse_tick)
            
        return status

    def _enter(self, traverse_tick):
        tree = traverse_tick.get_tree()
        black_board = traverse_tick.get_blackboard()

        if (not black_board.get('is_enter', tree.get_id(), self.id)):
            black_board.set('is_enter', True, tree.get_id(), self.id)
            self.enter(traverse_tick)


    def tick(self, traverse_tick):
        return self.tick(traverse_tick)


    def _exit(self, traverse_tick):
        tree = traverse_tick.get_tree()
        black_board = traverse_tick.get_blackboard()

        black_board.set('is_enter', False, tree.get_id(), self.id)
        self.exit(traverse_tick)

    def enter(self, traverse_tick): pass
    def exit(self, traverse_tick): pass