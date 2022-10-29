from bs4 import BeautifulSoup as BS
import requests
from pprint import pprint

URL_comedy = 'https://rezka.ag/animation/comedy/'
URL_fantasy = 'https://rezka.ag/animation/fantasy/'
URL_adventure = 'https://rezka.ag/animation/adventures/'
URL_everyday = 'https://rezka.ag/animation/everyday/'
URL_romance = 'https://rezka.ag/animation/romance/'
URL_sport = 'https://rezka.ag/animation/sport/'
URL_detective = 'https://rezka.ag/animation/detective/'
URL_horror = 'https://rezka.ag/animation/horror/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36',
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    anime = []
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    for item in items:
        info = item.find('div', class_='b-content__inline_item-link').find('div').getText().split(', ')
        anime.append({
            'title': item.find('div', class_='b-content__inline_item-link').find('a').getText(),
            'link': item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            'length': item.find('span', class_='info').getText()
            if item.find('span', class_='info') is not None else 'Фильм',
            'year': info[0],
            'country': info[1],
        })

    return anime


def parser_comedy():
    html = get_html(URL_comedy)
    if html.status_code == 200:
        html = get_html(URL_comedy)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_fantasy():
    html = get_html(URL_fantasy)
    if html.status_code == 200:
        html = get_html(URL_fantasy)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_adventure():
    html = get_html(URL_adventure)
    if html.status_code == 200:
        html = get_html(URL_adventure)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_everyday():
    html = get_html(URL_everyday)
    if html.status_code == 200:
        html = get_html(URL_everyday)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_romance():
    html = get_html(URL_romance)
    if html.status_code == 200:
        html = get_html(URL_romance)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_sport():
    html = get_html(URL_sport)
    if html.status_code == 200:
        html = get_html(URL_sport)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_detectives():
    html = get_html(URL_detective)
    if html.status_code == 200:
        html = get_html(URL_detective)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')


def parser_horrors():
    html = get_html(URL_horror)
    if html.status_code == 200:
        html = get_html(URL_horror)
        anime = get_data(html.text)
        return anime[:10]
    else:
        raise Exception('Parser error...')

