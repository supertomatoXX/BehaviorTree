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
    black_board = BT.BlackBoard()
    behavior_tree = load_obj.xml_2_tree(xml_path, black_board)

    data_id1 = black_board.gen_data()
    data_id2 = black_board.gen_data()
    
    #state = behavior_tree.execute( black_board )
    #behavior_tree.destory()

    
    while True:
        print(data_id1)
        behavior_tree.set_data_id(data_id1)
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break

        print(data_id2)
        behavior_tree.set_data_id(data_id2)
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break
