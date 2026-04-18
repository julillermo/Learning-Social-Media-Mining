import json
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bsoup

MY_JLPT_N5_VOCAB_URL = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary"
MY_JLPT_N5_KANJI_URL = "https://en.wikibooks.org/wiki/JLPT_Guide/JLPT_N5_Vocabulary"
BOOK_URL = "https://en.wikipedia.org/wiki/Category:Women_computer_scientists"

SCRAPER_HEADER = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0",
    "from": "https://github.com/julillermo",
}

WOMEN_SCIENTISTS_PATH = "./output/women-scientists.html"
OUTPUT_PATH = "./output/output.json"


def generate_files(filepaths: list[str]) -> None:
    for filepath in filepaths:
        path = Path(filepath)
        path.touch(exist_ok=True)


def file_exists(filepath: str) -> bool:
    return Path(filepath).exists()


def scrape_book_url():
    time.sleep(2)

    rows = []
    women_sci_file_exists = file_exists(WOMEN_SCIENTISTS_PATH)

    if women_sci_file_exists:
        woman_scientists_page_content = requests.get(
            url=BOOK_URL, headers=SCRAPER_HEADER
        ).content
    else:
        with open(
            file="./output/women-scientists.html", mode="r", encoding="utf-8"
        ) as file:
            woman_scientists_page_content = file.read()

    soup = bsoup(woman_scientists_page_content, "html.parser")
    content = soup.find("div", class_="mw-category-columns")

    if content is None:
        print("No content found on the page.")
        return

    if not women_sci_file_exists:
        with open("./output/woman-scientists.html", "w", encoding="utf-8") as file:
            file.write(str(content.prettify()))

    all_groupings = content.find_all("div", class_="mw-category-group")

    for grouping in all_groupings:
        names_list = grouping.find("ul")

        if not names_list:
            print(f"No alphabetical names found for category: {names_list}")
            continue

        category = (tag := grouping.find("h3")) and tag.get_text().strip()

        for alphabetical_name in names_list.find_all("li"):
            anchortag = alphabetical_name.find("a", href=True)

            if not anchortag or "href" not in anchortag.attrs:
                continue

            name = alphabetical_name.get_text(strip=True)
            link = anchortag["href"]
            letter_name = category
            rows.append({"name": name, "link": link, "letter_name": letter_name})

    with open("./output/output.json", "w", encoding="utf-8") as file:
        # file.write(str(rows))
        json.dump(rows, file, indent=2)


if __name__ == "__main__":
    generate_files([OUTPUT_PATH, WOMEN_SCIENTISTS_PATH])
    scrape_book_url()
    print("script completed")
