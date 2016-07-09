# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

import code
import os
import signal
import sys

import ecore
from . import Command

def raise_keyboard_interrupt(*a):
    raise KeyboardInterrupt()

class Console(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>"):
        code.InteractiveConsole.__init__(self, locals, filename)
        try:
            import readline
            import rlcompleter
        except ImportError:
            print 'readline or rlcompleter not available, autocomplete disabled.'
        else:
            readline.set_completer(rlcompleter.Completer(locals).complete)
            readline.parse_and_bind("tab: complete")

class Shell(Command):
    """Start ecore in an interactive shell"""
    def init(self, args):
        ecore.tools.config.parse_config(args)
        ecore.cli.server.report_configuration()
        ecore.service.server.start(preload=[], stop=True)
        signal.signal(signal.SIGINT, raise_keyboard_interrupt)

    def console(self, local_vars):
        if not os.isatty(sys.stdin.fileno()):
            exec sys.stdin in local_vars
        else:
            if 'env' not in local_vars:
                print 'No environment set, use `ecore.py shell -d dbname` to get one.'
            for i in sorted(local_vars):
                print '%s: %s' % (i, local_vars[i])
            Console(locals=local_vars).interact()

    def shell(self, dbname):
        local_vars = {
            'ecore': ecore
        }
        with ecore.api.Environment.manage():
            if dbname:
                registry = ecore.modules.registry.RegistryManager.get(dbname)
                with registry.cursor() as cr:
                    uid = ecore.SUPERUSER_ID
                    ctx = ecore.api.Environment(cr, uid, {})['res.users'].context_get()
                    env = ecore.api.Environment(cr, uid, ctx)
                    local_vars['env'] = env
                    local_vars['self'] = env.user
                    self.console(local_vars)
            else:
                self.console(local_vars)

    def run(self, args):
        self.init(args)
        self.shell(ecore.tools.config['db_name'])
        return 0
