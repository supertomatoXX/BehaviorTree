# -*- coding: utf-8 -*
import BT

__all__ = ['Inverter']

class Inverter(BT.Decorator):
    def tick(self, tick):
        if not self.child:
            return BT.ERROR

        status = self.child._execute(tick)

        if status == BT.SUCCESS:
            status = BT.FAILURE
        elif status == BT.FAILURE:
            status = BT.SUCCESS

        return status
        
