import csv

import requests
from bs4 import BeautifulSoup as bsoup

MY_JLPT_N5_VOCAB_URL = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary"
MY_JLPT_N5_KANJI_URL = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary"
BOOK_URL = "https://en.wikipedia.org/wiki/Category:Women_computer_scientists"


def scrape_book_url():
    rows = []
    women_scientists_page = requests.get(BOOK_URL)
    page_content = women_scientists_page.content

    soup = bsoup(page_content, "html.parser")


if __name__ == "__main__":
    scrape_book_url()
