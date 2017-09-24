# -*- coding: utf-8 -*-

import json
import os
import random
import datetime
import requests
import yaml

def get_today_datetime(difference):
    # herokuサーバーとの時差を修正する
    # 日本の場合は引数に 9 を入れる
    return datetime.datetime.now() + datetime.timedelta(hours = difference)

def get_weekday_as_number(date):
    # (YYYY, MM, DD)の int 形式の入力を曜日に変換
    # 年、月、日を入力することで曜日を番号で取得する
    # 月曜日=0, 火曜日=1, ... 日曜日=6
    return datetime.date(date.year, date.month, date.day).weekday()

def set_namelist(filename):
    # 読み込みたいyamlファイルの名前を引数にStringで受け取り、listで出力する
    f = open(filename, 'r')
    name_lists = yaml.load(f)
    f.close()
    return name_lists

def set_todays_desk_number(desk_quantity):
    # デスクの数を受け取って、ランダムな順番に並び替えたlistを返す
    default_list = list(range(1, desk_quantity + 1))
    return random.sample(default_list, desk_quantity)

def combine_name_and_desk(namelist, desk_number):
    # 2つのlistを受け取ってlistをネストした構造にする

    # listの要素数が違っていないかチェックする
    if len(namelist) != len(desk_number):
        return "error! namelistとdesk_numberは同じ要素数にしてください!"

    NESTING_LIST = []
    for i in range(len(namelist)):
        NESTING_LIST.append([namelist[i], desk_number[i]])
    return NESTING_LIST

def replace_desk_number(name_desk_list, name, place):
    # セットされた名前のリストを、リモートの人の名前と仕事場所の String を受け取って、置き換える

    # 名前だけのリストを作成
    SET_NAMELIST = []
    for i in range(len(name_desk_list)):
        SET_NAMELIST.append(name_desk_list[i][0])

    # NAME の人が NAMELIST の何番目にあるか
    NAME_NUM = SET_NAMELIST.index(name)
    STORE_NUMBER = name_desk_list[NAME_NUM][1]

    # 置き換えする
    name_desk_list[NAME_NUM][1] =place

    # 最後に空いた席を available として追加
    name_desk_list.append(['available', STORE_NUMBER])

    return name_desk_list

def what_day_is_it_today(daytime_arg, weeknumber):
    # 年月日と曜日に関するテキストを生成する
    WEEKNAME = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return "本日は{}年{}月{}日{}".format(daytime_arg.year, daytime_arg.month, daytime_arg.day, WEEKNAME[weeknumber])

def send_bot_message(bot_text, target_url):
    # 送りたいテキストと対象のURLを String で受け取って送信する
    payload_dic = { "text": bot_text }
    requests.post(target_url, data=json.dumps(payload_dic))

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

# if __name__ == '__main__':
# TODO:
# 曜日ごとのロジックや実際の挙動を記載
