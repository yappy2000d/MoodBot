"""指令幫助"""


from linebot.v3.messaging.models import (
    FlexMessage,
)


def help_msg() -> FlexMessage:
    """指令幫助"""
    return FlexMessage.from_dict({
        "type": "flex",
        "altText": "Help",
        "contents": {
            "type": "bubble",
            "size": "mega",
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
                                "text": "!help",
                                "color": "#ffffff66",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "指令幫助",
                                "color": "#ffffff",
                                "size": "xl",
                                "flex": 4,
                                "weight": "bold"
                            }
                        ]
                    }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#EA725D",
                "spacing": "md",
                "paddingTop": "22px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "指令列表",
                                "color": "#b7b7b7",
                                "size": "xs",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "指令說明",
                                "color": "#b7b7b7",
                                "size": "xs",
                                "align": "end",
                                "weight": "bold"
                            }
                        ]
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "!help",
                                "size": "sm",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "顯示指令幫助",
                                "size": "sm",
                                "align": "end"
                            }
                        ],
                        "spacing": "lg",
                        "margin": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "!intro",
                                "size": "sm",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "顯示機器人介紹",
                                "size": "sm",
                                "align": "end"
                            }
                        ],
                        "spacing": "lg",
                        "margin": "sm"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "!review <url>",
                                "size": "sm",
                                "gravity": "center",
                                "adjustMode": "shrink-to-fit",
                                "flex": 0,
                                "contents": [
                                    {
                                        "type": "span",
                                        "text": "!review ",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "span",
                                        "text": "<url>",
                                        "style": "italic"
                                    }
                                ]
                            },
                            {
                                "type": "text",
                                "text": "影片留言的正負面評價",
                                "gravity": "center",
                                "size": "sm",
                                "align": "end",
                                "wrap": True
                            }
                        ],
                        "spacing": "lg",
                        "margin": "sm"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "!check ",
                                "contents": [
                                    {
                                        "type": "span",
                                        "text": "!check ",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "span",
                                        "text": "<text>",
                                        "style": "italic"
                                    }
                                ],
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "檢查文字的正負面情緒",
                                "align": "end",
                                "flex": 0,
                                "size": "sm"
                            }
                        ],
                        "spacing": "lg",
                        "margin": "sm"
                    }
                ]
            }
        },
        "quickReply": {
            "items": [
                {
                    "type": "action",
                    "action": {
                        "type": "message",
                        "label": "指令幫助",
                        "text": "!help"
                    }
                },
                {
                    "type": "action",
                    "action": {
                        "type": "message",
                        "label": "機器人介紹",
                        "text": "!intro"
                    }
                },
                {
                    "type": "action",
                    "action": {
                        "type": "postback",
                        "label": "留言評價",
                        "data": "0",
                        "inputOption": "openKeyboard",
                        "fillInText": "!review "
                    }
                },
                {
                    "type": "action",
                    "action": {
                        "type": "postback",
                        "label": "文字情緒",
                        "data": "1",
                        "inputOption": "openKeyboard",
                        "fillInText": "!check "
                    }
                }
            ]
        }
    })
