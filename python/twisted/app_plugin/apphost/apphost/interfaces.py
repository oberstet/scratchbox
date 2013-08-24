from zope.interface import Interface


class IApphostPlugin(Interface):
    """
    The Apphost plugin interface.
    """

    def hello():
        """
        Returns a plugin specific hello message.
        """
