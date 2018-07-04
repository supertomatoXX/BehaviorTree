# -*- coding: utf-8 -*
SUCCESS   = 1
FAILURE   = 2
RUNNING   = 3
ERROR     = 4

COMPOSITE = 'composite'
DECORATOR = 'decorator'
ACTION    = 'action'
CONDITION = 'condition'


#基类相关
from BT.BaseNode.BaseNode import BaseNode
from BT.BaseNode.Tick import Tick
from BT.BaseNode.BlackBoard import BlackBoard
from BT.BaseNode.BehaviorTree import BehaviorTree

from BT.BaseNode.Composite import Composite
from BT.BaseNode.Decorator import Decorator
from BT.BaseNode.Action import Action
from BT.BaseNode.Condition import Condition


#Action相关
from BT.ActionNode.Succeed import Succeed
from BT.ActionNode.Failure import Failure
from BT.ActionNode.Running import Running
from BT.ActionNode.Error import Error
from BT.ActionNode.Wait import Wait


#Compoite相关
from BT.CompositeNode.Sequence import Sequence
from BT.CompositeNode.Priority import Priority
from BT.CompositeNode.MemPriority import MemPriority
from BT.CompositeNode.MemSequence import MemSequence


#Decorator相关
from BT.DecoratorNode.Inverter import Inverter
from BT.DecoratorNode.Limiter import Limiter
from BT.DecoratorNode.MaxTime import MaxTime
from BT.DecoratorNode.Repeater import Repeater
from BT.DecoratorNode.RepeatUntilFailure import RepeatUntilFailure
from BT.DecoratorNode.RepeatUntilSuccess import RepeatUntilSuccess

