from utils.chuck_api import Chuck_api as Chuck


class Test_api_chuck:
    """Тест методов"""
    def test_getting_chuck_joke(self):
        result_random_joke = Chuck.random_chuck_joke()
        print(result_random_joke.text)