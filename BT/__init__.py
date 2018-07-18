# -*- coding: utf-8 -*
SUCCESS   = 1
FAILURE   = 2
RUNNING   = 3
ERROR     = 4

COMPOSITE = 'composite'
DECORATOR = 'decorator'
ACTION    = 'action'
CONDITION = 'condition'
ROOT = 'Root'



#基类相关
from BT.BaseNode.BaseNode import BaseNode
from BT.BaseNode.Root import Root
from BT.BaseNode.BlackBoard import BlackBoard
from BT.BaseNode.BehaviorTree import BehaviorTree

from BT.BaseNode.Composite import Composite
from BT.BaseNode.Decorator import Decorator
from BT.BaseNode.Action import Action
from BT.BaseNode.Condition import Condition

#Action相关,特定的行为
from BT.ActionNode.Failure import Failure
from BT.ActionNode.MoveToPoint import MoveToPoint
from BT.ActionNode.Wait import Wait

#Decorator相关, 限制性行为
from BT.DecoratorNode.TickCount import TickCount
from BT.DecoratorNode.TickCountChange import TickCountChange

#Compoite相关，一组子行为的组合，并根据所有子行为的返回状态进行决策
from BT.CompositeNode.Sequence import Sequence
from BT.CompositeNode.Selection import Selection



#Condition相关，条件判断结点
from BT.ConditionNode.DistanceToTargetShorterThan import DistanceToTargetShorterThan
from BT.ConditionNode.IfElse import IfElse




#load xml
from BT.Load.XmlTool import xml_tool