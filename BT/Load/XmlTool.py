# -*- coding: utf-8 -*
import BT
import os

try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET


#缓存 load param check  status  动作持续时长带过程

#__all__ = ['XML2Tree']

NAME_2_NODE_CLASS = { 
    "MoveToPoint": BT.MoveToPoint, 
    "Failure": BT.Failure, 
    "Wait": BT.Wait,

    "Behavior": BT.BehaviorTree, 
    "Root":BT.Root, 

    "Sequence": BT.Sequence, 
    "Selection": BT.Selection, 

    "DistanceToTargetShorterThan": BT.DistanceToTargetShorterThan,

    "Repeater": BT.Repeater,  
    "RepeatUntilSuccess": BT.RepeatUntilSuccess, 
    "TickCount": BT.TickCount,
    "TickCountChange": BT.TickCountChange,
}

LOADED = {}

class XML2Tree(object):

    def __init__(self, coding='UTF-8'):
        self._coding = coding


#缓存 load param check  status  动作持续时长带过程




    def _parse_node_obj(self, node):
        tree = None

        #getchildren方法按照文档顺序返回所有子标签,为保证顺序，子结点放到list中
        for child in node.getchildren():
            cattr = child.attrib
            ctext = child.text.strip().encode(self._coding) if child.text is not None else ''
            ctree = self._parse_node_obj(child)


            child_obj = self._make_object(ctree, cattr)

            if tree == None: 
                tree = child_obj 
                continue
            
            if not isinstance(tree, list):
                tree = [tree]

            tree.append(child_obj)
        
        return  tree




    def _make_object(self, childrens, attr ):
        #print("make obj", attr['Name'])
        if childrens:
            return NAME_2_NODE_CLASS[attr['Name']](childrens, attr)

        return NAME_2_NODE_CLASS[attr['Name']]( attr)

    def _xml2tree(self, xml_data):
        element_tree = ET.fromstring(xml_data)
        behavior_tree = BT.BehaviorTree()
        behavior_tree.root = self._parse_node_obj(element_tree)
        return behavior_tree


    def load_tree( self, path):
        path = os.path.abspath(path)
        tree = None
        if path in LOADED:
            print("1111111111111111")
            tree = LOADED[path]
        else:
            print("2222222222222")
            try:
                fh = open(path)
                xml_data = fh.read()
            except IOError:
                print("Error: 没有找到文件或读取文件失败")
            else:
                fh.close()
                

            if not xml_data:
                print("load xml data error:", path)
                return

            tree = self._xml2tree(xml_data)
            LOADED[path] = tree
        return tree


    def load_tree_by_iter( self, path ):
        element_stack = []
        tree = None
        tree_dict = {}
        last_len = 0

        for event, elem in ET.iterparse(path, events=("start", "end")):
            if event == 'end':
                if tree is None:
                    tree = elem


