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
        if (not tree.get_data('is_enter', self.id)):
            tree.set_data('is_enter', True, self.id)
            self.on_first_enter(tree)


        status = self.tick(tree)

        if (status != BT.RUNNING):
            tree.set_data('is_enter', False, self.id)
            self.on_exit(tree)

        return status

    def set_param(self, k, v):
        #对象身上的初始属性直更新
        if hasattr(self, "param"):
            if self.param.has_key(k):
                setattr(self, k, v)
                #print("set default param", self.name, k, getattr(self, k))
                return

        #新增的属性需要记住，以但在后面清除
        if not hasattr(self, "extra_param"):
            self.extra_param = {}

        self.extra_param[k]=True
        setattr(self, k, v)
        #print("set extra_param", self.name, self.extra_param)


    #def del_param(self, k):
    #    if hasattr(self, k):
    #        #print("del default param1", self.name, k, getattr(self,k))
    #        delattr(self,k)
#
    #    if hasattr(self, "extra_param"):
    #        if self.extra_param.has_key(k):
    #            #print("del extra param", self.name, k)
    #            delattr(self,k)
    #            del self.extra_param[k]

    def set_param_by_dict( self, param_dict):
        for k in param_dict:
            self.set_param( k, param_dict[k]) 

    #恢复结点到初始状态
    def reset(self):
        #如果存在增外新增的属性，全部清除
        if hasattr(self, "extra_param"):
            for k in self.extra_param:
                #print("del extra param", self.name, k)
                delattr(self, k)
            del self.extra_param

        #恢复xml中配置的初始参数
        self.init_param()

        if hasattr(self, "child") and (self.child is not None):
            if not isinstance(self.child, list):
                self.child.reset()
            else:
                for child in self.child:
                    child.reset()


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



    def tick(self,tree): pass
    def on_first_enter(self, tree): pass
    def on_exit(self, tree):pass
    def init_param(self):pass