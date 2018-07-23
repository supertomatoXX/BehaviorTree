# -*- coding: utf-8 -*
import BT
import math

#__all__ = ['DistanceToTargetShorterThan']

class DistanceToTargetShorterThan(BT.Condition):
    def __init__(self, param, child=None):
        param_type = ['distance','x1','z1','x2','z2']
        super(DistanceToTargetShorterThan, self).__init__(param, param_type, child)
        self.init_param()

    def init_param(self):
        self.distance = int(self.param['distance'])
        self.x1 = int(self.param['x1'])
        self.z1 = int(self.param['z1'])
        self.x2 = int(self.param['x2'])
        self.z2 = int(self.param['z2'])


    def tick(self, tree):
        cur_distance = math.sqrt(math.pow(self.x1-self.x2,2)+math.pow(self.z1-self.z2,2))
        if cur_distance < self.distance:
            return BT.SUCCESS

        return BT.FAILURE