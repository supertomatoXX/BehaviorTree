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

    def _execute(self, tick):
        self._enter(tick)

        if (not tick.blackboard.get('is_open', tick.tree.id, self.id)):
            self._open(tick)

        status = self._tick(tick)

        if (status != BT.RUNNING):
            self._close(tick)

        self._exit(tick)

        return status

    def _enter(self, tick):
        tick._enter_node(self)
        self.enter(tick)

    def _open(self, tick):
        tick._open_node(self)
        tick.blackboard.set('is_open', True, tick.tree.id, self.id)
        self.open(tick)

    def _tick(self, tick):
        tick._tick_node(self)
        return self.tick(tick)

    def _close(self, tick):
        tick._close_node(self)
        tick.blackboard.set('is_open', False, tick.tree.id, self.id)
        self.close(tick)

    def _exit(self, tick):
        tick._exit_node(self)
        self.exit(tick)

    def enter(self, tick): pass
    def open(self, tick): pass
    def tick(self, tick): pass
    def close(self, tick): pass
    def exit(self, tick): pass