# MoodBot

一個基於Naive Bayes classifier的文字情緒辨識LINE機器人，高中二年級時的自主學習計畫。



2024年升級linebot至v3，也將回應訊息改為Flex Message美化。

## Features

+ 判斷文字情緒
+ 統計YouTube影片的留言評價

## Screenshots

![intro](MoodBot_v3/imgs/intro.png)


![review](MoodBot_v3/imgs/review.png)

## Tech Stack

Bot: [pallets/flask](https://github.com/pallets/flask), [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

AI: [fxsjy/jieba](https://github.com/fxsjy/jieba), [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)

Crawler: [psf/requests](https://github.com/psf/requests), [YouTube Data API v3](https://console.cloud.google.com/apis/api/youtube.googleapis.com/)

## Environment Variables

To run this project, you will need to add the following environment variables

```
KEY="Google Cloud API key for YouTube API"
TOKEN="Channel access token for LINE Messaging API"
SECRET="Channel secret for LINE Messaging API"
```

## Requirements(Tested)

Python: 3.10

```
flask==3.0.3
jieba==0.42.1
joblib==1.4.0
line-bot-sdk==3.11.0
numpy==1.26.4
pandas==2.2.2
requests==2.31.0
scikit-learn==1.2.2
```

#### v3

Python: 3.12.1、3.11.9

```
flask==3.0.3
jieba==0.42.1
joblib==1.4.2
line-bot-sdk==3.11.0
numpy==2.0.1
requests==2.31.0
scikit-learn==1.5.1
```

## Deploy
### LINE Setting
1. Go to [LINE Developers](https://developers.line.biz/)
2. Create a new "Provider" or click an existing provider
3. In the "Channels" tab, create a new channel with "Messaging API" type
4. Fill in the relevant information

Now you can find your Channel secret in the "Basic settings" tab.

In the 'Messaging API' tab, you will find the 'Bot Basic ID' for adding your bot friend later. Then scroll down, modify the 'Webhook URL,' and check the 'Use webhook' option. At the page bottom, issue a 'Channel access token.'  

Last of all, disable "Auto Response" at [LINE Official Account Manager](https://manager.line.biz/).

### YouTube Data API v3
Omit

### Webhook Server
Showcase with cPanel: [Chinese](deploy_on_cpanel.md)
