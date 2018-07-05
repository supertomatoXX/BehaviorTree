# -*- coding: utf-8 -*
import BT

__all__ = ['MoveToPoint']

class MoveToPoint(BT.Action):
    def __init__(self, des_pos = [0,0,0]):
        super(MoveToPoint, self).__init__()
        self.des_pos = des_pos


    def tick(self, traverse_tick):
        print("mvoe to point", self.des_pos)
        return BT.SUCCESS