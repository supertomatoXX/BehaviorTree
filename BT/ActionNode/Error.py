# -*- coding: utf-8 -*
import BT

__all__ = ['Error']

class Error(BT.Action):
    def tick(self, tick):
        return BT.ERROR;