# -*- coding: utf-8 -*

import sys
sys.path.append('..')
import BT



def ExecuteTree():
    blackBord = BT.BlackBoard()
    behaviorTree = BT.BehaviorTree()
    behaviorTree.root = BT.Sequence([
                            BT.DistanceToTargetShorterThan(1000, [0, 101], [0, 0]),
                            BT.MoveToPoint()
                        ])

    behaviorTree.execute( blackBord)



if __name__ == "__main__":
    load_obj = BT.XML2Tree()
    print(load_obj.LoadTree("../xml/test.xml"))
    #ExecuteTree()
