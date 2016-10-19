# this program scrapes web data based on the songs and titles list from 'filename'

from BeautifulSoup import BeautifulSoup
from PyLyrics import *
import re
import time
import csv

for i in range(515,516):
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

	# print artist, song, lyrics
	length = len(artist_list)
	# write in csv
	with open('song_lyrics_filename{0}.csv'.format(i),'w') as outputFile:
		writer = csv.writer(outputFile,delimiter=',')
		writer.writerow(['Artist','Title', 'Track_id','Year','Lyrics'])

		for i in range(length):
			artist = artist_list[i]
			title = title_list[i]
			track_id = id_list[i]
			year = yr_list[i]
			lyrics = getLyrics(artist_list[i], title_list[i]) 
			writer.writerow([artist,title,track_id,year,lyrics])

	"""for i in range(length):
					f.write(str(i+1)+'\n')
					f.write(artist_list[i] + ':' + title_list[i] + '\n')
					f.write(getLyrics(artist_list[i], title_list[i]) + '\n')"""
	

