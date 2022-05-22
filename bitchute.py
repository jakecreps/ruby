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

smat_query = str(sys.argv[1:])

smat_url = "https://api.smat-app.com/content?term=" + smat_query + "&limit=20&site=bitchute_video&since=2022-03-22T19%3A12%3A30.802480&until=2022-05-22T19%3A12%3A30.802480&esquery=false&sortdesc=false"

smat_response = requests.get(smat_url)

smat_json_data = smat_response.json()

hits = smat_json_data["hits"]["hits"]

for videos in hits:
    try:
        usernames = videos["_source"]["meta"]["channel_id"]
        authors = videos["_source"]["channel"]
        urls = videos["_source"]["canonical"]
        titles = videos["_source"]["title"]
    except:
        pass

    try:
        with open('search.csv', 'a') as csvfile:
            fieldnames = ['author', 'usernames', 'title', 'author_url', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not header_added:
                writer.writeheader()
                header_added = True
            writer.writerow({'author': authors, 'usernames': usernames, 'title': titles, 'author_url': '', 'url': urls})
    except:
        pass
