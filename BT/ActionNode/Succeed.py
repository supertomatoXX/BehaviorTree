# -*- coding: utf-8 -*
import BT

__all__ = ['Succeeder']

class Succeed(BT.Action):
    def tick(self, tick):
        print("Succeed tick"+self.id)
        return BT.SUCCESS;