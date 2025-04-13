import requests
import json
from utils.logger import Logger


class Main_api:
    """Тут будут методы написанные специально для теста"""

    @staticmethod
    # метод GET
    def get_method(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url)
        Logger.add_response(result)
        return result

    """проверка статус кода"""
    @staticmethod
    def check_status(result, code):
        print(result.status_code)
        assert code == result.status_code
        if result.status_code == code:
            print(f"Упешно!!! Статус код = {result.status_code}")
        else:
            print(f"провал!! Статус код = {result.status_code}")

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        print(check_info)
        assert check_info == expected_value
        print(f"{field_name} верен")


