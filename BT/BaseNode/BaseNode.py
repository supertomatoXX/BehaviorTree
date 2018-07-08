# -*- coding: utf-8 -*
import BT
import uuid

__all__ = ['BaseNode']

class BaseNode(object):
    node_type = None
    node_title = None
    node_desc = None

    def __init__(self):
        self.id = str(uuid.uuid1())
        self.node_title = self.node_title or self.__class__.__name__
        self.node_desc = self.node_desc or ''
        self.parameters = {}
        self.properties = {}

    @property
    def name(self):
        return self.__class__.__name__

    def _execute(self, traverse_tick):
        print("baes node execute")
        self._enter(traverse_tick)
        status = self._tick(traverse_tick)
        self._exit(traverse_tick)
        return status

    def _enter(self, traverse_tick):
        if (not traverse_tick.get_blackboard().get('is_enter', traverse_tick.get_tree().get_id(), self.id)):
            traverse_tick.get_blackboard().set('is_enter', True, traverse_tick.get_tree().get_id(), self.id)
            self.enter(traverse_tick)


    def _tick(self, traverse_tick):
        return self.tick(traverse_tick)


    def _exit(self, traverse_tick):
        traverse_tick.get_blackboard().set('is_enter', False, traverse_tick.get_tree().get_id(), self.id)
        self.exit(traverse_tick)

    def enter(self, traverse_tick): pass
    def tick(self, traverse_tick): pass
    def exit(self, traverse_tick): pass