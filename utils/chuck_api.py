from utils.main_api import Main_api as Ma
import utils.url_list as url


class Chuck_api:
    """Класс с методами для получения шуток о Чаке Норрисе"""
    @staticmethod
    def random_chuck_joke():
        """Случайная шутка"""
        result_random_joke = Ma.get_method(url.random_joke_url)
        return result_random_joke

    @staticmethod
    def chuck_joke_categories():
        """Категории шуток"""
        result_chuck_joke_categories = Ma.get_method(url.category_joke_url)
        return result_chuck_joke_categories

    @staticmethod
    def random_chuck_joke_category(category):
        """Случайная шутка в категории"""
        category_url = url.base_url + category
        result_random_chuck_joke_category = Ma.get_method(category_url)
        return result_random_chuck_joke_category
