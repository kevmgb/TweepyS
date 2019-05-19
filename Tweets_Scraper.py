# Required libraries

import json
import csv
import tweepy
import re

# Goal: Collect Raw tweets from #Ikokazi
# Inputs: user_key, user_secret, access_token,access_token_secret (for twitter authentication)
# Output: .csv spreadsheet with tweets

# For application authentication
user_key = input('Enter Your User Key ')
user_secret = input('Enter Your User Secret ')
access_token = input('Enter Your Access Token ')
access_token_secret = input('Enter Your Access Token Secret ')

# This hashtag will be #Ikokazi provided as input but with this method, any hashtag can be used.

hashtag_phrase = input('What hashtag are you interested in ?')



# tweet_amount = input ('How many tweets would you like ?')
# if __name__ == '__main__':
#     search_for_hashtags(user_key, user_secret, access_token, access_token_secret, hashtag_phrase)


# function that takes our access codes

def search_for_hashtags(user_key, user_secret,access_token, access_token_secret, hashtag_phrase):

    # create an twitter authentication object, using our access codes

    authenticate = tweepy.OAuthHandler(user_key, user_secret)
    authenticate.set_access_token(access_token, access_token_secret)

    # Start the tweepy Api here
    api = tweepy.API(authenticate) # Tweepy takes the authentication object for verification

    # create spreadsheet we will write to
    IkokaziTweets = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    # open the spreadsheet so as to write in it
    with open('%s.csv' % (IkokaziTweets), 'w', encoding= 'utf8') as file:
        #Lets alias it as write
        write = csv.writer(file)

        # write a header row
        write.writerow(['Timestamp', 'Tweet_text', 'username', 'followers'])

        # write tweets related to #IkoKazi (or any provided hashtag) to spreadsheet
        # i have filtered retweets, also used extended to make sure all text is present
        for tweet in tweepy.Cursor(api.search, q =hashtag_phrase + ' -filter:retweets', \
                                   tweet_mode='extended').items(200): # Lets get 200 tweets for now, we could alternatively pass (tweet_amount) in .items()

            # Write to spreadsheet the timestamp(tweet.created_at), the tweet itself(tweet.full_text.replace)
            # The username (tweet.user.screen_name.encode('utf-8'), and followers of who tweeted.

            write.writerow([tweet.created_at, tweet.full_text.replace('\n', ' '),
                        tweet.user.screen_name.encode('utf-8'),
                       tweet.user.followers_count])