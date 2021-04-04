import tweepy
import pandas as pd
import webbrowser

# API Authentication
ACCESS_TOKEN = '623947370-RV0FPSxSVXbTM8amwn9Fi22VV5Lt4RbHhh3AIWhk'
ACCESS_SECRET = 'BWnSPEBZb9s4LNIsPMRQxQIccHictI4vUdDqK6LfbqPYU'
CONSUMER_KEY = 'hSbJP9K4ovZ6Nt6t2NlG3vzqV'
CONSUMER_SECRET = 'LFsas61Gvaoik6ly6XYIjJCG11fbjWp2RnytFLm7BjWPu3b2k9'


# Accessing the API's data
def connect_to_twitter_Auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


# API object
api = connect_to_twitter_Auth()

# Finding a certain word (query)
moeghri_tweets = api.search(q='request for startup', lang='en', count=80)


# Extracting data from tweets
def extract_tweet_attributes(tweet_object):
    # Empty list
    tweet_list = []
    # loop through tweet objects
    for tweet in tweet_object:
        tweet_at = tweet.user.name
        tweet_user = tweet.user.screen_name
        tweet_id = tweet.id  # unique integer identifier for tweet
        text = tweet.text  # utf-8 text of tweet
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at  # utc time tweet created
        reply_to_status = tweet.in_reply_to_screen_name  # if reply int of orginal tweet id

        # Adding tweet attributes to the list
        tweet_list.append({'tweet_id': tweet_id,
                           'twitter_display_name': tweet_user,
                           'tweet_@_name': tweet_at,
                           'tweet_text': text,
                           'favorite_count': favorite_count,
                           'retweet_count': retweet_count,
                           'created_at': created_at,
                           'reply_to_status': reply_to_status,
                           })

    # Dataframe
    df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                           'twitter_display_name',
                                           'tweet_@_name',
                                           'tweet_text',
                                           'favorite_count',
                                           'retweet_count',
                                           'created_at',
                                           'reply_to_status'])

    return df


# Assigning the extract function with the search results to df
df = extract_tweet_attributes(moeghri_tweets)

# Putting the attributes in a CSV file
x = pd.read_csv(r'C:\Users\Mohammad Shughri\Desktop\test2.csv')

# Sorting the values in descending order
sorted_df = df.sort_values(by=["favorite_count", "retweet_count", "created_at"], ascending=[False, False, False])
sorted_df.to_csv('test2.csv', index=True)
print(sorted_df)

# Outputing the CSV in an external webpage
a = pd.read_csv(r'C:\Users\Mohammad Shughri\Desktop\test2.csv')
sorted_df.to_html("Table.html")
html_file = sorted_df.to_html()
f = open('Table_output.html', 'w')
webbrowser.open_new_tab('Table.html')
