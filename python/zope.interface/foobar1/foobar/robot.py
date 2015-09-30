from __future__ import absolute_import
from zope import interface

from foobar.interfaces import IRobot, IRobotFactory, IRobotRunner


class Robot(object):

    interface.implements(IRobot)
    interface.classProvides(IRobotFactory)

    def __init__(self):
        pass

    def talk(self, msg):
        print("robot: {}".format(msg))




def talk(robots, msg):
#    interface.directlyProvides(IRobotRunner)

    for robot in robots:
        print(IRobot.providedBy(robot))
        robot.talk(msg)

interface.directlyProvides(talk, IRobotRunner)
