import sys

# Mock deprecated ecore.addons.web.http module
import ecore.http
sys.modules['ecore.addons.web.http'] = ecore.http
http = ecore.http

import controllers
