# -*- coding: utf-8 -*-

import os
from .sessions import RedisSessionInterface

class Session(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.session_interface = self._get_interface(app)

    def _get_interface (self, app):
        config = app.config.copy()
        config.setdefault('SESSION_PERMANENT', True)
        config.setdefault('SESSION_USE_SIGNER', False)
        config.setdefault('SESSION_KEY_PREFIX', 'session:')
        config.setdefault('SESSION_REDIS', None)

        session_interface = RedisSessionInterface(config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        return session_interface