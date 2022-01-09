import pandas as pd
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def process(txt):
    txt = txt.replace("\r", "").replace("\n", "")
    return " ".join(jieba.cut(txt))


vectorizer = TfidfVectorizer()

df = pd.read_csv("mood.csv", encoding="utf-8-sig")
df["review"] = df["review"].apply(process)
x = df["review"]
y = df["label"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train = vectorizer.fit_transform(x_train)
model = MultinomialNB(alpha=0.001)
model.fit(x_train, y_train)
x_test = vectorizer.transform(x_test)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy: {accuracy}")
