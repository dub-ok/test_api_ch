from utils.main_api import Main_api as Ma
import utils.url_list as url


class Chuck_api:
    """Класс с методами для получения шуток о Чаке Норрисе"""
    @staticmethod
    def random_chuck_joke():
        """Случайная шутка"""
        result_random_joke = Ma.get_method(url.random_joke_url)
        return result_random_joke

