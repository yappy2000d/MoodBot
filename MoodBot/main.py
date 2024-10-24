import os

"""third party"""
import numpy as np
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

"""local"""
from ai import model, process, vectorizer
from youtube import comment, getid, video

SECRET = os.environ['SECRET']
TOKEN = os.environ['TOKEN']

app = Flask('')

bot = LineBotApi(TOKEN)
handler = WebhookHandler(SECRET)

@app.route('/')
def home():
    return "I'm alive"

#callback
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle(event):
    msg = event.message.text
    print(f"{event.source.user_id}, 說了{msg}")
    
    # YT留言分析
    if msg.startswith("!comment"):
        cmts = []
        id = getid(msg.split(" ")[1])
        next_page = ''
        count = int(video(id)["items"][0]["statistics"]['commentCount'])
        while count > 0:
            items, next_page = comment(id, next_page)
            item = items["items"]
            for cmt in item:
                cmts.append(cmt["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
                count -= 1
            print(cmts)

        resault = {0: 0, 1: 0}
        for i in cmts:
            inputs = [process(i)]
            vec = vectorizer.transform(inputs)
            pre = model.predict(vec)

            if pre[0] == np.int64(0):
                resault[0] += 1
            elif pre[0] == np.int64(1):
                resault[1] += 1

        info = video(id)["items"][0]
        snippet = info["snippet"]
        name = snippet["title"]
        upload_time = snippet["publishedAt"]
        channel = snippet["channelTitle"]
        statistics = info["statistics"]
        view = statistics["viewCount"]
        like = statistics.get("likeCount", 0)
        dislike = statistics.get("dislikeCount", 0)

        text = f"由：{channel}\n標題：\n{name}\n上傳於：{upload_time.split('T')[0]}\n觀看次數:{view}\n喜歡：{like}  不喜歡：{dislike}\n負面評價：{resault[0]}則，{resault[0] / len(cmts) * 100:.2f}%\n正面評價：{resault[1]}則，{resault[1] / len(cmts) * 100:.2f}%"
        bot.reply_message(event.reply_token, TextSendMessage(text=text))

    # 文字情緒分析
    elif msg.startswith("!check"):
        message = msg.split(" ")[1]
        inputs = [process(message)]
        vec = vectorizer.transform(inputs)
        pre = model.predict(vec)
        mood = {0: "負面", 1: "正面"}
        text = mood[pre[0]]
        bot.reply_message(event.reply_token, TextSendMessage(text=text))
        
    # 幫助
    elif msg == "!help":
        text = "!help                     |取得幫助\n!intro                    |介紹\n!comment {YT影片網址或ID} |影片評價\n!check   {一段文字}       |此文情緒\n輸入指令時，記得把\"{}\"去掉"
        bot.reply_message(event.reply_token, TextSendMessage(text=text))
        
    # 介紹
    elif msg == "!intro":
        text = "MoodBot 使用新浪微博之 weibo_senti_100k 資料庫，廣泛蒐集了正負向評論約各 5 萬條，並且搭載了 Multinomial Naive Bayes 機率模型做作為機器學習演算法，是一種監督式的分類演算法，對文字具有不錯的準確度（雖然說這隻得準確率 accuracy 只來到了 70%）。"
        bot.reply_message(event.reply_token, TextSendMessage(text=text))
    
    # 預設
    else:
        text = "輸入 !help 來取得幫助"
        bot.reply_message(event.reply_token, TextSendMessage(text=text))

app.run(host='0.0.0.0', port=8080)
