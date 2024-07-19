import requests
from requests import Response


class Method:
    """
    to quickly replace the library that is used for the REQUEST
    """
    @staticmethod
    def custom_request(method: str, url: str, **kwargs) -> Response:
        return requests.request(method, url, **kwargs)
