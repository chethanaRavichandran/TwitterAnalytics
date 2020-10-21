import tweepy
import datetime
import time
import json

CONSUMER_KEY = 'Your consumer key'
CONSUMER_SECRET = 'Your consumer secret'
OAUTH_TOKEN = 'Your auth token'
OAUTH_TOKEN_SECRET = 'Your auth token secret '

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

# This is for searching tweets having "covid-19" that have most number of retweets
for tweet in tweepy.Cursor(api.search,q="#covid-19",count=10,result_type='popular').items(10):
    # This statement checks if the tweeted date is 5 days ago from the current date
    if (datetime.datetime.now() - tweet.created_at).days <= 5:
        # This statement is to check if the tweeted language is other than english
        if(tweet.lang!="en"):
            otherlang =(tweet.user.screen_name,tweet.retweet_count,tweet.lang)
           
            # Writing into json file
            with open('nonenglishtweets.json','w') as otherlanguage:
                json.dump(otherlang,otherlanguage)
            # Reading from json file
            with open('nonenglishtweets.json') as read:
                data = json.load(read)
                for p in data:
                    print(p,end=",")
                print(tweet.created_at)
        # This statement is for english language tweets
        else:
            eng =(tweet.user.screen_name, tweet.retweet_count)
            with open('retweets.json','w') as rt:
                json.dump(eng,rt)
            with open('retweets.json') as reade:
                data = json.load(reade)
                for p in range(0,len(data)):
                    print()
                    if(p<len(data)-1):
                        print(data[p],data[p+1])
                   
                        
                   
           
          
           
    
