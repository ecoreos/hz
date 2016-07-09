# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

"""
eCore - Server
eCore is an ERP+CRM program for small and medium businesses.

The whole source code is distributed under the terms of the
GNU Public Licence.

(c) 2003-TODAY, Fabien Pinckaers - eCore SA
"""

import atexit
import csv
import logging
import os
import signal
import sys
import threading
import traceback
import time

import ecore

from . import Command

__author__ = ecore.release.author
__version__ = ecore.release.version

# Also use the `ecore` logger for the main script.
_logger = logging.getLogger('ecore')

def check_root_user():
    """Warn if the process's user is 'root' (on POSIX system)."""
    if os.name == 'posix':
        import pwd
        if pwd.getpwuid(os.getuid())[0] == 'root':
            sys.stderr.write("Running as user 'root' is a security risk.\n")

def check_postgres_user():
    """ Exit if the configured database user is 'postgres'.

    This function assumes the configuration has been initialized.
    """
    config = ecore.tools.config
    if config['db_user'] == 'postgres':
        sys.stderr.write("Using the database user 'postgres' is a security risk, aborting.")
        sys.exit(1)

def report_configuration():
    """ Log the server version and some configuration values.

    This function assumes the configuration has been initialized.
    """
    config = ecore.tools.config
    _logger.info("eCore version %s", __version__)
    _logger.info('addons paths: %s', ecore.modules.module.ad_paths)
    host = config['db_host'] or os.environ.get('PGHOST', 'default')
    port = config['db_port'] or os.environ.get('PGPORT', 'default')
    user = config['db_user'] or os.environ.get('PGUSER', 'default')
    _logger.info('database: %s@%s:%s', user, host, port)

def rm_pid_file(main_pid):
    config = ecore.tools.config
    if config['pidfile'] and main_pid == os.getpid():
        try:
            os.unlink(config['pidfile'])
        except OSError:
            pass

def setup_pid_file():
    """ Create a file with the process id written in it.

    This function assumes the configuration has been initialized.
    """
    config = ecore.tools.config
    if not ecore.evented and config['pidfile']:
        pid = os.getpid()
        with open(config['pidfile'], 'w') as fd:
            fd.write(str(pid))
        atexit.register(rm_pid_file, pid)

def export_translation():
    config = ecore.tools.config
    dbname = config['db_name']

    if config["language"]:
        msg = "language %s" % (config["language"],)
    else:
        msg = "new language"
    _logger.info('writing translation file for %s to %s', msg,
        config["translate_out"])

    fileformat = os.path.splitext(config["translate_out"])[-1][1:].lower()

    with open(config["translate_out"], "w") as buf:
        registry = ecore.modules.registry.RegistryManager.new(dbname)
        with ecore.api.Environment.manage():
            with registry.cursor() as cr:
                ecore.tools.trans_export(config["language"],
                    config["translate_modules"] or ["all"], buf, fileformat, cr)

    _logger.info('translation file written successfully')

def import_translation():
    config = ecore.tools.config
    context = {'overwrite': config["overwrite_existing_translations"]}
    dbname = config['db_name']

    registry = ecore.modules.registry.RegistryManager.new(dbname)
    with ecore.api.Environment.manage():
        with registry.cursor() as cr:
            ecore.tools.trans_load(
                cr, config["translate_in"], config["language"], context=context,
            )

def main(args):
    check_root_user()
    ecore.tools.config.parse_config(args)
    check_postgres_user()
    report_configuration()

    config = ecore.tools.config

    # the default limit for CSV fields in the module is 128KiB, which is not
    # quite sufficient to import images to store in attachment. 500MiB is a
    # bit overkill, but better safe than sorry I guess
    csv.field_size_limit(500 * 1024 * 1024)

    if config["db_name"]:
        try:
            ecore.service.db._create_empty_database(config["db_name"])
        except ecore.service.db.DatabaseExists:
            pass

    if config["test_file"]:
        config["test_enable"] = True

    if config["translate_out"]:
        export_translation()
        sys.exit(0)

    if config["translate_in"]:
        import_translation()
        sys.exit(0)

    # This needs to be done now to ensure the use of the multiprocessing
    # signaling mecanism for registries loaded with -d
    if config['workers']:
        ecore.multi_process = True

    preload = []
    if config['db_name']:
        preload = config['db_name'].split(',')

    stop = config["stop_after_init"]

    setup_pid_file()
    rc = ecore.service.server.start(preload=preload, stop=stop)
    sys.exit(rc)

class Server(Command):
    """Start the ecore server (default command)"""
    def run(self, args):
        main(args)
