# coding=<'utf-8'>

import json
import os
import random
import datetime
import requests
import yaml

def desk(WEEKDAY_NUMBER):

    # 月曜日
    if WEEKDAY_NUMBER == 0:
        NAME_LIST_YAML = 'name_list_monday.yaml'
        f = open(NAME_LIST_YAML, 'r')
        name_lists = yaml.load(f)
        f.close()
        r = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        SEKIGAE = '本日は{}年{}月{}日'.format(TODAY_NOW.year, TODAY_NOW.month, TODAY_NOW.day) + str(WEEKNAME[WEEKDAY_NUMBER]) + '\n【本日の席番号】\n'

        for (i, j) in zip(name_lists, r):
            SEKIGAE += str(i) +": "+ str(j) + " \n"

        SEKIGAE += "\n\n" + "インターンは適当に空いてるとこに座ろう" + "\n\n" + """-----------------------------------------
|  shelf  |                  |  white board  |


+-----+-----+       +-----+-----+-----+
 |   1    |   2   |         |   3   |   4   |   5   |
+-----+-----+       +-----+-----+-----+
 |   6    |   7   |         |   8   |   9   |  10  |
+-----+-----+       +-----+-----+-----+
               +------------------------------
                 |        corridor  """

        return SEKIGAE

    # 火曜日、水曜日
    if WEEKDAY_NUMBER == 1 or WEEKDAY_NUMBER == 2:
        NAME_LIST_YAML = 'name_list_monday.yaml'
        f = open(NAME_LIST_YAML, 'r')
        name_lists = yaml.load(f)
        f.close()
        r = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        SEKIGAE = '本日は{}年{}月{}日'.format(TODAY_NOW.year, TODAY_NOW.month, TODAY_NOW.day) + str(WEEKNAME[WEEKDAY_NUMBER]) + '\n【本日の席番号】\n'

        # name_list_monday.yamlから'is8r'を検索し、一旦保存、そしてそのindexに対応するrの値を:house_with_garden:に
        num_for_none = r[name_lists.index('is8r')]
        r[name_lists.index('is8r')] = ':house_with_garden:'

        for (i, j) in zip(name_lists, r):
            SEKIGAE += str(i) +": "+ str(j) + " \n"

        SEKIGAE += "available: " + str(num_for_none) + " \n"
        SEKIGAE += "\n\n" + "インターンは適当に空いてるとこに座ろう" + "\n\n" + """-----------------------------------------
|  shelf  |                  |  white board  |


+-----+-----+       +-----+-----+-----+
 |   1    |   2   |         |   3   |   4   |   5   |
+-----+-----+       +-----+-----+-----+
 |   6    |   7   |         |   8   |   9   |  10  |
+-----+-----+       +-----+-----+-----+
               +------------------------------
                 |        corridor  """

        return SEKIGAE

    # 木曜日
    if WEEKDAY_NUMBER == 3:
        NAME_LIST_YAML = 'name_list_normal.yaml'
        f = open(NAME_LIST_YAML, 'r')
        name_lists = yaml.load(f)
        f.close()
        r = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        SEKIGAE = '本日は{}年{}月{}日'.format(TODAY_NOW.year, TODAY_NOW.month, TODAY_NOW.day) + str(WEEKNAME[WEEKDAY_NUMBER]) + '\n【本日の席番号】\n'

        for (i, j) in zip(name_lists, r):
            SEKIGAE += str(i) +": "+ str(j) + " \n"

        SEKIGAE += "\n\n" + "インターンは適当に空いてるとこに座ろう" + "\n\n" + """-----------------------------------------
|  shelf  |                  |  white board  |


+-----+-----+       +-----+-----+-----+
 |   1    |   2   |         |   3   |   4   |   5   |
+-----+-----+       +-----+-----+-----+
 |   6    |   7   |         |   8   |   9   |  10  |
+-----+-----+       +-----+-----+-----+
               +------------------------------
                 |        corridor  """

        return SEKIGAE

    # 金曜日
    if WEEKDAY_NUMBER == 4:
        NAME_LIST_YAML = 'name_list_normal.yaml'
        f = open(NAME_LIST_YAML, 'r')
        name_lists = yaml.load(f)
        f.close()
        r = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        SEKIGAE = '本日は{}年{}月{}日'.format(TODAY_NOW.year, TODAY_NOW.month, TODAY_NOW.day) + str(WEEKNAME[WEEKDAY_NUMBER]) + '\n【本日の席番号】\n'

        # name_list_normal.yamlから'eruma'と'shinofara'を検索し、その値を一旦保存、そしてそのindexに対応するrの値を:tamachi:に
        num_for_none_1 = r[name_lists.index('eruma')]
        num_for_none_2 = r[name_lists.index('shinofara')]

        r[name_lists.index('eruma')] = ':tamachi:'
        r[name_lists.index('shinofara')] = ':tamachi:'

        for (i, j) in zip(name_lists, r):
            SEKIGAE += str(i) + ": " + str(j) + " \n"

        SEKIGAE += "available: " + str(num_for_none_1) + " \n"
        SEKIGAE += "available: " + str(num_for_none_2) + " \n"
        SEKIGAE += "\n\n" + "インターンは適当に空いてるとこに座ろう" + "\n\n" + """-----------------------------------------
|  shelf  |                  |  white board  |


+-----+-----+       +-----+-----+-----+
 |   1    |   2   |         |   3   |   4   |   5   |
+-----+-----+       +-----+-----+-----+
 |   6    |   7   |         |   8   |   9   |  10  |
+-----+-----+       +-----+-----+-----+
               +------------------------------
                 |        corridor  """

        return SEKIGAE

    # 土曜日、日曜日
    if WEEKDAY_NUMBER == 5 or WEEKDAY_NUMBER == 6:
        SEKIGAE = '本日は{}年{}月{}日'.format(TODAY_NOW.year, TODAY_NOW.month, TODAY_NOW.day) + str(WEEKNAME[WEEKDAY_NUMBER]) + '\n\n本日はお休みです。'

        return SEKIGAE

if __name__ == '__main__':
    SLACK_URL = os.getenv("SLACK_URL")

    TODAY_NOW = datetime.datetime.now() + datetime.timedelta(hours=9)
    # herokuはUTCなのでJSTにするために9時間足す

    WEEKDAY_NUMBER = datetime.date(TODAY_NOW.year, TODAY_NOW.month, TODAY_NOW.day).weekday()

    WEEKNAME = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

    bot_text = desk(WEEKDAY_NUMBER)

    payload_dic = { "text":bot_text }

    requests.post(SLACK_URL, data=json.dumps(payload_dic))
