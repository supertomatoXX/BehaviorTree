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
        status = behavior_tree.execute( )
        time.sleep(1)

def test_tick_count_change():
    xml_path = "../xml/test_tick_count_change.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    test_dict = {
                    "TickCountChange":{
                                "extra_param":{"count":5},
                                },
        }

    reset_data = False
    while True:
        print("tick tick count")
        status = behavior_tree.execute( )
        if status != BT.RUNNING:
            if not reset_data:
                print("set tick count 5")
                behavior_tree.set_param_by_path(test_dict, "Root.TickCountChange")
                reset_data = True
            else:
                break

        time.sleep(1)

    print("reset node")
    behavior_tree.reset_node_by_path( "Root.TickCountChange")
    while True:
        print("tick tick count")
        status = behavior_tree.execute( )
        if status != BT.RUNNING:
            break
        time.sleep(1)

def test_wait():
    xml_path = "../xml/test_wait.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)


    while True:
        print("tick wait")
        status = behavior_tree.execute( )
        if status != BT.RUNNING:
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
        status = behavior_tree1.execute( )
        if status != BT.RUNNING:
            break
        time.sleep(1)

        status = behavior_tree2.execute( )
        if status != BT.RUNNING:
            break
        time.sleep(1)


    behavior_tree1.destory()
    behavior_tree2.destory()




def test_xml( path ):
    xml_path = path
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    status = behavior_tree.execute( )
    print("behavior status", status)
    return status

def test_begin_node( ):
    xml_path = "../xml/test.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    print("execute from root")
    status = behavior_tree.execute( )
    print("execute from begin node")
    behavior_tree.set_begin_node_by_path("Root.Selection.TickCount.Sequence.DistanceToTargetShorterThan")
    status = behavior_tree.execute( )
    behavior_tree.del_begin_node()
    print("execute from root")
    status = behavior_tree.execute( )
    return status


def test_extra_param( ):
    test_dict = {
        "Root":{ 
                "extra_param":{"test":2},
                "TickCountChange":{
                            "extra_param":{"count":5},
                            },
                }
    }

    

    xml_path = "../xml/test_tick_count_change.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)

    reset_data = False
    while True:
        print("tick tick count")
        status = behavior_tree.execute( )
        if status != BT.RUNNING:
            if not reset_data:
                print("reset tick count 5")
                behavior_tree.set_param( test_dict )
                reset_data = True
            else:
                break

        time.sleep(1)

    print("del extra param by dict")
    behavior_tree.reset()
    while True:
        print("tick tick count")
        status = behavior_tree.execute( )
        if status != BT.RUNNING:
                break
    
        time.sleep(1)


def test_extra_param2( ):
    test_dict = {
        "Root":{ 
                "extra_param":{"test1":1},                      #extra_param key为对应结点的参数

                "Selection":{                               #其它key为其它结点的param dict
                                "extra_param":{"test2":2},

                                    "TickCount":{
                                            "extra_param":{"count":5},

                                            "Sequence":{
                                                "extra_param":{
                                                }
                                            },
                                    },

                                "Sequence":{
                                            "extra_param":{"test4":7},

                                            "Wait":{
                                                "extra_param":{"end_time":8},
                                                },

                                            "MoveToPoint":{
                                                "extra_param":{"x":9}
                                                }
                                            },

                            },
                }
    }

    

    xml_path = "../xml/test.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    behavior_tree.set_param( test_dict )
    #behavior_tree.dump()
    #print("=================================================")
    #behavior_tree.reset()
    #behavior_tree.dump()





def test_tree_composite( ):
    xml_path = "../xml/test_tree_composite.xml"
    behavior_tree = BT.xml_tool.create_tree(xml_path)
    behavior_tree.execute()

    test_dict = {
        "Root":{ 
                "extra_param":{"test1":1},                      

                "IfElse":{                               
                                "extra_param":{"test2":2},

                                "BehaviorTree1":{
                                            "extra_param":{"count":5},

                                            "Root":{
                                                        "Sequence":{
                                                            "MoveToPoint":{
                                                                "extra_param":{"x":500}
                                                            }
                                                        }
                                            },
                                    },

                                "BehaviorTree2":{
                                            "extra_param":{"test4":7},

                                            "Root":{
                                                        "Selection":{
                                                            "MoveToPoint":{
                                                                "extra_param":{"x":888}
                                                            }
                                                        }
                                            },
                                    }

                            },
                }
    }
    print("set param.....")
    behavior_tree.set_param( test_dict )
    behavior_tree.execute()






STR_2_TEST_FUNC = {
    "test_xml":test_xml,
    "test_tick_count":test_tick_count,
    "test_wait":test_wait,
    "test_tree_scope_switch":test_tree_scope_switch,
    "test_tick_count_change":test_tick_count_change,
    "test_begin_node":test_begin_node,
    "test_extra_param":test_extra_param,
    "test_tree_composite":test_tree_composite,
    "test_extra_param":test_extra_param,
    "test_extra_param2":test_extra_param2
}

import itertools

if __name__ == "__main__":
    test_str = sys.argv[1]

    if test_str in STR_2_TEST_FUNC:
        if test_str == "test_xml":
            STR_2_TEST_FUNC[test_str](sys.argv[2])
        else:
            STR_2_TEST_FUNC[test_str]()
    
