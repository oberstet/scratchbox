from foobar import Robot, talk
from foobar.interfaces import IRobot, IRobotRunner
from zope.interface.verify import verifyObject

class Foo:
    def talk(self, msg):
        print("foo: {}".format(msg))

foo = Foo()

robot1 = Robot()
robot1.talk(u"Hello, world!")

robot2 = Robot()
talk([robot1, robot2, foo], u"foo, bar!")

print(IRobot.providedBy(robot1))
print(IRobot.providedBy(foo))
print(verifyObject(IRobot, robot1))
print(verifyObject(IRobot, foo))
#print IRobotRunner.providedBy(talk)


# user docs for AB public API => Sphinx/RTD + handselected

# AB internal docs / dev intents => zope.interface

# WAMP based AP definition => A markdown based API definition tool



# change txaio to zope.interface
# pimp up the docs


# write up CB meta API in
