import json
from utils.chuck_api import Chuck_api as Chuck
from utils.main_api import Main_api as Ma


class Test_api_chuck:
    """Тест методов"""

    def test_getting_chuck_random_joke(self):
        result_random_joke = Chuck.random_chuck_joke()
        check_result_random_joke = result_random_joke.json()
        print(check_result_random_joke)
        Ma.check_status(result_random_joke, 200)
