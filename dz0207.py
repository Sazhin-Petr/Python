from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы: {e}")
        return None


def write_csv(data):
    with open('euro_news.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow([data['title'], data['url'], data['time'], data['snippet']])


def get_data(html):
    if not html:
        return

    soup = BeautifulSoup(html, 'lxml')
    news_section = soup.find('div', class_='main-news__items')

    if not news_section:
        print("Не найден раздел с новостями")
        return

    news_items = news_section.find_all('div', class_='main-news__item')

    for item in news_items:
        try:
            title = item.find('a', class_='main-news__title').text.strip()
            url = 'https://www.euro-football.ru' + item.find('a', class_='main-news__title')['href']
            time = item.find('div', class_='main-news__time').text.strip()

            # Для snippet можно использовать первый абзац или оставить пустым
            snippet = ""

            data = {
                'title': title,
                'url': url,
                'time': time,
                'snippet': snippet
            }

            write_csv(data)

        except Exception as e:
            print(f"Ошибка при обработке новости: {e}")
            continue


def main():
    url = 'https://www.euro-football.ru/'

    # Создаем файл с заголовками
    with open('euro_news.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Заголовок', 'Ссылка', 'Время', 'Краткое описание'])

    # Получаем и парсим данные
    html = get_html(url)
    if html:
        get_data(html)
        print("Парсинг завершен. Данные сохранены в euro_news.csv")


if __name__ == '__main__':
    main()