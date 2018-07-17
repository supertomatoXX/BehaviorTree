# -*- coding: utf-8 -*
import BT
import os

try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET


#缓存 load param check  status  动作持续时长带过程

#__all__ = ['XMLTool']

NAME_2_NODE_CLASS = { 
    "MoveToPoint": BT.MoveToPoint, 
    "Failure": BT.Failure, 
    "Wait": BT.Wait,

    "Behavior": BT.BehaviorTree, 
    "Root":BT.Root, 

    "Sequence": BT.Sequence, 
    "Selection": BT.Selection, 

    "DistanceToTargetShorterThan": BT.DistanceToTargetShorterThan,


    "TickCount": BT.TickCount,
    "TickCountChange": BT.TickCountChange,
}

LOADED = {}

class XMLTool(object):

    def __init__(self, coding="UTF-8"):
        self._coding = coding


    def _parse_node_obj(self, node):
        tree = None

        #getchildren方法按照文档顺序返回所有子标签,为保证顺序，子结点放到list中
        for child in node.getchildren():
            cattr = child.attrib
            ctext = child.text.strip().encode(self._coding) if child.text is not None else ''
            ctree = self._parse_node_obj(child)


            child_obj = self._make_object( cattr, ctree)

            if tree == None: 
                tree = child_obj 
                continue
            
            if not isinstance(tree, list):
                tree = [tree]

            tree.append(child_obj)
        
        return  tree




    def _make_object(self, attr, childrens = None ):
        #print("make obj", childrens, attr['Name'])
        return NAME_2_NODE_CLASS[attr["Type"]]( attr, childrens)


    def create_tree( self, path ):
        root = self.load_tree(path)
        return BT.BehaviorTree(root)




    def load_tree( self, path ):
        path = os.path.abspath(path) 

        root = self.get_tree(path)
        if root:
            return root


        try:
            root = self.load_tree_by_iter(path)
        except IOError:
            print("load_tree_by_iter Error: 没有找到文件或读取文件失败", path)

        if root is not None:
            self.cache_tree(path, root)
            return root


        try:
            with open(path,'r') as f:
                xml_str = f.read()
        except IOError:
            print("load_tree_by_str Error: 没有找到文件或读取文件失败", path)
            

        if not xml_str:
            print("load xml data error:", path)
            return

        root = self.load_tree_by_str(xml_str)
        self.cache_tree(path, tree)
        return root



    def load_tree_by_str( self, xml_str):
        element_tree = ET.fromstring(xml_str)
        root = self._parse_node_obj(element_tree)
        return root

    def load_tree_by_iter( self, path ):
        element_stack = []
        obj_stack = []

        for event, elem in ET.iterparse(path, events=("start", "end")):
            if event == "start":
                if "Type" in elem.attrib:
                    element_stack.append(elem.attrib)

            if event == "end":
                if "Type" in elem.attrib:
                    attr = element_stack.pop()
                    element_stack_len = len(element_stack)

                    if len(obj_stack) == 0:
                        obj_stack.append( {"obj":self._make_object(attr), "element_stack_len":element_stack_len} )
                        continue

                    top_obj = obj_stack[len(obj_stack)-1]
                    if top_obj["element_stack_len"] <= element_stack_len:
                        obj_stack.append( {"obj":self._make_object(attr), "element_stack_len":element_stack_len} )
                        continue

                    child = None
                    for i in xrange(len(obj_stack), 0, -1):
                        obj = obj_stack[i-1]
                        if obj["element_stack_len"] > element_stack_len:
                            obj = obj_stack.pop()

                            if child is None:
                                child = obj
                                continue

                            if not isinstance(child["obj"], list):
                                child["obj"] = [child["obj"]]

                            child["obj"].append(obj["obj"])

                        else:
                            break

                    if isinstance(child["obj"], list):
                        child["obj"].reverse()
                    obj_stack.append( {"obj":self._make_object( attr, child["obj"]), "element_stack_len":element_stack_len} )
        
        if len(obj_stack) > 1:
            print("load tree from xml error", path)
            return None

        return obj_stack[0]["obj"]
            


    def get_tree(self, path):
        return LOADED.get(path)
        
    def cache_tree( self, path, tree):
        LOADED[path] = tree

    def clean_tree( self, path):
        del LOADED[path]

xml_tool = XMLTool()