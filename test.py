import pytest
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

# Helper function to get a token
def get_token():
    response = Token(url=URL).get_token()
    assert response.status_code == OK, "Token response status is not 200"
    token = response.cookies.get('token')
    assert token, "Token was not found"
    return token

# Parameterized test for adding random favorite
@pytest.mark.parametrize('data, expected_status_code', [
    (FavoritesData.set_random_favorite(), OK)
])
def test_add_random_favorite(data, expected_status_code):
    token = get_token()
    head = FavoritesData.set_token(token=token)
    response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=valid_schema)
    assert response.status_code == expected_status_code, "Status code error"
    response_json = response.json()
    for key, value in data.items():
        if key in ["lat", "lon"]:
            value = round(float(value), 6)
        assert response_json[key] == value

# Parameterized test for expired token
@pytest.mark.parametrize('data, expected_status_code, expected_error', [
    (FavoritesData.set_random_favorite(), INSPIRED, TOKEN_ERROR)
])
def test_inspired_token(data, expected_status_code, expected_error):
    token = get_token()
    time.sleep(2.1)
    head = FavoritesData.set_token(token=token)
    response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
    assert response.status_code == expected_status_code, "Status code error"
    assert response.json().get('error', {}).get('message', 'Unknown error') == expected_error, "Incorrect message"

# Parameterized tests for invalid title
@pytest.mark.parametrize('data, expected_error_message', [
    (FavoritesData.set_little_title(), TITLE_ERROR[0]),
    (FavoritesData.set_big_title(), TITLE_ERROR[1]),
    (FavoritesData.set_large_title(), TITLE_ERROR[1])
])
def test_wrong_title(data, expected_error_message):
    token = get_token()
    head = FavoritesData.set_token(token=token)
    response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
    assert response.status_code == TYPE_ERROR, "Status code error"
    assert response.json().get('error', {}).get('message', 'Unknown error') == expected_error_message, "Incorrect message"

# Parameterized tests for invalid lat
@pytest.mark.parametrize('data, expected_error_message', [
    (FavoritesData.set_wrong_negative_lat(), LAT_ERROR[0]),
    (FavoritesData.set_wrong_positive_lat(), LAT_ERROR[1]),
    (FavoritesData.set_none_lat(), LAT_ERROR[2])
])
def test_wrong_lat(data, expected_error_message):
    token = get_token()
    head = FavoritesData.set_token(token=token)
    response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
    assert response.status_code == TYPE_ERROR, "Status code error"
    assert response.json().get('error', {}).get('message', 'Unknown error') == expected_error_message, "Incorrect message"

# Parameterized tests for invalid lon
@pytest.mark.parametrize('data, expected_error_message', [
    (FavoritesData.set_wrong_negative_lon(), LON_ERROR[0]),
    (FavoritesData.set_wrong_positive_lon(), LON_ERROR[1]),
    (FavoritesData.set_none_lon(), LON_ERROR[2])
])
def test_wrong_lon(data, expected_error_message):
    token = get_token()
    head = FavoritesData.set_token(token=token)
    response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
    assert response.status_code == TYPE_ERROR, "Status code error"
    assert response.json().get('error', {}).get('message', 'Unknown error') == expected_error_message, "Incorrect message"

# Parameterized tests for invalid color
@pytest.mark.parametrize('data, expected_error_message', [
    (FavoritesData.set_wrong_color(), COLOR_ERROR),
    (FavoritesData.set_combination_color(), COLOR_ERROR)
])
def test_wrong_color(data, expected_error_message):
    token = get_token()
    head = FavoritesData.set_token(token=token)
    response = Favorites(url=URL).set_favorites_standard(head=head, data=data, schema=error_schema)
    assert response.status_code == TYPE_ERROR, "Status code error"
    assert response.json().get('error', {}).get('message', 'Unknown error') == expected_error_message, "Incorrect message"

