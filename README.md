# python-parser

### Установка
##### Устанавливаем BeautifulSoup

`apt-get install libxml2-dev libxslt-dev python-dev`
`pip install beautifulsoup4`

##### Устанавливаем requests
`pip install requests`
##### Устанавливаем psycopg2 для связи с PostgreSQL
`pip install psycopg2-binary`

##### Добавляем таблицу movies в PostgreSQL
`psql < db.sql`

### Запуск
`python get_movie_list.py`
