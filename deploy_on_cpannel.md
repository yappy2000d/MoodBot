# 於cPanel上佈署

1. 於cPanel面板的「Tools」 > 「檔案」上找到「檔案管理員」

2. 新增一個資料夾，名稱為「MoodBot」

3. 上傳相關檔案，結構如下所示：

   ```
   /
   ├── (略)
   ├── mail
   └── MoodBot
       ├── core
       │   ├── ai.py
       │   └── youtube.py
       ├── data.csv
       ├── main.py
       ├── model.pkl
       ├── replies
       │   ├── __init__.py
       │   ├── check.py
       │   ├── help.py
       │   ├── intro.py
       │   └── review.py
       ├── requirements.txt
       └── vectorizer.pkl
   ```

4. 於cPanel面板的「Tools」 > 「軟體」上找到「Setup Python App」

5. 點擊右上方的「CREATE APPLICATION」

6. 選擇Python版本: 3.11.9

7. Application root: `MoodBot`

8. URL: `moodbot`

9. Application URL: `passenger_wsgi.py`

10. Application Entry point: `main`

11. Passenger log file: `logs/passenger.log`

12. 新增Environment variables: `KEY`, `TOKEN` , `SECRET`

13. 點擊「Save」保存

14. 在Configuration files那邊輸入`requirements.txt`後按「Add」

15. 按「Run Pip Install」

16. 回到「檔案管理員」上傳`passenger_wsgi.py`（與`main.py`同級）

    ```python
    import os
    import sys
    
    sys.path.insert(0, os.path.dirname(__file__))
    
    from main import app as application
    ```

現在LINE Messaging API的Webhook URL為`https://<your domain>/moodbot/callback`，