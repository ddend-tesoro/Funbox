Сервис запускается командой
docker-compose up

создается три контейнер
-redis
-flask
-redis-test (загрузка тестовых данных в Redis)

GET запрос со статистикой доступен по адрессу
localhost:5000/visited_domains?from=1545221231&to=1545217638

POST запрос для загрузки данных в Redis
localhost:5000/visited_links