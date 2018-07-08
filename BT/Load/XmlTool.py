# -*- coding: utf-8 -*
import BT


try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET


__all__ = ['XML2Tree']




NAME_2_NODE_DICT = {
    "Behavior": BT.BehaviorTree,

    "Root":BT.Root,

    "MoveToPoint": BT.MoveToPoint,

    "Inverter": BT.Inverter,
    "Limiter": BT.Limiter,
    "MaxTime": BT.MaxTime,
    "Repeater": BT.Repeater,
    "RepeatUntilFailure": BT.RepeatUntilFailure,
    "RepeatUntilSuccess": BT.RepeatUntilSuccess,


    "Sequence": BT.Sequence,
    "Priority": BT.Priority,
    "MemPriority": BT.MemPriority,
    "MemSequence": BT.MemSequence,


    
    "DistanceToTargetShorterThan": BT.DistanceToTargetShorterThan
}

class XML2Tree(object):

    def __init__(self, coding='UTF-8'):
        self._coding = coding



    def _xml2dict(self, xml_data):
        element_tree = ET.fromstring(xml_data)
        behavior_tree = NAME_2_NODE_DICT[element_tree.tag]()
        tree_str = self._parse_node(element_tree)
        print("11111111", tree_str)
        exec( "behavior_tree.root = " + tree_str)
        return behavior_tree

    def _parse_node(self, node):
        tree = ""
        to_list = False
        for child in node.getchildren():
            ctag = child.tag
            cattr = child.attrib
            ctext = child.text.strip().encode(self._coding) if child.text is not None else ''
            ctree = self._parse_node(child)


            cdict = self._make_dict(ctree, cattr)

            if tree == "": 
                tree = cdict 
                continue
            

            tree = "%s,%s" %(tree, cdict)
            to_list = True
                


        if to_list:
            tree = "[%s]" %(tree)

        #if tree and to_list:
        #    tree = "[%s]" %(tree)
        #    to_list = False
        return  tree




    def _make_dict(self, value, attr=None):
        dict_str = value
        if attr:
            dict_str = "BT.%s(%s)" %(attr['Name'], str(attr))
            if value:
                dict_str = "BT.%s(%s,%s)" %(attr['Name'], value, str(attr))

        return dict_str



    def LoadTree( self, path):
        #path = "../xml/basic_attack_medic.xml"
        xml_data = open(path).read()
        bt_tree = self._xml2dict(xml_data)
        return bt_tree

