import tweepy

auth = tweepy.OAuthHandler('qloLkyjCnI1WfuVpzuHL6IKte', 'Ml1kmM6f1SRltwgvogFy9Q8uFEEtagsuDIgDXyvQWEGvjw1Xla')
auth.set_access_token('78420609-6N9Nit4Liyk1GinFHTRVu7l2kFYkzll3yq408inB0', 'eYkrmZxZgswcapzOrQcOJ6Ya0DNUn8zkm1rTKQQFRNdDT')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
print(user.screen_name)
print(user.followers_count)

def limit_handler(cursor):
    try: 
        while True: 
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500)


#Generous Bot 
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
   if follower.followers_count > 1000:
       follower.follow()
       break

