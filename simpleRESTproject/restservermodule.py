
__author__ = 'vivekl'

import cherrypy
import logging
try:
    import simplejson as json
except ImportError:
    import json

class ScopesRESTService:

    __scopes = {
        'SCM_scope': ['PLMN-PLMN/RNC-148/WBTS-1/WCEL-1', 'PLMN-PLMN/RNC-148/WBTS-1/WCEL-2'],
        'CAC_scope': ['PLMN-PLMN/RNC-150/LNBTS-1/LNCEL-1', 'PLMN-PLMN/RNC-150/LNBTS-2/LNCEL-5'],
        'PCI_scope': ['PLMN-PLMN/RNC-150/LNBTS-2/LNCEL-3', 'PLMN-PLMN/RNC-150/LNBTS-2/LNCEL-1']
    }

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['PUT'])
    def index(self):
        return "Hello, welcome to Python RESTful service!"

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def get_scope(self, scope_name='SCM_scope'):
        logging.info('GET scope method invoked')
        return self.__scopes[scope_name]

    @cherrypy.tools.json_in()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def add_scope(self):
        self.__scopes.update(cherrypy.request.json)

if __name__ == '__main__':

    cherrypy.config.update({'server.socket_port': 7711})
    conf = {
        '/': {'request.dispatch': cherrypy.dispatch.Dispatcher()}
    }
    cherrypy.tree.mount(ScopesRESTService(), '/api/scopes', conf)
    cherrypy.quickstart(ScopesRESTService(), '/', conf)
