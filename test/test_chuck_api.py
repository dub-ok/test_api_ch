import allure
from utils.chuck_api import Chuck_api as Chuck
from utils import url_list as url
from utils.checking import Checkin_api as Ca


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
        Ca.check_status(result_random_joke, 200)
        print("Проверка полей")
        Ca.check_json_value(result_random_joke, 'categories', [])
        Ca.check_json_value(result_random_joke, 'icon_url', url.icon_url)

    @allure.description("Get Chuck's jokes in random category")
    def test_getting_chuck_joke_in_category(self):
        print("Получаем список категорий")
        result_joke_categories = Chuck.chuck_joke_categories()
        print("Получаем случайную категорию из списка")
        random_category = Ca.get_random_category(result_joke_categories)
        print(f"Получена случайная категория '{random_category}'")
        print(f"Получаем случайную шутку в категории '{random_category}'")
        result_random_joke_in_category = Chuck.random_chuck_joke_category(random_category)
        check_result_random_joke_in_category = result_random_joke_in_category.json()
        print(check_result_random_joke_in_category)
        print("Получаем статус случайной шутки")
        Ca.check_status(result_random_joke_in_category, 200)
        print("Проверка полей")
        Ca.check_json_value(result_random_joke_in_category, 'categories', [random_category])
        Ca.check_json_value(result_random_joke_in_category, 'icon_url', url.icon_url)
