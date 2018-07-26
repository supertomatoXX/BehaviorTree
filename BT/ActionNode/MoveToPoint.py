# -*- coding: utf-8 -*
import BT

#__all__ = ['MoveToPoint']

class MoveToPoint(BT.Action):
    def __init__(self,  param, child=None):
        param_type = ['x', 'y', 'z']
        super(MoveToPoint, self).__init__(param, param_type)

    def init_param(self, tree):
        tree.set_data("x", self.param['x'], self.id)
        tree.set_data("y", self.param['y'], self.id)
        tree.set_data("z", self.param['z'], self.id)

    def tick(self, tree):
        print("move to pos", "x=%s,y=%s,z=%s" %(tree.get_data("x", self.id), tree.get_data("y", self.id), tree.get_data("z", self.id)))
        return BT.SUCCESS