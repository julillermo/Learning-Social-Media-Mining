import csv
import json

import requests


def main():
    print("Hello from ch3!")


def url_based_API_call():
    # Creating API call from URL
    api_url = "https://www.googleapis.com/youtube/v3/search?part=\
            snippet&channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&key=YOUTUBE_APP_KEY"
    api_response = requests.get(api_url)
    videos = json.loads(api_response.text)

    # Storing Data in a Spreadsheet
    with open("youtube_videos.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["publishedAt", "title", "description", "thumbnailurl"])

    # converting JSON into a Python Dictionary


if __name__ == "__main__":
    main()
