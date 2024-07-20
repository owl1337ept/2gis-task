import random
import string

from faker import Faker

fake = Faker()


def generate_title(min_length=1, max_length=999):
    cyrillic = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    latin = string.ascii_letters + string.digits + string.punctuation
    chars = cyrillic + latin
    length = random.randint(min_length, max_length)
    title = ''.join(random.choice(chars) for _ in range(length))
    return title


class Response:
    """
    Для быстрой замены библиотеки, которая используется для REQUEST
    """
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response


class FavoritesData:
    """
    Модели для тестов
    """
    @staticmethod
    def set_token(token):
        return {"Cookie": f"token={token}"}

    @staticmethod
    def set_random_favorite():
        title = generate_title()
        lat = fake.latitude()
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_little_title():
        title = ""
        lat = fake.latitude()
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_big_title():
        title = 's' * 1000
        lat = fake.latitude()
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_large_title():
        title = 's' * random.randint(1001, 10000)
        lat = fake.latitude()
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_wrong_negative_lat():
        title = generate_title()
        lat = -90.000001
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_wrong_positive_lat():
        title = generate_title()
        lat = 90.000001
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_wrong_negative_lon():
        title = generate_title()
        lat = fake.latitude()
        lon = -180.000001
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_wrong_positive_lon():
        title = generate_title()
        lat = fake.latitude()
        lon = 180.000001
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_wrong_color():
        title = generate_title()
        lat = fake.latitude()
        lon = fake.longitude()
        color = "test"
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_combination_color():
        title = generate_title()
        lat = fake.latitude()
        lon = fake.longitude()
        color = "BLUEGREEN"
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_none_lat():
        title = generate_title()
        lat = None
        lon = fake.longitude()
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    @staticmethod
    def set_none_lon():
        title = generate_title()
        lat = fake.latitude()
        lon = None
        color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
        return {"title": title, "lat": lat, "lon": lon, "color": color}

    # CURL can not encode special symbols
    # @staticmethod
    # def set_greek():
    #     title = '\u0394'
    #     lat = fake.latitude()
    #     lon = fake.longitude()
    #     color = fake.random_element(elements=("BLUE", "GREEN", "RED", "YELLOW")) if fake.boolean() else None
    #     print(title)
    #     return {"title": title, "lat": lat, "lon": lon, "color": color}