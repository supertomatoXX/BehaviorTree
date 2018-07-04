# -*- coding: utf-8 -*
import BT

__all__ = ['Runner']

class Running(BT.Action):
    def tick(self, tick):
        return BT.RUNNING;