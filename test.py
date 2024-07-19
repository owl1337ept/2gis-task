import time
from rest_api import Token
from rest_api import Favorites
from tools.favorites import valid_schema
from tools.favorites import error_schema
from tools.models import FavoritesData

URL = 'https://regions-test.2gis.com/v1'
TYPE_ERROR = 400
INSPIRED = 401
OK = 200


class TestRestApi:
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
        time.sleep(3)
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_random_favorite()

        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == INSPIRED, "Status code error"

    def test_wrong_title(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_little_title()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

        response = Token(url=URL).get_token()  #there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_big_title()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

    def test_wrong_lat(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_negative_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

        response = Token(url=URL).get_token()  #there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_positive_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

        response = Token(url=URL).get_token()  # there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_none_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

    def test_wrong_lon(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_negative_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

        response = Token(url=URL).get_token()  #there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_positive_lat()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

        response = Token(url=URL).get_token()  # there may not be enough time
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_none_lon()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"

    def test_wrong_color(self):
        response = Token(url=URL).get_token()
        assert response.status_code == OK, "Token response status is not 200"
        token = response.cookies.get('token')
        assert token, "Token was not found"
        head = FavoritesData.set_token(token=token)
        data = FavoritesData.set_wrong_color()
        response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
        assert response.status_code == TYPE_ERROR, "Status code error"
