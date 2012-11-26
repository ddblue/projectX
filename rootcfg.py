from nevow import loaders, rend, tags as T
from twisted.web.static import File
import os

_sourcedir = os.path.dirname(__file__)
css = File(_sourcedir + '/css', defaultType= 'text/css')
imgs = File(_sourcedir + '/imgs', defaultType= 'image/png')

class RootTemplate(rend.Page):
    addSlash = 0
    myhtmlfile = None
    mycss = None
    myjs = None
    docFactory = loaders.htmlfile('html/template.html')

    def render_contents(self, ctx, data):
	return loaders.htmlfile(self.myhtmlfile)

    def render_css(self, ctx, data):
	return [T.link(type='text/css', rel='stylesheet', href= self.mycss)]


class Homepage(RootTemplate):
    myhtmlfile = 'html/homepage.html' 
    mycss = '/css/style.css'

class About(RootTemplate):
    myhtmlfile = 'html/about.html' 
    mycss = '/css/about.css'

class RootPage(rend.Page):
    docFactory = loaders.htmlfile('html/rootpage.html')
    def __init__(self):
	rend.Page.__init__(self)
	self.children = {
	    'homepage': Homepage(),
	    'about' : About(),
	    'css' : css,
	    'imgs' : imgs,
	    '' : self,
    
	}

