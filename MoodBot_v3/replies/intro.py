"""回覆自我介紹"""

from linebot.v3.messaging.models import (
    FlexMessage,
)

def intro() -> FlexMessage:
    """自我介紹"""
    return FlexMessage.from_dict({
        "type": "flex",
        "altText": "Intro",
        "contents": {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://obs.line-scdn.net/0hn35mbTtKMRwIFCcIiWJOSylJOn47di8XKnJ5fikdaiUtIXYkNCYtfysWPCUidyJPYHAqfkMUZ35yJHBPNDd_L31DPC4lJA/f256x256",
                "size": "3xl",
                "aspectRatio": "20:13",
                "aspectMode": "fit",
                "action": {
                    "type": "uri",
                    "uri": "https://line.me/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "MoodBot",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#ffffff"
                    },
                    {
                        "type": "text",
                        "text": "文字情緒判斷機器人",
                        "size": "sm",
                        "color": "#ffffffcc"
                    },
                    {
                        "type": "text",
                        "text": "使用了 weibo_senti_100k 資料庫，廣泛蒐集約 5 萬條正向與負向評論，並採用了 Multinomial Naive Bayes 機率模型，準確率為73.6%。",
                        "wrap": True,
                        "color": "#ffffff",
                        "margin": "lg"
                    },
                    {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#ffffff"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "message",
                                    "label": "查看功能",
                                    "text": "!help"
                                },
                                "style": "primary",
                                "color": "#ffffff1A"
                            }
                        ],
                        "backgroundColor": "#ffffff1A",
                        "cornerRadius": "lg",
                        "margin": "lg"
                    }
                ]
            },
            "styles": {
                "body": {
                    "backgroundColor": "#464F69"
                }
            }
        }
    })
