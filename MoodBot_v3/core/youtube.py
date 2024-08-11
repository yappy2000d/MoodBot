"""Youtube API."""

import os
from urllib.parse import parse_qs, urlparse

import requests

KEY = os.environ['KEY']


def getid(url):
    """Get youtube video id from url."""
    if url.startswith("http"):

        if "youtu.be" in url:
            # https://www.youtu.be/ZuQgsTcuM4g?feature=shared
            return url.split("/")[-1].split("?")[0]

        try:
            # https://www.youtube.com/watch?v=ZuQgsTcuM4g
            url_data = urlparse(url)
            query = parse_qs(url_data.query)
            return query["v"][0]

        except KeyError:
            return url.split("/")[-1]
    else:
        return url


def video(video_id):
    """Get video information from youtube video id."""
    url = "https://youtube.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,contentDetails,statistics",
        "id": video_id,
        "key": KEY
    }
    res = requests.get(url, params=params, timeout=5)
    return res.json()


def comment(video_id, page_token=''):
    """Get comments of a youtube video."""
    url = "https://youtube.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet,replies",
        "videoId": video_id,
        "next_page_token": page_token,
        "key": KEY
    }
    res = requests.get(url, params=params, timeout=5)
    return res.json(), res.json().get("nextPageToken", "")
