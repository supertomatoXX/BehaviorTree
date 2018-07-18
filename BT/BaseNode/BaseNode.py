# -*- coding: utf-8 -*
import BT
import uuid

#__all__ = ['BaseNode']

class BaseNode(object):
    node_type = None
    node_name = None


    def __init__(self, param = None, param_type = None):
        if param:
            if param_type:
                if not self.param_check(param, param_type):
                    return 


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


    def tick(self,tree): pass
    def on_first_enter(self, tree): pass
    def on_exit(self, tree):pass
