# -*- coding: utf-8 -*
import BT

#__all__ = ['Action']


class Action(BT.BaseNode):
	node_type = BT.ACTION

	def __init__(self, param, param_type):
		super(Action, self).__init__( param, param_type)

