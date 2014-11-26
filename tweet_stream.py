import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time

ckey = ''
csecret = ''
atoken = ''
asecret = ''

class listener(StreamListener):
	def on_data(self, data):
		try:
			#print data

			# split up the data
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet

			# save the data
			saveThis = str(time.time())+'::'+tweet
			saveFile = open('twitDB2.csv','a')
			saveFile.write(saveThis)#data)
			saveFile.write('\n')
			saveFile.close()
			return True 
		except BaseException, e:
			# in case Internet is off
			print 'failed on data',str(e)
			time.sleep(5)

	def on_error(self,status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["car"])
