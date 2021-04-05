# yjmMSswmJSbJ0RSU

This project uses the tweepy library to get information related to the tweets that we are looking for using certain words (query).

## Notes about the project
The reply/discussion count is not available in the tweepy library.
It is available in twitter’s API, however it requires premium membership [(Reference)](https://stackoverflow.com/questions/47851662/reply-count-attribute-missing-from-tweet-object).

Instead, I decided to display the @ name of the user.

For the sorting part, each column is being sorted in descending order.
However, after the first column is done sorting, the column that follows will wait for the previous column to finish sorting out, and then it will start sorting. 
I couldn’t quite figure out what’s the problem. I’m assuming it’s a bug related to the pandas library. 

You can check the sorting method by putting the desired column at the beggning of sort_values.

```
sorted_df = df.sort_values(["Favorite count", "Retweet count", "Date of the tweet", "Discussion"], ascending=(False, False, False, False))
```
