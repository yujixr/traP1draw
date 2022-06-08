from datetime import datetime

import mycsv
import twitter

text = "本日23:00からtraP1drawを実施します！\n"\
    "今からお題を募集するので、このツイートにリプライで送ってください！\n"\
    "traP1drawの参加の可否は問わないので気軽にお願いします！\n"\
    "お題は募集した中から3つ選ばれ、開始1時間前の22:00に発表されます。\n"\
    "#traP1draw"

session = twitter.connect()
id = twitter.tweet(session, text)

mycsv.append_row("1200.csv", [datetime.now(), id])
