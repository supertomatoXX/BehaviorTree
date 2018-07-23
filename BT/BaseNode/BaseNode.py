# -*- coding: utf-8 -*
import BT
import uuid

#__all__ = ['BaseNode']

class BaseNode(object):
    node_type = None
    node_name = None


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
                self.k = v
                return

        #新增的属性需要记住，以但在后面清除
        if not hasattr(self, "extra_param"):
            self.extra_param = {}

        self.extra_param[k]=True
        self.k = v

    #恢复结点到初始状态
    def reset(self):
        #如果存在增外新增的属性，全部清除
        if hasattr(self, "extra_param"):
            for k in self.extra_param:
                del self[l]
            del self.extra_param

        #恢复xml中配置的初始参数
        self.init_param()

    def tick(self,tree): pass
    def on_first_enter(self, tree): pass
    def on_exit(self, tree):pass
    def init_param(self):pass