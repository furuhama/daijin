# coding:utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to("ping")
def cheer(message):
	 message.reply("PONG")

@respond_to('天気')
def weather(message):
	import urllib
	import json

	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	city_id = '130010'
	# '130010'は東京の情報

	html = urllib.request.urlopen(url+city_id)
	jsonfile = json.loads(html.read().decode('utf-8'))
	text = jsonfile['description']['text']

	message.send(text)

@respond_to("パクチー")
def hate(message):
	message.reply("ぐぬぬ")
	message.react("coriander")

@listen_to("席替え")
def todaysdesk(message):
	import yaml
	import random

	NAME_LIST_YAML = "name_list_monday.yaml"

	f = open(NAME_LIST_YAML, "r")
	name_lists = yaml.load(f)

	r = random.sample([1,2,3,4,5,6,7,8,9,10],10)
	lists = "【本日の席番号】\n"

	for (i, j) in zip(name_lists , r) :
		lists += str(i) +": "+ str(j) + " \n"

	lists += "\n\n" + """-----------------------------------------
|  shelf  |                  |  white board  |


+-----+-----+       +-----+-----+-----+
 |   1    |   2   |         |   3   |   4   |   5   |
+-----+-----+       +-----+-----+-----+
 |   6    |   7   |         |   8   |   9   |  10  |
+-----+-----+       +-----+-----+-----+

               +------------------------------
                 |        corridor  """

	message.send(lists)

@respond_to("マリカ")
def mario_cart_character(message):
	import random
	lists = list(range(0,42))
	r = random.sample(lists, 1)

	if r[0] == 0:
		emoji = "mario"
	else:
		emoji = "mario%s" % str(r[0])

	message.react(emoji)
