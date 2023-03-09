from py4web import action

# -*- coding: utf-8 -*-

from py4web import action, HTTP

from .istsos_auth import IstsosCeresioAuth, IstsosVerbanoAuth, IstsosLarioAuth, IstsosVareseAuth
from .common import logger, cors #, checkin

# from .tools import get_form

ceresio = IstsosCeresioAuth()
verbano = IstsosVerbanoAuth()
lario = IstsosLarioAuth()
varese = IstsosVareseAuth()


@action("index", method=["GET", "POST", "COMMENT"])
# @action("istsos", method=["GET", "POST"])
# @action("istsos.json", method=["GET", "POST"])
@action("ceresio", method=["GET", "POST", "COMMENT"])
@action.uses(cors)
def get_ceresio_istsos_token():
    """ """
    return ceresio.json()

@action("verbano", method=["GET", "POST", "COMMENT"])
@action.uses(cors)
def get_verbano_istsos_token():
    """ """
    return verbano.json()

@action("lario", method=["GET", "POST", "COMMENT"])
@action.uses(cors)
def get_lario_istsos_token():
    """ """
    return lario.json()

@action("varese", method=["GET", "POST", "COMMENT"])
@action.uses(cors)
def get_varese_istsos_token():
    """ """
    return varese.json()
