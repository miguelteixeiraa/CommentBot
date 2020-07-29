# RugratsBot


An Instagram bot that automates follow and comments (tagging people too).

```shell
# 1. install pip
sudo apt install python3-pip
# 2. install requestium
pip3 install requestium
# 3. Download https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.we38/
# 4. Put it extracted in the folder of this project
# 5. run
python3 bot_main.py
````

**Example:**

```python
from rugrats_bot import RugratsBot


# creating our baby rugrat
rugratBot = RugratsBot()
rugratBot.setLoginInfo("Your instagram username", "Your instagram password")

listOfComments = [
    # your string list of possible comments here
]
rugratBot.setListOfComments(listOfComments)

# url of publication to send comments
rugratBot.setInstagramPageUrl("https://www.instagram.com/TargetUrl")

# now, just watch our baby rugrat having fun with your instagram account
rugratBot.startCommenting()
```

## Instagram limits:
**Accounts older than one year (recommended to not have limited functions by instagram)**
 1. 10 - 15 comments per hour
 2. 600 - 1000 likes a day
 3. 60 - 80 new DMs
 4. 2200 characters in a post or comment (max recommended)
 5. 5 hashtags in a post or comment (max recommended)


Make your own luck on instagram promotions :)



It will be completely written one day
