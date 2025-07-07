from bs4 import BeautifulSoup
import requests
import re
import csv

# r = requests.get('https://ru.wordpress.org/')


def get_html(url):
    r = requests.get(url)
    return r.text


# def refined(s):
#     return re.sub(r'\D+', '', s)


def write_csv(data):
    with open('news.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow([data['name'], data['url'], data['rating'], data['snippet']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('span', class_='main-news-items-widget__item-mark')
    pluggins = p1.find_all('li')
    for plugin in pluggins:
        try:
            name = plugin.find('h3', class_='entry-title').text
        except:
            name = ""
        url = plugin.find('h3', class_='entry-title').find('a').get('href')
        rating = plugin.find('span', class_='rating-count').text
        replays_rating = refined(rating)
        snippet = plugin.find('div', class_='entry-excerpt').text.strip()

        data = {'name': name, 'url': url, 'rating': replays_rating, 'snippet': snippet}
        write_csv(data)


def main():
    url = 'https://www.euro-football.ru/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()