import requests


class Main_api:
    """Тут будут методы написанные специально для теста"""

    @staticmethod
    # метод GET
    def get_method(url):
        result = requests.get(url)
        return result

    @staticmethod
    def check_status(result_random_joke, code):
        print(result_random_joke.status_code)
        assert code == result_random_joke.status_code
        if result_random_joke.status_code == code:
            print(f"Упешно!!! Статус код = {result_random_joke.status_code}")
        else:
            print(f"провал!! Статус код = {result_random_joke.status_code}")



