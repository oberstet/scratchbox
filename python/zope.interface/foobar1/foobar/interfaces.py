from zope import interface

class IRobot(interface.Interface):
    """
    Robots implement this interface.
    """

    def talk(msg):
        """
        Make the robot speak the provided text.

        :param msg: The text to speak.
        :type msg: unicode
        """

class IRobotFactory(interface.Interface):
    """
    Create robots providing the IRobot interface.
    """

    def __call__():
        """
        Create a new robot.
        """

class IRobotRunner(interface.Interface):

    def __call__(robots, msg):
        """
        :param robots: The robots to let talk.
        :type robots: list of IRobot
        :param msg: The text to speak.
        :type msg: unicode
        """
