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
    behavior_tree = load_obj.load_tree(xml_path)
    black_board = BT.BlackBoard()
    
    #state = behavior_tree.execute( black_board )
    #behavior_tree.destory()

    
    while True:
        state = behavior_tree.execute( black_board )
        if state != BT.RUNNING:
            break
    
