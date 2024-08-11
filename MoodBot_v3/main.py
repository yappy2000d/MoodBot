"""MoodBot is a Line chatbot that can help you record your mood and review it later."""

import os
from typing import Literal

from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

import replies

app = Flask(__name__)

SECRET = os.environ['SECRET']
TOKEN = os.environ['TOKEN']

configuration = Configuration(access_token=TOKEN)
handler = WebhookHandler(SECRET)


@app.route("/callback", methods=['POST'])
def callback() -> Literal['OK']:
    """Line webhook callback."""
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: %s", body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event) -> None:
    """Handle message event."""
    with ApiClient(configuration) as api_client:
        print(f"{event.source.user_id}, 說了{event.message.text}")
        line_bot_api = MessagingApi(api_client)

        function = {
            '!review': replies.review,
            '!intro': replies.intro,
            '!check': replies.check,
            "!help": replies.help_msg,
        }
        command, *args = event.message.text.split(' ')

        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                replyToken=event.reply_token,
                messages=[function[command](*args)],
                notificationDisabled=False
            )
        )


if __name__ == "__main__":
    app.run()
