# -*- coding: utf-8 -*
import BT

#__all__ = ['MoveToPoint']

class MoveToPoint(BT.Action):
    def __init__(self,  param, child=None):
        param_type = ['x', 'y', 'z']
        super(MoveToPoint, self).__init__(param, param_type)
        self.init_param()

    def init_param(self):
        self.x = self.param['x']
        self.y = self.param['y']
        self.z = self.param['z']

    def tick(self, tree):
        print("move to pos", "x=%s,y=%s,z=%s" %(self.param['x'], self.param['y'], self.param['z']))
        return BT.SUCCESS