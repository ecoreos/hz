import json
import urllib
import ecore
from ecore import http
from ecore.http import request
import ecore.addons.web.controllers.main as webmain
from ecore.addons.web.http import SessionExpiredException
from werkzeug.exceptions import BadRequest
import werkzeug.utils

class google_auth(http.Controller):
    
    @http.route('/google_account/authentication', type='http', auth="none")
    def oauth2callback(self, **kw):
        """ This route/function is called by Google when user Accept/Refuse the consent of Google """
        
        state = json.loads(kw['state'])
        dbname = state.get('d')
        service = state.get('s')
        url_return = state.get('f')
        
        registry = ecore.modules.registry.RegistryManager.get(dbname)
        with registry.cursor() as cr:
            if kw.get('code',False):
                registry.get('google.%s' % service).set_all_tokens(cr,request.session.uid,kw['code'])
                return werkzeug.utils.redirect(url_return)
            elif kw.get('error'):
                return werkzeug.utils.redirect("%s%s%s" % (url_return ,"?error=" , kw.get('error')))
            else:
                return werkzeug.utils.redirect("%s%s" % (url_return ,"?error=Unknown_error"))

        
