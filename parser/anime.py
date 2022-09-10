import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/animation/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36",
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="b-content__inline_item")
    anime = []
    for item in items:
        desk = item.find("div", class_="b-content__inline_item-link").find("div").getText().split(', ')
        anime.append({
            "ttitle": item.find("div", class_="b-content__inline_item-link").find('a').getText(),
            "year": desk[0],
            "city": desk[1],
            "genre": desk[2],
            "link": item.find("div", class_="b-content__inline_item-link").find('a').get("href"),
        })
        return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 5):
            html = get_html(f"{URL}page/{page}/")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Ошибка")

print(parser())
