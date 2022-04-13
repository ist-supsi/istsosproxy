# -*- coding: utf-8 -*-

import sys
import logging
# from mptools.frameworks.py4web.controller import CORS
from . import settings

from py4web import request
from py4web.utils.cors import CORS
from py4web.core import Fixture
from py4web.core import HTTP

# #######################################################
# implement custom loggers form settings.LOGGERS
# #######################################################
logger = logging.getLogger("py4web:" + settings.APP_NAME)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
for item in settings.LOGGERS:
    level, filename = item.split(":", 1)
    if filename in ("stdout", "stderr"):
        handler = logging.StreamHandler(getattr(sys, filename))
    else:
        handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    logger.setLevel(getattr(logging, level.upper(), "DEBUG"))
    logger.addHandler(handler)


cors = CORS(origin=settings.ALLOWED_ORIGINS)

class CheckIn(Fixture):
    """docstring for CheckIn."""

    def __init__(self, origin='http://localhost'):
        super(CheckIn, self).__init__()
        self.origins = origin.split(',')

    def on_request(self, context=None):
        current_origin = request.environ.get('HTTP_ORIGIN')
        if not any(map(lambda o: o==current_origin, self.origins)):
            logger.info(f'Current origin {current_origin} not allowed.')
            raise HTTP(403)
        else:
            logger.debug(f'Check passed for current origin {current_origin}.')

checkin = CheckIn(origin=settings.ALLOWED_ORIGINS)
