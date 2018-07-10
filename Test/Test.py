# -*- coding: utf-8 -*

import sys
sys.path.append('..')
import BT



def ExecuteTree():
    blackBord = BT.BlackBoard()
    behaviorTree = BT.BehaviorTree()
    behaviorTree.root = BT.Sequence([
                            BT.DistanceToTargetShorterThan({'distance':10000, 'x1':0, 'z1':0, 'x2':200, 'z2':300}),
                            BT.MoveToPoint({'x':0, 'y':0, 'z':0})
                        ])

    behaviorTree.execute( blackBord)



if __name__ == "__main__":
    load_obj = BT.XML2Tree()
    behaviorTree = load_obj.LoadTree("../xml/test.xml")
    blackBord = BT.BlackBoard()
    
    behaviorTree.execute( blackBord )

    
    #ExecuteTree()
