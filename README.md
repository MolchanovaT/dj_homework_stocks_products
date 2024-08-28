# Склады и товары

## Создание образа
docker build . --tag=my_app:1.0
## Запуск контейнера
docker run -d -p 5555:8000 --name my_app my_app:1.0

## Проверка в VSC отправкой запросов в файле requests-examples