# -*- coding: utf-8 -*
import BT

#__all__ = ['Failer']

class Failure(BT.Action):
    def tick(self, tree):
        return BT.FAILURE;