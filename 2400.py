from datetime import datetime

import mycsv
import twitter

session = twitter.connect()

status_id_2300 = mycsv.get_last_row("2300.csv")[1]
tweets = twitter.search(session, "#traP1draw", status_id_2300)

for tweet in tweets:
    if "entities" in tweet and "urls" in tweet["entities"] and len(tweet["entities"]["urls"]) >= 1:
        twitter.retweet(session, tweet["id_str"])
        mycsv.append_row("2400.csv", [
            datetime.now(),
            tweet["created_at"],
            tweet["id_str"],
            tweet["user"]["screen_name"],
            tweet["user"]["name"],
            tweet["text"]
        ])
