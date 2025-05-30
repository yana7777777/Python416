import requests
from bs4 import BeautifulSoup


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("div", class_="wrapper_inner")[1]
    kinds = p1.find_all("li")

    for kind in kinds:
        url = kind.find("a")["href"]
        print(url)


def main():
    url = "https://aquabot-zip.ru/catalog/"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()








