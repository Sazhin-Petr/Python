from bs4 import BeautifulSoup
import requests


class Parsing:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def par(self):
        games = self.html.find_all('article', class_='game')
        for game in games:
            title = game.find('h2').text
            href = game.find('a')['href']
            date = game.find('div', class_='date').text
            self.res.append({
                'title': title,
                'href': href,
                'date': date
            })

    def save(self):
        with open(self.path, 'w') as f:
            num = 1
            for item in self.res:
                f.write(f'Игра № {num}\n\nНазвание: {item["title"]}'
                        f'\nСсылка: {item["href"]}\nДата создания: {item["date"]}\n\n{"*" * 40}\n')
                num += 1

    def run(self):
        self.get_html()
        self.par()
        self.save()
