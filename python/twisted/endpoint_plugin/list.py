## verify that Autobahn Twisted endpoints have been installed
try:
   from twisted.internet.interfaces import IStreamServerEndpointStringParser
   from twisted.internet.interfaces import IStreamClientEndpointStringParser

   has_server_endpoint = False
   for plugin in getPlugins(IStreamServerEndpointStringParser):
      if plugin.prefix == "autobahn":
         has_server_endpoint = True
         break

   if has_server_endpoint:
      log.info("Autobahn Twisted stream server endpoint successfully installed")
   else:
      log.warn("Autobahn Twisted stream server endpoint installation seems to have failed")

   has_client_endpoint = False
   for plugin in getPlugins(IStreamClientEndpointStringParser):
      if plugin.prefix == "autobahn":
         has_client_endpoint = True
         break

   if has_client_endpoint:
      log.info("Autobahn Twisted stream client endpoint successfully installed")
   else:
      log.warn("Autobahn Twisted stream client endpoint installation seems to have failed")

except:
   log.warn("Autobahn Twisted endpoint installation could not be verified")
