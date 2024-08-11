"""查看文字情緒"""
from linebot.v3.messaging.models import (
    TextMessage,
)
from core.ai import process, vectorizer, model

def check(*texts) -> TextMessage:
    """Check the sentiment of the text."""
    message = " ".join(texts)
    inputs = [process(message)]
    vec = vectorizer.transform(inputs)
    pre = model.predict(vec)
    mood = {0: "負面", 1: "正面"}
    result = mood[pre[0]]
    return TextMessage.from_dict({"type": "text", "text": result})
