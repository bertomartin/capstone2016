# this program parse the xml file to one scv
# with the column artist,title,track_id,year


from BeautifulSoup import BeautifulSoup
from PyLyrics import *
import re
import time
import csv

with open('xml_parse_year.csv','w') as outputFile:
	writer = csv.writer(outputFile,delimiter=',')
	writer.writerow(['Artist','Title', 'Track_id','Year','Lyrics'])

	for i in range(0,470):
		filename = 'filename_{0}.xml'.format(i)
		f = open(filename)
		doc = f.readlines()
		soup = BeautifulSoup(doc[0])
		# find titles
		list_title = soup.findAll('title')
		title_list = []
		for title in list_title:
			title_list.append(str(title.text))

		# find artists
		list_artist = soup.findAll('artist_name')
		artist_list = []
		for artist in list_artist:
			artist_list.append(str(artist.text))

		# find track_id
		list_id = soup.findAll('track_id')
		id_list = []
		for idnum in list_id:
			id_list.append(str(idnum.text))

		# find year
		list_yr = soup.findAll('year')
		yr_list = []
		for yr in list_yr:
			yr_list.append(str(yr.text))

		import sys
		reload(sys)
		sys.setdefaultencoding("utf-8")

		# write in csv
		length = len(artist_list)

		for i in range(length):
			artist = artist_list[i]
			title = title_list[i]
			track_id = id_list[i]
			year = yr_list[i]
			writer.writerow([artist,title,track_id,year])
			










