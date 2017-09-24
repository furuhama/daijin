# -*- coding: utf-8 -*-

# In[ ]:

default_reply = "Hello world!"

import os
# heroku の環境変数でAPI_TOKENを取得
API_TOKEN = os.getenv("API_TOKEN")

PLUGINS = [
    'plugins',
]
