# -*- coding: utf-8 -*-

from . import settings
import requests

# Courtesy of: https://stackoverflow.com/a/1794540/1039510
join_url_path = lambda *pieces: "/".join(s.strip("/") for s in pieces)


class IstsosAuth(object):
    """docstring for IstsosAuth."""

    url = None

    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    DEFAULTS = {"grant_type": "password", "client_id": "istsos-istsos"}

    def __init__(self, username, password):
        super(IstsosAuth, self).__init__()
        self.args = dict(self.DEFAULTS, username=username, password=password)

    def __call__(self):
        response = requests.post(self.url, data=self.args, headers=self.headers)

        return response

    def json(self):
        return self().json()

    def get_token(self):
        response = self()
        return response.json()["access_token"]


class IstsosCeresioAuth(IstsosAuth):
    """ """

    url = join_url_path(
        settings.ISTSOS_CERESIO_BASEURL, settings.ISTSOS_CERESIO_AUTH_ENDPOINT
    )

    def __init__(
        self,
        username=settings.ISTSOS_CERESIO_USERNAME,
        password=settings.ISTSOS_CERESIO_PASSWORD,
    ):
        super(IstsosCeresioAuth, self).__init__(username, password)


class IstsosVerbanoAuth(IstsosAuth):
    """ """

    url = join_url_path(
        settings.ISTSOS_VERBANO_BASEURL, settings.ISTSOS_VERBANO_AUTH_ENDPOINT
    )

    def __init__(
        self,
        username=settings.ISTSOS_VERBANO_USERNAME,
        password=settings.ISTSOS_VERBANO_PASSWORD,
    ):
        super(IstsosVerbanoAuth, self).__init__(username, password)


class IstsosLarioAuth(IstsosAuth):
    """ """

    url = join_url_path(
        settings.ISTSOS_LARIO_BASEURL, settings.ISTSOS_LARIO_AUTH_ENDPOINT
    )

    def __init__(
        self,
        username=settings.ISTSOS_LARIO_USERNAME,
        password=settings.ISTSOS_LARIO_PASSWORD,
    ):
        super(IstsosLarioAuth, self).__init__(username, password)

class IstsosVareseAuth(IstsosAuth):
    """ """

    url = join_url_path(
        settings.ISTSOS_VARESE_BASEURL, settings.ISTSOS_VARESE_AUTH_ENDPOINT
    )

    def __init__(
        self,
        username=settings.ISTSOS_VARESE_USERNAME,
        password=settings.ISTSOS_VARESE_PASSWORD,
    ):
        super(IstsosVareseAuth, self).__init__(username, password)

def test():
    # istsos = IstsosLarioAuth()
    # istsos = IstsosVerbanoAuth()
    istsos = IstsosCeresioAuth()
    token = istsos.get_token()
    print(token)


if __name__ == "__main__":
    istsos = IstsosAuth()
    token = istsos.get_token()
