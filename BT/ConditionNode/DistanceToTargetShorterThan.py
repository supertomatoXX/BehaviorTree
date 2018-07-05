# -*- coding: utf-8 -*
import BT
import math

__all__ = ['DistanceToTargetShorterThan']

class DistanceToTargetShorterThan(BT.Condition):
    def __init__(self, distance, target_pos=[0,0], self_pos = [0,0]):
        super(DistanceToTargetShorterThan, self).__init__()
        self.node_title = 'DistanceToTargetShorterThan'
        self.node_desc = '与目标的距离小于给定的距离'
        

        self.distance = distance
        self.target_pos = target_pos
        self.self_pos = self_pos



    def tick(self, traverse_tick):
        cur_distance = math.sqrt(math.pow(self.target_pos[0]-self.self_pos[0],2)+math.pow(self.target_pos[1]-self.self_pos[1],2))
        if cur_distance < self.distance:
            return BT.SUCCESS

        return BT.RUNNING