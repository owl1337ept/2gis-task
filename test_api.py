from jsonschema import validate
from tools.our_request import Method
import logging

logger = logging.getLogger("rest_api")


class Token:
    """
    to access the token
    """
    def __init__(self, url):
        self.url = url
        self.method = Method

    POST_TOKENS = '/auth/tokens'

    def get_token(self):
        response = self.method.custom_request("POST", f"{self.url}{self.POST_TOKENS}")
        return response


class Favorites:
    """
    to access favorites
    """
    def __init__(self, url):
        self.url = url
        self.method = Method

    POST_FAVORITES = '/favorites'

    def set_favorites_standard(self, head: dict, data: dict, schema: dict):
        response = self.method.custom_request("POST", f"{self.url}{self.POST_FAVORITES}", headers=head, data=data)
        validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return response
