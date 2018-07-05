# -*- coding: utf-8 -*
import sys
sys.path.append('..')

import BT
'''
    root = Priority(child_nodes =[
        Sequence(child_nodes = [
            BatteryCheck(), 
            FindHome(), 
            GoHome(), 
            Dock()
        ]),
        Selection(child_nodes = [
            Sequence(child_nodes = [
                Spot(),
                Timer20(child_node = CleanSpot()),
                DoneSpot()
            ]),
            Sequence(child_nodes = [
                General(),
                Sequence(child_nodes = [
                    UntilFail(child_node = 
                        Sequence(child_nodes = [
                            NotOperator(child_node = BatteryCheck()),
                            Selection(child_nodes = [
                                Sequence(child_nodes = [
                                    DustySpot(),
                                    Timer35(child_node = CleanSpot())
                                ]),
                                Clean()
                            ])
                        ])
                    ),
                    DoneGeneral()
                ])
            ])
        ]),
        DoNothing()
    ])
'''

def ExecuteTree():
    blackBord = BT.BlackBoard()
    behaviorTree = BT.BehaviorTree()
    behaviorTree.root = BT.Sequence([
                            BT.DistanceToTargetShorterThan(1000, [0, 101], [0, 0]),
                            BT.MoveToPoint()
                        ])

    behaviorTree.execute( blackBord)



if __name__ == "__main__":
    ExecuteTree()
