import random
from datetime import datetime

import mycsv
import twitter

session = twitter.connect()

status_id_1200 = mycsv.get_last_row("1200.csv")[1]
mentions = twitter.get_mentions(session, status_id_1200)

themes = []
for mention in mentions:
    if mention["in_reply_to_status_id_str"] == status_id_1200:
        # [10:] means that we need to remove username, "@traP1draw"
        theme = mention["text"][10:]
        themes.append(theme)

themes_chosen = [themes[i] for i in random.sample(range(len(themes)), k=3)]

text = "本日のワンドロのお題は、\n"\
    f"① {themes_chosen[0]}\n"\
    f"② {themes_chosen[1]}\n"\
    f"③ {themes_chosen[2]}\n"\
    "の３つです。\n"\
    "どれか１つ以上のお題に沿って作品を作って下さい。\n"\
    "できた作品には #traP1draw のタグを付けて投稿しましょう！"

id = twitter.tweet(session, text)

mycsv.append_row("2200.csv",  [datetime.now(), themes_chosen[0],
                 themes_chosen[1], themes_chosen[2], id])
