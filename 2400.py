import mycsv
import twitter


session = twitter.connect()

status_id_2300 = mycsv.get_last_row("2300.csv")[0]
tweets = twitter.search(session, "#traP1draw", status_id_2300)

for tweet in tweets:
    twitter.retweet(session, tweet["id_str"])
    mycsv.append_row("2400.csv", [
                     tweet["created_at"],
                     tweet["id_str"],
                     tweet["user"]["username"],
                     tweet["text"]])
