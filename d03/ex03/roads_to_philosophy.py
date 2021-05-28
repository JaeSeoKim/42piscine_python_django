#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup


class roads_to_philosophy:
    def __init__(self) -> None:
        self.prev = []

    def search_wikipeadia(self, path: str) -> None:
        URL = 'https://en.wikipedia.org{page}'.format(page=path)
        try:
            res = requests.get(url=URL)
            res.raise_for_status()
        except requests.HTTPError as e:
            if (res.status_code == 404):
                return print("It's a dead end !")
            return print(e)
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find(id='firstHeading').text
        if title in self.prev:
            return print("It leads to an infinite loop !")
        self.prev.append(title)
        print(title)
        if title == 'Philosophy':
            return print("{} roads from {} to Philosophy".format(len(self.prev), self.prev[0] if len(self.prev) > 0 else 'Philosophy'))
        content = soup.find(id='mw-content-text')
        allLinks = content.select('p > a')
        for link in allLinks:
            if link.get('href') is not None and link['href'].startswith('/wiki/')\
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                return self.search_wikipeadia(link['href'])
        return print("It leads to a dead end !.")


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
