import pytest


@pytest.fixture()
def func_support():
    print(f"\nДелаю до начала функции!!!!")
    yield
    print(f"\nДелаю после завершения функции!!!!")
