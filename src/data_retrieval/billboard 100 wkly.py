# getting weekly hint 100 songs' artists and titles form billboard
import requests
import re
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
h = HTMLParser()
import time
from datetime import date, timedelta
import pandas as pd

# website prefix
web = 'http://www.billboard.com/charts/hot-100/'
# start date
start = date(2016,1,2)
# time in week period
period = timedelta(days = 7)
# set up today
today = date.today()
# generate week's date list
week_of = start
week_of_list = []
while True:
	week_of_list.append(str(week_of))
	week_of = week_of + period
	if week_of > today:
		break

# open txt to write
f = open('wkly100.txt','w')

# get 100 songs for each week and write them in the txt
def getwk100(time):
	page = requests.get(web + time)
	source_code = page.content
	soup = BeautifulSoup(source_code)
	# get title of the song
	list_title = soup.findAll('h2', {'class':'chart-row__song'})
	title_list = []
	for name in list_title:
		title_list.append(h.unescape(name.text.encode('utf-8')))
	# get artist of the song
	list_artist = soup.findAll(['a', 'h3'], {'class': 'chart-row__artist'})
	artist_list = []
	for name1 in list_artist:
		artist_list.append(h.unescape(name1.text.encode('utf-8')))
	for rank in range(100):
		f.write(artist_list[rank] + ':' + title_list[rank] + ',' + str(rank + 1) + '\n')

#write all wks in txt
for i in week_of_list:
	f.write('week of ' + str(i) + '\n')
	getwk100(i)
