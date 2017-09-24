# cording=<'utf-8'>

import json
import os
import random
import datetime
import requests
import yaml

def get_today_in_japan(DIFFERENCE):
    # herokuサーバーとの時差を修正する
    # 日本の場合は引数に 9 を入れる
    return datetime.datetime.now() + datetime.timedelta(DIFFERENCE)

def get_weekday_as_number(WEEKDAY_NUMBER):
    # (YYYY, MM, DD)の int 形式の入力を曜日に変換
    # 年、月、日を入力することで曜日を番号で取得する
    # 月曜日=0, 火曜日=1, ... 日曜日=6
    return datetime.date(WEEKDAY_NUMBER.year, WEEKDAY_NUMBER.month, WEEKDAY_NUMBER.day).weekday()

def set_namelist(FILENAME):
    # 読み込みたいyamlファイルの名前を引数にStringで受け取り、listで出力する
    f = open(FILENAME, 'r')
    name_lists = yaml.load(f)
    f.close()
    return name_lists

def set_todays_desk_number(DESK_QUANTITY):
    # デスクの数を受け取って、ランダムな順番に並び替えたlistを返す
    default_list = list(range(1, DESK_QUANTITY + 1))
    return random.sample(default_list, DESK_QUANTITY)

def combine_name_and_desk(NAMELIST, DESK_NUMBER):
    # 2つのlistを受け取ってlistをネストした構造にする

    # listの要素数が違っていないかチェックする
    if len(NAMELIST) != len(DESK_NUMBER)
        return "error! NAMELISTとDESK_NUMBERは同じ要素数にしてください!"

    NESTING_LIST = []
    for i in range(len(NAMELIST)):
        NESTING_LIST.append([NAMELIST[i], DESK_NUMBER[i])
    return NESTING_LIST

def replace_desk_number_and_set_available(NAME_DESK_LIST, NAME, PLACE):
    # セットされた名前のリストを、リモートの人の名前と仕事場所の String を受け取って、置き換えるT_DAY_IS_IT_TODAY = "本日は{}年{}月{}日{}".format())}}}}

    # 名前だけのリストを作成
    SET_NAMELIST = []
    for i in range(len(NAME_DESK_LIST)):
        SET_NAMELIST.append(NAME_DESK_LIST[i][0])

    # NAME の人が NAMELIST の何番目にあるか
    NAME_NUM = SET_NAMELIST.index(NAME)
    STORE_NUMBER = NAME_DESK_LIST[NAME_NUM][1]

    # 置き換えする
    NAME_DESK_LIST[NAME_NUM][1] = PLACE

    # 最後に空いた席を available として追加
    NAME_DESK_LIST.append(['available', STORE_NUMBER])

    return NAME_DESK_LIST

def what_day_is_it_today(DAYTIME, WEEKNUMBER):
    # 年月日と曜日に関するテキストを生成する
    WEEKNAME = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return "本日は{}年{}月{}日{}".format(DAYTIME.year, DAYTIME.month, DAYTIME.day, WEEKNAME[WEEKNUMBER])

def send_bot_message(BOT_TEXT, TARGET_URL):
    # 送りたいテキストと対象のURLを String で受け取って送信する
    payload_dic = { "text":BOT_TEXT }
    requests.post(TARGET_URL, data=json.dumps(payload_dic))

### 以下は細かいglobal変数を定義

WEEKDAY_COMMENT = "インターンは空いているところに座ろう"
HOLIDAY_COMMENY = "本日はお休みです"
OFFICE_MAP = """-----------------------------------------
|  shelf  |                  |  white board  |


+-----+-----+       +-----+-----+-----+
 |   1    |   2   |         |   3   |   4   |   5   |
+-----+-----+       +-----+-----+-----+
 |   6    |   7   |         |   8   |   9   |  10  |
+-----+-----+       +-----+-----+-----+
               +------------------------------
                 |        corridor  """

if __name__ == '__main__':
    # TODO:
    # 曜日ごとのロジックや実際の挙動を記載

