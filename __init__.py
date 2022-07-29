from py4web import action

# -*- coding: utf-8 -*-

from py4web import action, HTTP

from .istsos_auth import IstsosAuth
from .common import logger, cors #, checkin

# from .tools import get_form

istsos = IstsosAuth()

@action("index", method=["GET", "POST", "COMMENT"])
@action("istsos", method=["GET", "POST"])
@action("istsos.json", method=["GET", "POST"])
@action.uses(cors)
def get_istsos_token():
    """ """
    logger.debug('ciao')
    return istsos.json()
