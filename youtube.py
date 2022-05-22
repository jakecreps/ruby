import requests
import json
import sys
import argparse
import csv
import os.path

file_exists = os.path.exists('search.csv')

if file_exists:
    header_added = True
else:
    header_added = False

query = str(sys.argv[1:])

url = "http://youtube-scrape.herokuapp.com/api/search?q=" + query + "&page=1"

response = requests.get(url)

data = response.json()

data = data["results"]

for videos in data:
    try:
        authors = videos["uploader"]["username"]
        titles = videos["video"]["title"]
        urls = videos["video"]["url"]
        author_urls = videos["uploader"]["url"]
    except:
        pass

    with open('search.csv', 'a') as csvfile:
        fieldnames = ['author', 'usernames', 'title', 'author_url', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not header_added:
            writer.writeheader()
            header_added = True
        writer.writerow({'author': authors, 'usernames': '', 'title': titles, 'author_url': author_urls, 'url': urls})
