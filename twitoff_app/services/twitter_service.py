# Access Twitter dev info

# Imports
import tweepy
import os
from dotenv import load_dotenv

# Load in credentials
load_dotenv()

# Credentials - currently using professors, needs to update to my own
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Set authorization to twitter develop
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print('AUTH', auth)

# Set api
api = tweepy.API(auth)
print('API', api)


if __name__ == "__main__":

    ## Get information about a specific user

    # Creates object of specific user
    user = api.get_user('s2t2')

    # Print info about user
    # print(user.id)
    # print(user.screen_name)
    # print(user.followers_count)

    ## Getting tweets from the twitter api

    # # Returns 20 most recent statuses posted by specific user
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)

    # statuses = api.user_timeline('s2t2')

    # Define how many tweets you want and how much of the tweet to display
    statuses = api.user_timeline('s2t2', tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    status = statuses[0]
    print(status.id)
    print(status.full_text)

    for status in statuses:
        print('-----')
        print(status.full_text)

