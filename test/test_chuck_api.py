import allure
from utils.chuck_api import Chuck_api as Chuck
from utils.main_api import Main_api as Ma
from utils import url_list as url


@allure.epic("Get Chuck's jokes")
class Test_api_chuck_random_joke:
    """Тест методов"""

    @allure.description("Get random Chuck's jokes")
    def test_getting_chuck_random_joke(self):
        print("Получаем случайную шутку")
        result_random_joke = Chuck.random_chuck_joke()
        check_result_random_joke = result_random_joke.json()
        print(check_result_random_joke)
        print("Получаем статус случайной шутки")
        Ma.check_status(result_random_joke, 200)
        print("Проверка полей")
        Ma.check_json_value(result_random_joke, 'categories', [])
        Ma.check_json_value(result_random_joke, 'icon_url', url.icon_url)
