import requests


class Main_api:
    """Тут будут методы написанные специально для теста"""

    @staticmethod
    # метод GET
    def get_method(url):
        result = requests.get(url)
        return result




