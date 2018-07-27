# -*- coding: utf-8 -*
import os
import platform
import glob
try:
    import xml.etree.ElementTree as ET
except:
    import cElementTree as ET

import BT

NAME_2_NODE_CLASS = { 
    "MoveToPoint": BT.MoveToPoint, 
    "Failure": BT.Failure, 
    "Wait": BT.Wait,

    "Behavior": BT.BehaviorTree, 
    "Root":BT.Root, 

    "Sequence": BT.Sequence, 
    "Selection": BT.Selection, 
    "Parallel": BT.Parallel,
    "Probability": BT.Probability,

    "DistanceToTargetShorterThan": BT.DistanceToTargetShorterThan,
    "IfElse": BT.IfElse,


    "TickCount": BT.TickCount,
    "TickCountChange": BT.TickCountChange,

    "SubTree": lambda *args: BT.SubTree(xml_tool.load_tree(args[0]["path"]), args[0])


}

LOADED = {}

class XMLTool(object):


    def _parse_node_obj(self, node):
        tree = None

        #getchildren方法按照文档顺序返回所有子标签,为保证顺序，子结点放到list中
        for child in node.getchildren():
            cattr = child.attrib
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
        #if attr["Type"] == "BehaviorTree":
        #    print("load sub tree")
        #    return self.load_tree( attr["path"])

        return NAME_2_NODE_CLASS[attr["Type"]]( attr, childrens)


    def create_tree( self, path ):
        root = self.load_tree(path)
        return BT.BehaviorTree(root)




    def load_tree( self, path ):
        path = os.path.abspath(path) 
        path = os.path.normcase(path)

        #f not(os.path.exists(path)):
        #   print("load tree file error:%s, cannot get file" %path)
        #   return None

        #在windows平台下要使用glob做路径大小写的判断
        #f platform.system() == "Windows":
        #   #构建glob匹配路径
        #   #path = E:\\BehaviorTreeNew\\XML\\Test.xml
        #   #glob_path = E:\\BehaviorTreeNe[w]\\XM[L]\\Test.xm[l]
        #   #print("the abspath", path)
        #   path_pattern = path.split("\\")
        #   glob_path = path_pattern[0]
        #   for i in range(1, len(path_pattern)):
        #       pattern_str = path_pattern[i]
        #       glob_path = "%s\\%s[%s]" % (glob_path, pattern_str[:-1], pattern_str[-1])

        #   
        #   #使用glob匹配出真实的文件路径
        #   glob_path = glob.glob(glob_path)[0]
        #   #print("the glob path", glob_path)
        #   if path != glob_path:
        #       print("load tree file error:%s, maybe path case insensitive" %path)
        #       return None


        root = self.get_tree(path)
        if root:
            return root


        try:
            root = self.load_tree_by_iter(path)
        except Exception,ex:
            print("load_tree_by_iter Error: %s %s", Exception,ex)

        if root is not None:
            self.cache_tree(path, root)
            return root



        try:
            with open(path,'r') as f:
                xml_str = f.read()
        except Exception,ex:
            print("load_tree_by_str Error: %s %s", Exception,ex)
            

        if not xml_str:
            print("load xml data error:", path)
            return

        root = self.load_tree_by_str(xml_str)
        self.cache_tree(path, root)
        return root



    def load_tree_by_str( self, xml_str):
        element_tree = ET.fromstring(xml_str)
        root = self._parse_node_obj(element_tree)
        return root

    def load_tree_by_iter( self, path ):
        #element栈，每个栈元素的在的栈深度，等于xml树中的深度
        element_stack = []              
        #obj栈，在构建结点时使用
        obj_stack = []

        for event, elem in ET.iterparse(path, events=("start", "end")):
            if event == "start":
                if "Type" in elem.attrib:
                    element_stack.append(elem.attrib)

            if event == "end":
                if "Type" in elem.attrib:
                    attr = element_stack.pop()
                    element_stack_len = len(element_stack)

                    #首个构建的对象
                    if len(obj_stack) == 0:
                        obj_stack.append( {"obj":self._make_object(attr), "element_stack_len":element_stack_len} )
                        continue

                    #同级结点，或是更深的结点，进接入栈
                    top_obj = obj_stack[len(obj_stack)-1]
                    if top_obj["element_stack_len"] <= element_stack_len:
                        obj_stack.append( {"obj":self._make_object(attr), "element_stack_len":element_stack_len} )
                        continue

                    #非叶子结点，先弹出所有子结点，再进行构建
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
        path = os.path.abspath(path) 
        del LOADED[path]

xml_tool = XMLTool()

