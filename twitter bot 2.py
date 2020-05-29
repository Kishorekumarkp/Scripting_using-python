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
        time.sleep(30)


#generous bot
#for follower in tweepy.Cursor(api.friends).items(): # cursor collects everything in api that we give
                                                    #like followers or friends...
 #   print(follower.name)

for follower in limit_handle(tweepy.Cursor(api.friends).items()):
    if follower.name == "Polimer News": #fining a follower name and going to follow by here
        follower.unfollow()
        break