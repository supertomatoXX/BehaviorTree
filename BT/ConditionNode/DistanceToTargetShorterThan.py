# -*- coding: utf-8 -*
import BT
import math

#__all__ = ['DistanceToTargetShorterThan']

class DistanceToTargetShorterThan(BT.Condition):
    def __init__(self, param, child=None):
        param_type = ['distance','x1','z1','x2','z2']
        super(DistanceToTargetShorterThan, self).__init__(param, param_type, child)

    def init_param(self, tree):
        for name in self.param_type:
            tree.set_data(name, int(self.param[name]), self.id)


    def tick(self, tree):
        cur_distance = math.sqrt(math.pow(tree.get_data("x1",self.id)-tree.get_data("x2", self.id),2)+math.pow(tree.get_data("z1",self.id)-tree.get_data("z2",self.id),2))
        if cur_distance < tree.get_data("distance", self.id):
            return BT.SUCCESS

        return BT.FAILURE