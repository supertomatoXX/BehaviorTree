# -*- coding: utf-8 -*
import BT

#__all__ = ['MoveToPoint']

class MoveToPoint(BT.Action):
    def __init__(self,  param, child=None):
        param_type = ['x', 'y', 'z']
        super(MoveToPoint, self).__init__(param, param_type)
        self.des_pos = "x=%s,y=%s,z=%s" %(param['x'], param['y'],param['z'])


    def tick(self, traverse_tick):
        print("move to pos", self.des_pos)
        return BT.SUCCESS