# -*- coding: utf-8 -*

import sys
sys.path.append('..')
import BT



if __name__ == "__main__":
    load_obj = BT.XML2Tree()
    behaviorTree = load_obj.load_tree("../xml/test.xml")
    blackBoard = BT.BlackBoard()
    
    behaviorTree.execute( blackBoard )

    
    #ExecuteTree()
