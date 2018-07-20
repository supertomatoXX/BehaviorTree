# -*- coding: utf-8 -*
import BT
import random

#10，20，80，100

class Probability(BT.Composite):

    def __init__(self, param, child ):
        super(Probability, self).__init__(param, child)


    def tick(self, tree):
        idx = random.randint(0, len(self.child)-1)
        return self.child[idx]._execute(tree)