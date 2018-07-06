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

        #Save childrens
        for child in node.getchildren():
            ctag = child.tag
            print("parse chilld 1111", child.text)
            cattr = child.attrib
            ctext = child.text.strip().encode(self._coding) if child.text is not None else ''
            print("parse chilld 222", child.text)
            ctree = self._parse_node(child)


            if not ctree:
                cdict = self._make_dict(ctag, ctext, cattr)
            else:
                cdict = self._make_dict(ctag, ctree, cattr)

            if ctag not in tree: # First time found
                tree.update(cdict)
                print("update dict 2222222", cdict)
                continue

            atag = '@' + ctag
            atree = tree[ctag]
            if not isinstance(atree, list):
                if not isinstance(atree, dict):
                    atree = {}

                if atag in tree:
                    atree['#'+ctag] = tree[atag]
                    del tree[atag]

                tree[ctag] = [atree] # Multi entries, change to list

            if cattr:
                ctree['#'+ctag] = cattr

            
            tree[ctag].append(ctree)

        print("retrun3333333", tree)
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


    def parse(self, path):
        data = open(path).read()
        EL = ET.fromstring(data)
        print( EL.tag, EL.attrib)
        self._make_dict(EL.tag, self._parse_node(EL), EL.attrib)


    def parse_node(self, node):
        tree = {}
        print("parse node...", node)

        for child in node.getchildren():
            print("new child", child.tag, child.attrib, child.text)
            ctag = child.tag
            cattr = child.attrib
            ctree = self.parse_node(child)

            if not ctree:
                print("1111111")
                cdict = self.make_tree(ctag, "", cattr)
            else:
                print("222222")
                cdict = self.make_tree(ctag, ctree, cattr)

            if ctag not in tree: # First time found
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

                tree[ctag] = [atree] # Multi entries, change to list

            if cattr:
                ctree['#'+ctag] = cattr


            tree[ctag].append(ctree)

        return  tree

    def make_tree(self, tag, value, attr=None):
        ret = {tag: value}
        if attr:
            atag = '@' + tag

            aattr = {}
            for k, v in attr.items():
                aattr[k] = v

            ret[atag] = aattr

            del atag
            del aattr

        #print("1111", ret)
        return ret


    def LoadTree( self, path):
        xml_data = open(path).read()
        element_tree = ET.fromstring(xml_data)

        behavior_tree = NAME_2_NODE_DICT[element_tree.tag]()
        behavior_tree.root = self._make_dict( element_tree.tag, self._parse_node(element_tree), element_tree.attrib)

        return behavior_tree

'''
def fix_attribs(elem):
    dict_ = {}
    for key in elem.attrib:
        dict_.update({key: attr(elem, key)})
    return dict_

def build_dict(elem):
    if elem is not None:
        dict_ = {}


        for subelem in elem:
            print subelem.tag
            if subelem.tag in dict_:
                if not isinstance(dict_[subelem.tag], list):
                    dict_[subelem.tag] = [dict_[subelem.tag]]
                dict_[subelem.tag].append(build_dict(subelem))
            else:
                dict_.update({subelem.tag: build_dict(subelem)})
            if subelem.text and subelem.text.strip():
                dict_.update({subelem.tag: {"_text": subelem.text}})
        dict_.update(fix_attribs(elem))
        return dict_
    else:
        return fix_attribs(elem)
'''