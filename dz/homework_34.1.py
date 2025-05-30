

import requests
from bs4 import BeautifulSoup


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("section", class_="plugin-section")[1]
    kinds = p1.find_all("li")

    for kind in kinds:
        name = kind.find("h3").text
        url = kind.find("h3").find("a").get("href")
        print(url)


def main():
    url = "https://ru.wordpress.org/plugins/"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()