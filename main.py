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
tweet_search = api.search(q='request for startup', lang='en', count=50)


# Extracting data from tweets
def extract_tweet_attributes(tweet_obj):
    # Empty list
    tweet_list = []
    # loop through tweet objects
    for tweet in tweet_obj:
        tweet_user = tweet.user.name  # User's display name
        tweet_at = tweet.user.screen_name  # User's @ name/ID
        tweet_id = tweet.id  # ID of the tweet
        text = tweet.text  # Text of the tweet
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        tweet_date = tweet.created_at  # utc time tweet created
        discussion_users = tweet.in_reply_to_screen_name  # @ Names of users who replied

        # Adding tweet attributes to the list
        tweet_list.append({'Tweet ID': tweet_id,
                           'Display name': tweet_user,
                           'Tweet @name': tweet_at,
                           'Tweet text': text,
                           'Favorite count': favorite_count,
                           'Retweet count': retweet_count,
                           'Date of the tweet': tweet_date,
                           'Discussion': discussion_users,
                           })

    # Dataframe
    df = pd.DataFrame(tweet_list, columns=['Tweet ID',
                                           'Display name',
                                           'Tweet @name',
                                           'Tweet text',
                                           'Favorite count',
                                           'Retweet count',
                                           'Date of the tweet',
                                           'Discussion'])

    return df


# Assigning the extract function with the search results to df
df = extract_tweet_attributes(tweet_search)


# Putting the attributes in a CSV file
x = pd.read_csv(r'C:\Users\Mohammad Shughri\Desktop\test2.csv')

# Sorting the values in descending order
sorted_df = df.sort_values(["Favorite count", "Retweet count", "Date of the tweet", "Discussion"], ascending=(False, False, False, False))
sorted_df.to_csv(r'C:\Users\Mohammad Shughri\Desktop\test2.csv', index=False)
print(sorted_df)

# Outputting the CSV in an external webpage
a = pd.read_csv(r'C:\Users\Mohammad Shughri\Desktop\test2.csv')
sorted_df.to_html("Table.html")
html_file = sorted_df.to_html()
f = open('Table_output.html', 'w')
webbrowser.open_new_tab('Table.html')
