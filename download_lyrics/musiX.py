from urllib2 import urlopen, HTTPError
from json import load
import json

baseURL = 'http://api.musixmatch.com/ws/1.1/'
api = 'apikey=848c3251fff94bb1586efba5a399d18a'
# get the lyrics for thr track id 15953433
getlyrics = 'track.lyrics.get?track_id=15953433'

request = baseURL + getlyrics + '&' + api
response = urlopen(request)
baseData = load(response)
#print baseData['message']['body']['lyrics']

# write return json file
with open('musiXlyrics.json','w') as outfile:
	json.dump(baseData, outfile)

# parsing the json, convert to csv
body = baseData['message']['body']['lyrics']
f = open('lyric.txt','w')
for part in body:
	f.write(part+': ')
	f.write(str(body[part])+'\n')
