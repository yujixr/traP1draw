import mycsv
import twitter

text = "スタートです！\n"\
    "#traP1draw"

session = twitter.connect()
id = twitter.tweet(session, text)

mycsv.append_row("2300.csv", [id])
