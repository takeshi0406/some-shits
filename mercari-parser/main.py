import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dataclasses import dataclass

def main():
    urls = [
        'https://www.mercari.com/jp/u/252084402/',
        'https://www.mercari.com/jp/u/252084402/?max_pager_id=5249963702'
    ]
    for u in urls:
        content = get_content(u)
        for y in parse(content):
            print(f"* [{y.title}]({y.url})")


def get_content(url):
    result = requests.get(url, headers={'User-Agent': 'Sample Header'})
    result.raise_for_status()
    return BeautifulSoup(result.text)

def parse(content):
    l = content.find_all(class_="items-box")
    return [parse_each(x) for x in l]

def parse_each(x):
    return Content(
        title=x.find(class_="items-box-name").text,
        url=urljoin("https://www.mercari.com/", x.find("a").get("href")),
        price=int(x.find(class_="items-box-price").text.lstrip('¥').replace(",", "")),
    )

@dataclass
class Content:
    title: str
    url: str
    price: str

if __name__ == "__main__":
    main()
