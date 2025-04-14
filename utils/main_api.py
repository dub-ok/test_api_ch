import allure
import requests
from utils.logger import Logger


class Main_api:
    """Тут будут методы написанные специально для теста"""

    @staticmethod
    # метод GET
    def get_method(url):
        with allure.step("GET random joke"):
            Logger.add_request(url, method="GET")
            result = requests.get(url)
            Logger.add_response(result)
            return result




