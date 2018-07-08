# -*- coding: utf-8 -*
import BT
import math

__all__ = ['DistanceToTargetShorterThan']

class DistanceToTargetShorterThan(BT.Condition):
    def __init__(self, param):
        super(DistanceToTargetShorterThan, self).__init__()
        self.distance = param['distance']
        self.x1 = param['x1']
        self.z1 = param['z1']
        self.x2 = param['x2']
        self.z2 = param['z2']



    def tick(self, traverse_tick):
        print("11111111")
        cur_distance = math.sqrt(math.pow(self.x1-self.x2,2)+math.pow(self.z1-self.z2,2))
        print("2222222")
        if cur_distance < self.distance:
            print("333333")
            return BT.SUCCESS

        print("44444")
        return BT.RUNNING