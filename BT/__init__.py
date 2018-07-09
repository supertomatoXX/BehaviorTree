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
from BT.BaseNode.TraverseTick import TraverseTick
from BT.BaseNode.BlackBoard import BlackBoard
from BT.BaseNode.BehaviorTree import BehaviorTree

from BT.BaseNode.Composite import Composite
from BT.BaseNode.Decorator import Decorator
from BT.BaseNode.Action import Action
from BT.BaseNode.Condition import Condition


#Action相关,特定的行为
from BT.ActionNode.Failure import Failure
from BT.ActionNode.MoveToPoint import MoveToPoint

#Decorator相关, 限制性行为
from BT.DecoratorNode.Repeater import Repeater
from BT.DecoratorNode.RepeatUntilSuccess import RepeatUntilSuccess

#Compoite相关，一组子行为的组合，并根据所有子行为的返回状态进行决策
from BT.CompositeNode.Sequence import Sequence
from BT.CompositeNode.Selection import Selection



#Condition相关，条件判断结点
from BT.ConditionNode.DistanceToTargetShorterThan import DistanceToTargetShorterThan




#load xml
from BT.Load.XmlTool import XML2Tree