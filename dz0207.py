from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('dz0207_news.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow([data['name'],
                         data['url'],
                         data['time']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('a', class_='card-mini _topnews')
    for news in p1:
        name = news.find('h3', class_='card-mini__title').text.strip()
        url = news["href"]
        time = news.find('time', class_=('card-mini__info-item')).text.strip()
        data = {
            'name': name,
            'url': url,
            'time': time
        }
        write_csv(data)


def main():
    url = 'https://lenta.ru/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
