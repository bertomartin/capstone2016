import requests
from BeautifulSoup import  BeautifulSoup
from PyLyrics import *
import re

page = requests.get('http://www.officialcharts.com/charts/singles-chart/20160624/7501/')
source_code = page.content
soup = BeautifulSoup(source_code)

# get title of the song
list_t = soup.findAll('div',{'class':'title'})
song_list = []
for name in list_t:
	# to lowercase, delete'\n', encode str
	# change & to and for lyricswiki
	song_list.append(str(name.text.lower()).replace('\n',''))

# get artist of the song
list_a = soup.findAll('div',{'class':'artist'})
artist_list = []
for name1 in list_a:
	# delete FT, VS
	artist = re.split(' FT ',name1.text)[0]
	artist_list.append(str(artist.lower()).replace('\n',''))

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

#print #rank, artist, song, lyrics
f = open('song_lyrics.txt','w')
for i in range(100):
	f.write(str(i+1)+'\n')
	f.write(artist_list[i]+ ':' + song_list[i]+'\n')
	f.write(getLyrics(artist_list[i], song_list[i])+'\n')










