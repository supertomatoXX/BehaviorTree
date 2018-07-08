# -*- coding: utf-8 -*
import BT


try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET


__all__ = ['XML2Tree']




NAME_2_NODE_DICT = {
    "Behavior": BT.BehaviorTree,

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


    def _parse_node(self, node):
        tree = {}

        for child in node.getchildren():
            ctag = child.tag
            cattr = child.attrib
            ctext = child.text.strip().encode(self._coding) if child.text is not None else ''
            ctree = self._parse_node(child)

            if not ctree:
                cdict = self._make_dict(ctag, ctext, cattr)
            else:
                cdict = self._make_dict(ctag, ctree, cattr)

            if ctag not in tree: 
                tree.update(cdict)
                continue


            atag = '@' + ctag
            atree = tree[ctag]
            if not isinstance(atree, list):
                if not isinstance(atree, dict):
                    atree = {}

                if atag in tree:
                    atree['#'+ctag] = tree[atag]
                    del tree[atag]

                tree[ctag] = [atree] 

            if cattr:
                ctree['#'+ctag] = cattr
            tree[ctag].append(ctree)
        return  tree




    def _make_dict(self, tag, value, attr=None):
        ret = {tag: value}
        if attr:
            atag = '@' + tag

            aattr = {}
            for k, v in attr.items():
                aattr[k] = v

            ret[atag] = aattr

            del atag
            del aattr

        return ret


    def _xml2dict(self, xml_data):
        element_tree = ET.fromstring(xml_data)
        behavior_tree = NAME_2_NODE_DICT[element_tree.tag]()
        behavior_tree.root = self._make_dict( element_tree.tag, self._parse_node(element_tree), element_tree.attrib)
        return behavior_tree.root

    def _parse_node(self, node):
        tree = ""

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

        if tree:
            tree = "[%s]" %(tree)
        return  tree




    def _make_dict(self, value, attr=None):
        dict_str = "%s(%s,%s)" %(attr['Name'], value, str(attr))
        return ret



    def LoadTree( self, path):
        #path = "../xml/basic_attack_medic.xml"
        xml_data = open(path).read()
        bt_tree = self._xml2dict(xml_data)


        self._dict2tree(bt_tree['Behavior']['Node'])
#        print("111111111", bt_tree)
#        bt_str = str(bt_tree)
#        print("222222222", bt_str)
#        
#        test_tree = None
#        exec( "test_tree = " + bt_str)
#        print("33333333", test_tree)
        
        print(str(bt_tree))
        return bt_tree

