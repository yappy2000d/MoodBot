import os

KEY = os.environ['KEY']

from urllib.parse import parse_qs, urlparse

import requests


def getid(url):
    if url.startswith("http"):
        try:
            url_data = urlparse(url)
            query = parse_qs(url_data.query)
            return query["v"][0]
        except KeyError:
            return url.split("/")[-1]
    else:
        return url


def video(id):
    url = "https://youtube.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": id,
        "key": KEY
    }
    res = requests.get(url, params=params)
    return res.json()


def comment(id, page_token=''):
    url = "https://youtube.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet,replies",
        "videoId": id,
        "next_page_token": page_token,
        "key": KEY
    }
    res = requests.get(url, params=params)
    return res.json(), res.json().get("nextPageToken", "")
