# Liking the tweets according to the string that user gives
import tweepy
import time

auth = tweepy.OAuthHandler('6RI303XmMvbenX2wtrCGQtlYX',
                           'O7WcUyyWEhholxpyzoN9RiBCxt9WOKgI28562Yis59eA9Xccs8')
auth.set_access_token('1261840540619816960-D8xQT5m73Q6Q31FWxGdk5x61YiJeZq' , 'uVkAHkxztAZmhTqcGQN0AwLib0CflXaIJ1j04TOhgzgvd')

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'python'
numberoftweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numberoftweets): #search the tweets
    try:
        tweet.favorite()    # this favorite() makes likes in the profile acc to numbers in items(n)
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break