# -*- coding: utf-8 -*

import sys
sys.path.append('..')
import BT


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("please input xml file")
        exit(0)

    xml_path = sys.argv[1]
    load_obj = BT.XML2Tree()
    behaviorTree = load_obj.load_tree(xml_path)
    blackBoard = BT.BlackBoard()
    
    while True:
        state = behaviorTree.execute( blackBoard )
        if state != BT.RUNNING:
            break

    
    #ExecuteTree()
