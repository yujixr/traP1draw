import os
import json

from requests_oauthlib import OAuth1Session


def connect() -> OAuth1Session:
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    return OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET,
                         ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def tweet(twitter_session: OAuth1Session, text: str) -> str:
    params = {"status": text, "trim_user": "true"}
    res = twitter_session.post(
        "https://api.twitter.com/1.1/statuses/update.json", params=params)

    if res.status_code != 200:
        return ""

    tweet = json.loads(res.text)
    return tweet["id_str"]


def search(twitter_session: OAuth1Session, query: str, since_id: str) -> list:
    params = {
        "q": query,
        "locale": "ja",
        "result_type": "recent",
        "count": 100,
        "since_id": since_id,
        "include_entities": "false"
    }
    res = twitter_session.get(
        "https://api.twitter.com/1.1/search/tweets.json", params=params)

    if res.status_code != 200:
        return []

    return json.loads(res.text)["statuses"]


def get_mentions(twitter_session: OAuth1Session, since_id: str) -> list:
    params = {
        "count": 200,
        "since_id": since_id,
        "trim_user": "true",
        "include_entities": "false"
    }
    res = twitter_session.get(
        "https://api.twitter.com/1.1/statuses/mentions_timeline.json", params=params)

    if res.status_code != 200:
        return []

    return json.loads(res.text)


def retweet(twitter_session: OAuth1Session, id: str) -> str:
    params = {"trim_user": "true"}
    res = twitter_session.post(
        f"https://api.twitter.com/1.1/statuses/retweet/{id}.json", params=params)

    if res.status_code != 200:
        return ""

    tweet = json.loads(res.text)
    return tweet["id_str"]
