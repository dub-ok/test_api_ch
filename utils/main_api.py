import requests


class Main_api:
    """Тут будут методы написанные специально для теста"""

    @staticmethod
    # метод GET
    def get_method(url):
        result = requests.get(url)
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



