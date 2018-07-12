from re import compile as re_compile
from requests import get as requests_get
from bs4 import BeautifulSoup
from psycopg2 import connect


url_base = 'https://www.kinopoisk.ru'
url = 'test.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}


def get_page(url, headers):
    r = requests_get(url, headers=headers)
    data = r.text.encode('cp1251')
    return data


def db_write(sql_data):
    sql_request = """
        INSERT INTO movies (name, url, "like", dislike) VALUES (%s, %s, %s, %s)
        ON CONFLICT (url) DO UPDATE SET 
            name=EXCLUDED.name, 
            "like" = EXCLUDED."like",
            dislike = EXCLUDED.dislike
    """
    with connect() as con:
        cur = con.cursor()
        cur.execute(sql_request, sql_data)
        con.commit()


def main():
    main_soup = BeautifulSoup(get_page('%s%s' % (url_base, '/top'), headers))
    movie_data = main_soup.find_all('tr', id=re_compile("^top250"))
    counter = 0
    for item in movie_data[:1]:
        counter += 1
        movie_link = item.find('a', {'class': 'all'}).get('href')
        print counter, movie_link
        movie_url = '%s%s' % (url_base, movie_link)
        movie_soup = BeautifulSoup(get_page(movie_url, headers))
        movie_name = movie_soup.find('h1', {'itemprop': 'name'}).text
        positive = int(movie_soup.find('li', {'class': 'pos'}).find('b').text)
        negative = int(movie_soup.find('li', {'class': 'neg'}).find('b').text)
        db_write((movie_name, movie_url, positive, negative))


if __name__=='__main__':
    main()