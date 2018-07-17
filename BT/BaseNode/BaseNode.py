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

    def _execute(self, traverse_tick):
        print("execute node", self.class_name)
        return self._tick(traverse_tick)



    def param_check(self, param, param_type):
        for param_name in param_type:
            if param_name not in param:
                print "%s param error: %s" %(self.class_name, param_name)
                return False

        return True


    def _tick(self, traverse_tick): 
        tree = traverse_tick.tree

        if (not tree.get_data('is_enter', self.id)):
            tree.set_data('is_enter', True, self.id)
            self.on_first_enter(traverse_tick)
            
        #traverse_tick.append_running_node(self)

        status = self.tick(traverse_tick)

        if (status != BT.RUNNING):
            tree.set_data('is_enter', False, self.id)
            #traverse_tick.pop_running_node(self)
            self.on_exit(traverse_tick)

        return status


    def tick(self,traverse_tick): pass
    def on_first_enter(self, traverse_tick): pass
    def on_exit(self, traverse_tick):pass
