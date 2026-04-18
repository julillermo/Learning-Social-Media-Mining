import csv

import requests
from bs4 import BeautifulSoup as bsoup

MY_JLPT_N5_VOCAB_URL = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary"
MY_JLPT_N5_KANJI_URL = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary"
BOOK_URL = "https://en.wikipedia.org/wiki/Category:Women_computer_scientists"
# BOOK_URL = "https://github.com/julillermo"

headers = {
    "User-Agent": "MyScraper/1.0 (+https://github.com/julillermo)",
}


def scrape_book_url():
    rows = []
    women_scientists_page = requests.get(url=BOOK_URL, headers=headers)
    page_content = women_scientists_page.content

    soup = bsoup(page_content, "html.parser")
    content = soup.find("div", class_="mw-category-columns")

    if content is not None:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(content.getText())
    else:
        print("No content found on the page.")
        return

    # all_groupings = content.find_all("div", class_="mw-category-columns")

    # for grouping in all_groupings:
    #     names_list = grouping.find("ul")
    #     if not names_list:
    #         print(f"No alphabetical names found for category: {names_list}")
    #         continue

    #     category = (tag := grouping.find("h3")) and tag.get_text()

    #     for alphabetical_name in names_list.find_all("li"):
    #         anchortag = alphabetical_name.find("a", href=True)
    #         if not anchortag or "href" not in anchortag.attrs:
    #             continue

    #         name = alphabetical_name.get_text(strip=True)
    #         link = anchortag["href"]
    #         letter_name = category
    #         rows.append({"name": name, "link": link, letter_name: letter_name})


if __name__ == "__main__":
    scrape_book_url()
