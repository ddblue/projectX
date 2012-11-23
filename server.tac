from twisted.application import internet
from twisted.application import service
from nevow import appserver
import rootcfg

application = service.Application('RootTemplate')
site = appserver.NevowSite(rootcfg.RootPage())
webServer = internet.TCPServer(8080, site)
webServer.setServiceParent(application)
