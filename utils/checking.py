import random


class Checkin_api:
    """Методы проверок на различные параметры"""

    """проверка статус кода"""
    @staticmethod
    def check_status(result, code):
        print(result.status_code)
        assert code == result.status_code
        if result.status_code == code:
            print(f"Упешно!!! Статус код = {result.status_code}")
        else:
            print(f"провал!! Статус код = {result.status_code}")

    """метод на проверку значения поля"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        print(check_info)
        assert check_info == expected_value
        print(f"Значение поля {field_name} верен")

    """метод получения случайной категории шутки"""
    @staticmethod
    def get_random_category(category):
        category = category.json()
        category = random.choice(category)
        return category



