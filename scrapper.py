import bs4
import requests


class Scrapper:
    def _init_bs(self, source) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(source, features="html.parser")

    def get_list_of_repos(self, tag: str, range_from: int = 1, range_to: int = 10) -> list[str]:
        repos = []
        for page in range(range_from, range_to + 1):
            source = requests.get(f'https://github.com/topics/{tag}?l=python&o=asc&s=stars&page={page}').content
            soup = self._init_bs(source)
            elems = soup.findAll('h3', attrs={'class': 'f3 color-fg-muted text-normal lh-condensed'})
            repos.extend(''.join(a.text.strip() for a in elem) for elem in elems)
        return repos

