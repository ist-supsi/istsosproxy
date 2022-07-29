# -*- coding: utf-8 -*-

import os
# from py4web.core import required_folder

# db settings
APP_FOLDER = os.path.dirname(__file__)
APP_NAME = os.path.split(APP_FOLDER)[-1]

# logger settings
LOGGERS = [
    "warning:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

ISTSOS_SERVICES = 'demo'
ISTSOS_USERNAME = 'test'
ISTSOS_PASSWORD = 'test'

ALLOWED_ORIGINS = 'http://localhost:8080,http://172.20.0.3:8080'

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass
