# get lyrics for each year 
# from 1942-1961, request all lyrics from all the tracks recorded
# from 1962 - 1980, randomly select 600 songs from recorded tracks
# from 1980 - 2008, randomly select 300 songs from recorded tracks

import pandas as pd
import random
import csv
import numpy as np
import re
import requests
from BeautifulSoup import BeautifulSoup
from PyLyrics import *


import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# get lyrics
# modified from PyLyrics
def getLyrics(singer, song):
	#Replace spaces with _
	#Delete multiple singers, only keep the first one
	singer = re.split('/',singer)[0]
	singer = singer.replace(' ', '_')
	song = song.replace(' ', '_')
	r = requests.get('http://lyrics.wikia.com/{0}:{1}'.format(singer,song))
	s = BeautifulSoup(r.text)
	# if has redirect class
	redirect = s.find("ul",{'class':'redirectText'})
	# if has suggested: " Did you mean..."
	suggest = s.find("span",{'class':'mw-headline'})
	if redirect is not None:
		ss = redirect.text.replace(' ','_')
		r = requests.get('http://lyrics.wikia.com/'+ss)
		s = BeautifulSoup(r.text)
	if suggest is not None:
		# has suggestion
		# delete 'did you mean' & '?'
		ss = suggest.text
		if 'Did you mean' in ss:
			ss = suggest.text.split('Did you mean')[1].split('?')[0].replace(' ','_')
			r = requests.get('http://lyrics.wikia.com/'+ss)
			s = BeautifulSoup(r.text)

    #Get main lyrics holder
	lyrics = s.find("div",{'class':'lyricbox'})
	if lyrics is None:
		#raise ValueError("Song or Singer does not exist or the API does not have Lyrics")
		return '######'
	#Remove Scripts
	[s.extract() for s in lyrics('script')]

	#Remove Comments
	comments = lyrics.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]

	#Remove unecessary tags
	for tag in ['div','i','b','a']:
		for match in lyrics.findAll(tag):
			match.replaceWithChildren()
	#Get output as a string and remove non unicode characters and replace <br> with newlines
	output = str(lyrics).encode('utf-8', errors='replace')[22:-6:].decode("utf-8").replace('\n','').replace('<br/>','\n')
	try:
		return output
	except:
		return output.encode('utf-8') 
	time.sleep(0.1)



content = pd.read_csv("xml_parse_year.csv")
df = pd.DataFrame(content)

for i in range(1960,1962):
	content_yr = df.loc[df['Year'] == i]
	# # random choose
	# random_row = content_yr.ix[np.random.choice(content_yr.index, 300)]
	# random_row.index = range(300)
	lyrics = [getLyrics(content_yr.loc[ii]['Artist'], content_yr.loc[ii]['Title']) for ii in content_yr.index]
	content_yr['Lyrics'] = pd.Series(lyrics,index = content_yr.index)
	content_yr.to_csv('song_lyrics_year{0}.csv'.format(i), sep = ',')





