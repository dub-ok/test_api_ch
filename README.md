# test_api_ch


Создать две папки в корневом каталоге проекта:  
- logs
- test_results

Подтянуть allure:
```
pip3 install allure-pytest
```

Для запуска allure отчёта:
```
python -m pytest -s -v  --alluredir=test_results
```