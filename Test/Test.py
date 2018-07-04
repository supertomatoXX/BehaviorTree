# -*- coding: utf-8 -*
import sys
sys.path.append('..')

import BT


def ExecuteTree():
    blackBord = BT.BlackBoard()
    behaviorTree = BT.BehaviorTree()
    behaviorTree.root = BT.RepeatUntilFailure(BT.Succeed(), 5)


    

    behaviorTree2 = BT.BehaviorTree()
    behaviorTree2.root = BT.RepeatUntilFailure(BT.Succeed(), 15)

    behaviorTree.tick( None, blackBord)
    behaviorTree2.tick( None, blackBord)


if __name__ == "__main__":
    ExecuteTree()
