# -*- coding: utf-8 -*

import sys
import time
sys.path.append('..')
import BT
import uuid


def test_tick_count():
    xml_path = "../xml/test_tick_count.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)


    while True:
        print("tick tick count")
        state = behavior_tree.execute( )
        time.sleep(1)

def test_tick_count_change():
    xml_path = "../xml/test_tick_count_change.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)

    reset_data = False
    while True:
        print("tick tick count")
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            if not reset_data:
                print("reset tick count 5")
                behavior_tree.set_node_extra_param_by_path({"tick_count_change":5}, ["Root", "TickCountChange"])
                reset_data = True
            else:
                break

        time.sleep(1)

def test_wait():
    xml_path = "../xml/test_wait.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)


    while True:
        print("tick wait")
        state = behavior_tree.execute( )
        if state != BT.RUNNING:
            break

        time.sleep(1)

    #print("cur datas1", behavior_tree.black_board.data )
    behavior_tree.destory()
    #print("cur datas2", behavior_tree.black_board.data )




def test_tree_scope_switch():
    xml_path = "../xml/test_tick_count.xml"
    xml_tool = BT.xml_tool
    behavior_tree1 = xml_tool.create_tree(xml_path)
    behavior_tree2 = xml_tool.create_tree(xml_path)
    xml_tool.clean_tree(xml_path)
    behavior_tree2 = xml_tool.create_tree(xml_path)
    print("behavior_tree1:", behavior_tree1,  behavior_tree1.root)
    print("behavior_tree1:", behavior_tree2,  behavior_tree1.root)

    while True:
        state = behavior_tree1.execute( )
        if state != BT.RUNNING:
            break
        time.sleep(1)

        state = behavior_tree2.execute( )
        if state != BT.RUNNING:
            break
        time.sleep(1)


    behavior_tree1.destory()
    behavior_tree2.destory()




def test_xml( path ):
    xml_path = path
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    state = behavior_tree.execute( )
    return state

def test_begin_node( ):
    xml_path = "../xml/test.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    print("execute from root")
    state = behavior_tree.execute( )
    print("execute from begin node")
    behavior_tree.set_begin_node_by_path("Root,Selection,TickCount,Sequence,DistanceToTargetShorterThan")
    state = behavior_tree.execute( )
    behavior_tree.del_begin_node()
    print("execute from root")
    state = behavior_tree.execute( )
    return state


STR_2_TEST_FUNC = {
    "test_xml":test_xml,
    "test_tick_count":test_tick_count,
    "test_wait":test_wait,
    "test_tree_scope_switch":test_tree_scope_switch,
    "test_tick_count_change":test_tick_count_change,
    "test_begin_node":test_begin_node,
}

import itertools

if __name__ == "__main__":
    test_str = sys.argv[1]

    if test_str in STR_2_TEST_FUNC:
        if test_str == "test_xml":
            STR_2_TEST_FUNC[test_str](sys.argv[2])
        else:
            STR_2_TEST_FUNC[test_str]()
    
