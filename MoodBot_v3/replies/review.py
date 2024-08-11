"""YT留言分析"""

from linebot.v3.messaging.models import (
    FlexMessage,
)
import numpy as np

from core.youtube import getid, video, comment
from core.ai import process, vectorizer, model


def review(url: str) -> FlexMessage:
    """YT留言分析"""
    comments = []
    video_id = getid(url)
    next_page = ''

    count = int(video(video_id)["items"][0]["statistics"]['commentCount'])
    while count > 0:
        items, next_page = comment(video_id, next_page)
        item = items["items"]
        for cmt in item:
            comments.append(cmt["snippet"]["topLevelComment"]
                            ["snippet"]["textOriginal"])
            count -= 1
        # print(comments)

    result = {0: 0, 1: 0}
    for i in comments:
        inputs = [process(i)]
        vec = vectorizer.transform(inputs)
        pre = model.predict(vec)

        if pre[0] == np.int64(0):
            result[0] += 1
        elif pre[0] == np.int64(1):
            result[1] += 1

    info = video(video_id)["items"][0]
    snippet = info["snippet"]
    name = snippet["title"]
    upload_time = snippet["publishedAt"]
    channel = snippet["channelTitle"]
    statistics = info["statistics"]
    view = statistics["viewCount"]
    like = statistics.get("likeCount", 0)
    dislike = statistics.get("dislikeCount", 0)

    return FlexMessage.from_dict({
        "type": "flex",
        "altText": "Review",
        "contents": {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "!review",
                                "color": "#ffffff66",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "留言評價",
                                "color": "#ffffff",
                                "size": "xl",
                                "flex": 4,
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": f"{round(result[1] / len(comments) * 100)}%",
                                "margin": "lg",
                                "size": "xs",
                                "color": "#ffffff",
                                "align": "start",
                                "gravity": "center"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "backgroundColor": "#0D8186",
                                        "height": "6px",
                                        "width": f"{result[1] / len(comments) * 100:.2f}%"
                                    }
                                ],
                                "margin": "sm",
                                "height": "6px",
                                "backgroundColor": "#9FD8E36E"
                            }
                        ]
                    }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#27ACB2",
                "spacing": "md",
                "paddingTop": "22px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "影片標題",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": name,
                        "margin": "md",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": channel,
                        "color": "#aaaaaa",
                        "size": "xs",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "上傳時間",
                                        "color": "#555555",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": upload_time.split('T')[0],
                                        "color": "#111111",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ],
                                "spacing": "sm",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "觀看次數",
                                        "color": "#555555",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": view,
                                        "color": "#111111",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ],
                                "spacing": "sm",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "喜歡",
                                        "color": "#555555",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": str(like),
                                        "color": "#111111",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ],
                                "spacing": "sm",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "不喜歡",
                                        "color": "#555555",
                                        "size": "sm",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": str(dislike),
                                        "color": "#111111",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                ],
                                "spacing": "sm",
                                "margin": "xxl"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "正面評價",
                                "color": "#555555",
                                "size": "sm",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": f"{result[1]}則",
                                "color": "#111111",
                                "size": "sm",
                                "align": "end"
                            }
                        ],
                        "spacing": "sm",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "負面評價",
                                "color": "#555555",
                                "size": "sm",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": f"{result[0]}則",
                                "color": "#111111",
                                "size": "sm",
                                "align": "end"
                            }
                        ],
                        "spacing": "sm",
                        "margin": "xxl"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Video ID",
                                "flex": 0,
                                "size": "xs",
                                "color": "#aaaaaa"
                            },
                            {
                                "type": "text",
                                "text": video_id,
                                "color": "#aaaaaa",
                                "size": "xs",
                                "align": "end"
                            }
                        ],
                        "margin": "md"
                    }
                ]
            }
        }
    })
