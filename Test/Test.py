# -*- coding: utf-8 -*

import sys
import time
sys.path.append('..')
import BT


def test_tick_count():
    xml_path = "../xml/test_tick_count.xml"
    load_obj = BT.XML2Tree()
    black_board = BT.BlackBoard()
    behavior_tree = load_obj.xml_2_tree(xml_path, black_board)


    while True:
        print("tick tick count")
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break

        time.sleep(1)

def test_tick_count_change():
    xml_path = "../xml/test_tick_count_change.xml"
    load_obj = BT.XML2Tree()
    black_board = BT.BlackBoard()
    behavior_tree = load_obj.xml_2_tree(xml_path, black_board)

    reset_data = False
    while True:
        print("tick tick count")
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            if not reset_data:
                print("reset tick count 5")
                behavior_tree.set_extra_param({"tick_count_change":5})
                reset_data = True
            else:
                break

        time.sleep(1)

def test_wait():
    xml_path = "../xml/test_wait.xml"
    load_obj = BT.XML2Tree()
    black_board = BT.BlackBoard()
    behavior_tree = load_obj.xml_2_tree(xml_path, black_board)


    while True:
        print("tick wait")
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break

        time.sleep(1)

def test_tree_scope_switch():
    xml_path = "../xml/test_tick_count.xml"
    load_obj = BT.XML2Tree()
    black_board = BT.BlackBoard()
    behavior_tree = load_obj.xml_2_tree(xml_path, black_board)

    data_id1 = black_board.gen_data(behavior_tree)
    data_id2 = black_board.gen_data(behavior_tree)
    

    
    while True:
        print(data_id1)
        behavior_tree.set_data_id(data_id1)
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break
        time.sleep(1)

        print(data_id2)
        behavior_tree.set_data_id(data_id2)
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break
        time.sleep(1)

def test_xml( path ):
    xml_path = path
    load_obj = BT.XML2Tree()
    black_board = BT.BlackBoard()
    behavior_tree = load_obj.xml_2_tree(xml_path, black_board)
    state = behavior_tree.execute( )
    return state



STR_2_TEST_FUNC = {
    "test_xml":test_xml,
    "test_tick_count":test_tick_count,
    "test_wait":test_wait,
    "test_tree_scope_switch":test_tree_scope_switch,
    "test_tick_count_change":test_tick_count_change,
}


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("please input xml file")
        exit(0)

    test_str = sys.argv[1]

    if test_str in STR_2_TEST_FUNC:
        if test_str == "test_xml":
            STR_2_TEST_FUNC[test_str](sys.argv[2])
        else:
            STR_2_TEST_FUNC[test_str]()
    
