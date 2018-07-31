# -*- coding: utf-8 -*
import BT
import uuid

#__all__ = ['BaseNode']

class BaseNode(object):
    node_type = None

    def __init__(self, param = None, param_type = None):
        if param and param_type:
            if self.param_check(param, param_type):
                #保留xml中的初始参数，以用于恢复参数
                self.param_type = param_type
                self.param = param
            else:
                return None 


        if "Name" in param:
            self.name = param["Name"]

        self.id = str(uuid.uuid1())


    @property
    def class_name(self):
        return self.__class__.__name__

    def _execute(self, tree):
        print("execute node", self.class_name)
        return self._tick(tree)



    def param_check(self, param, param_type):
        for param_name in param_type:
            if param_name not in param:
                print "%s param error: %s" %(self.class_name, param_name)
                return False
        return True


    def _tick(self, tree): 
        if (not tree.get_data('is_first_enter', self.id)):
            tree.set_data('is_first_enter', True, self.id)
            self.on_first_enter(tree)

        if (not tree.get_data('is_enter', self.id)):
            tree.set_data('is_enter', True, self.id)
            self.on_enter(tree)
            


        status = self.tick(tree)

        if (status != BT.RUNNING):
            tree.set_data('is_enter', False, self.id)
            self.on_exit(tree)

        return status



    def set_param_by_dict( self, tree, param_dict, cur_path=""):
        for k in param_dict:
            if k == "extra_param":
                extra_param = param_dict["extra_param"]
                for k in extra_param:
                    print("set node data", k, extra_param[k], self.name, self)
                    tree.set_data(k, extra_param[k], self.id)
                    print("set node data11111",tree.get_data("count", self.id), self)
                continue

            child = self.get_child_by_name(k)
            if child is not None:
                child.set_param_by_dict(tree, param_dict[k], ("%s.%s" %(cur_path, k)))
            else:
                path = "%s.%s" %(cur_path, k)
                print(("set extra param by dict error: key %s error" %path))


    #恢复结点到初始状态
    def reset(self, tree):
        tree.del_node_data(self.id)

        if hasattr(self, "child") and (self.child is not None):
            if not isinstance(self.child, list):
                self.child.reset(tree)
            else:
                for child in self.child:
                    child.reset(tree)

    def get_child_by_name( self, child_name):
        if not hasattr( self, "child"):
            return None

        if hasattr( self, "child_map"):
            return self.child_map.get(child_name)

        self.child_map = {}
        if not isinstance(self.child, list):
            self.child_map[self.child.name] = self.child
        else:
            for child in self.child:
                self.child_map[child.name] = child

        return self.child_map.get(child_name)

    def get_child_by_path( self, node_path ):
        node_path = node_path.split(".")
        node = self

        for i in xrange(len(node_path)):
            node_name = node_path[i]
            node = node.get_child_by_name(node_name)

            if not node:
                print("get node by path error:", node_path[:i+1])
                node = None
                break

        return node




    def on_first_enter(self, tree):
        self.init_param(tree)

    def dump(self):
        print("node:", self.name)
        from pprint import pprint
        pprint (vars(self))
        print("\n")

        if getattr(self, "child", None):
            if not isinstance(self.child, list):
                self.child.dump()
            else:
                for child in self.child:
                    child.dump()

    def tick(self,tree): pass
    def on_enter(self, tree): pass
    def on_exit(self, tree):pass
    def init_param(self, tree):pass