import time
from test_api import Token
from test_api import Favorites
from tools.favorites import valid_schema
from tools.favorites import error_schema
from tools.models import FavoritesData

URL = 'https://regions-test.2gis.com/v1'
TYPE_ERROR = 400
INSPIRED = 401
OK = 200
TOKEN_ERROR = "Передан несуществующий или «протухший» 'token'"
COLOR_ERROR = "Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW"
LAT_ERROR = [
    "Параметр 'lat' должен быть не менее -90",
    "Параметр 'lat' должен быть не более 90",
    "Параметр 'lat' является обязательным"
]
LON_ERROR = [
    "Параметр 'lon' должен быть не менее -180",
    "Параметр 'lon' должен быть не более 180",
    "Параметр 'lon' является обязательным"
]
TITLE_ERROR = [
    "Параметр 'title' не может быть пустым",
    "Параметр 'title' должен содержать не более 999 символов"
]


class TestApi:
    def test_add_random_favorite(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_random_favorite()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=valid_schema)
        assert response.status_code == OK, "Status code error"
        response_json = response.json()
        for key, value in data.items():
            if key == "lat" or key == "lon":
                value = float(value)
                value = round(value, 6)
            assert response_json[key] == value

    def test_inspired_token(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        time.sleep(2.1)
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_random_favorite()

        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == INSPIRED, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == TOKEN_ERROR, "Incorrect message"

    # it makes no sense to test several invalid parameters, since they are processed sequentially
    def test_wrong_title(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_little_title()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == TITLE_ERROR[0], "Incorrect message"

        response = Token(url=URL).get_token()  #there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_big_title()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == TITLE_ERROR[1], "Incorrect message"

        response = Token(url=URL).get_token()  # there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_large_title()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == TITLE_ERROR[1], "Incorrect message"

    def test_wrong_lat(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_negative_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == LAT_ERROR[0], "Incorrect message"

        response = Token(url=URL).get_token()  #there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_positive_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == LAT_ERROR[1], "Incorrect message"

        response = Token(url=URL).get_token()  # there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_none_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == LAT_ERROR[2], "Incorrect message"

    def test_wrong_lon(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_negative_lon()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == LON_ERROR[0], "Incorrect message"

        response = Token(url=URL).get_token()  #there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_positive_lon()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == LON_ERROR[1], "Incorrect message"

        response = Token(url=URL).get_token()  # there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_none_lon()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == LON_ERROR[2], "Incorrect message"

    def test_wrong_color(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_color()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == COLOR_ERROR, "Incorrect message"

        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_combination_color()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
        assert response.json().get('error', {}).get('message', 'Unknown error') == COLOR_ERROR, "Incorrect message"


    # CURL can not encode special symbols
    # def test_greek_title(self):
    #     response = Token(url=URL).get_token()
    #     assert response.status_code == OK, "Token response status is not 200"
    #     token = response.cookies.get('token')
    #     assert token, "Token was not found"
    #     head = FavoritesData.set_token(token=token)
    #     data = FavoritesData.set_greek()
    #     response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
    #     assert response.status_code == TYPE_ERROR, "Status code error"

