import requests
import json
import sys
import argparse
import csv
import os.path

def rumble():
    file_exists = os.path.exists('search.csv')

    if file_exists:
        header_added = True
    else:
        header_added = False

    rumble_query = str(sys.argv[1:])

    limit = "50" #change this variable to get more or less results

    rumble_url = "https://api.smat-app.com/content?term=" + rumble_query + "&limit=" + limit + "&site=rumble_video&since=2022-03-22T19%3A12%3A30.802480&until=2022-05-22T19%3A12%3A30.802480&esquery=false&sortdesc=false"

    rumble_response = requests.get(rumble_url)

    rumble_json_data = rumble_response.json()

    hits = rumble_json_data["hits"]["hits"]

    for videos in hits:
        try:
            usernames = videos["_source"]["channel_id"]
            print(" Username: " + usernames)
            authors = videos["_source"]["username"]
            print(" Author: " + authors)
            titles = videos["_source"]["metadata"]["name"]
            print(" Title: " + titles)
            urls = videos["_source"]["canonical"]
            print(" URL: " + urls + "\n")
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
