#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup


class roads_to_philosophy:
    def __init__(self) -> None:
        self.prev = []

    def search_wikipeadia(self, path: str) -> None:
        if path in self.prev:
            return print("It leads to an infinite loop !")
        URL = 'https://en.wikipedia.org{page}'.format(page=path)
        try:
            res = requests.get(url=URL)
            res.raise_for_status()
        except requests.HTTPError as e:
            if (res.status_code == 404):
                return print("It's a dead end !")
            return print(e)
        soup = BeautifulSoup(res.text, 'html.parser')
        print(soup.find(id='firstHeading').text)
        content = soup.find(id='mw-content-text')
        allLinks = content.find_all('a')
        self.prev.append(path)
        for link in allLinks:
            if link['href'].startswith('/wiki/') \
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:')\
                    and not link['href'].startswith('/wiki/Category:') and not link['href'].startswith('/wiki/Template:')\
                    and not link['href'].startswith('/wiki/File:')\
                    and link.parent.name != 'b' and link.parent.name != 'strong' and link.parent.name != 'i':
                return self.search_wikipeadia(link['href'])
        if (len(self.prev) == 1):
            return print("It leads to a dead end !.")
        return print("{} roads from {} to {}".format(len(self.prev), self.prev[0], path))


def main():
    wiki = roads_to_philosophy()
    if (len(sys.argv) == 2):
        wiki.search_wikipeadia('/wiki/'+sys.argv[1])
    elif len(sys.argv) == 2:
        print('one argument required! : title')
    else:
        print('wrong argument count!')


if __name__ == '__main__':
    main()
