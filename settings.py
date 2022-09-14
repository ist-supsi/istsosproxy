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

ISTSOS_AUTH_ENDPOINT = 'auth/realms/istsos/protocol/openid-connect/token'

# Lago di Lugano
ISTSOS_CERESIO_BASEURL = 'https://istsos.ddns.net'
ISTSOS_CERESIO_AUTH_ENDPOINT = ISTSOS_AUTH_ENDPOINT
ISTSOS_CERESIO_USERNAME = ''
ISTSOS_CERESIO_PASSWORD = ''

# Lago Maggiore
ISTSOS_VERBANO_BASEURL = 'http://150.145.35.198:2000'
ISTSOS_VERBANO_AUTH_ENDPOINT = ISTSOS_AUTH_ENDPOINT
ISTSOS_VERBANO_USERNAME = ''
ISTSOS_VERBANO_PASSWORD = ''

# Lago di Como
ISTSOS_LARIO_BASEURL = ISTSOS_VERBANO_BASEURL
ISTSOS_LARIO_AUTH_ENDPOINT = ISTSOS_AUTH_ENDPOINT
ISTSOS_LARIO_USERNAME = ''
ISTSOS_LARIO_PASSWORD = ''

# ISTSOS_SERVICES = 'demo'
# ISTSOS_USERNAME = 'test'
# ISTSOS_PASSWORD = 'test'

ALLOWED_ORIGINS = 'http://localhost:8080,http://172.20.0.3:8080'

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass
