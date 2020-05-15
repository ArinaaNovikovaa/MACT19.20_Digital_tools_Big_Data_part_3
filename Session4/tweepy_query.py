import tweepy
import pandas as pd

consumer_key = 'dq1eizDpvpN8UaNvuIBQoz59M'
consumer_secret = '0cUblSwiKvCmSfvH5oSrtR0CvxKKa2lOrkJuz1CzjQVjzv4R8O'

tweets = []
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='barcelona').items(10000):
    text = tweet.text
    place = tweet.place
    if place:
        place_name = place.full_name
        bbox = place.bounding_box
        bbox = bbox.coordinates[0]
        place_lat_min = bbox[0][0]
        place_lon_min = bbox[0][1]
        place_lat_max = bbox[2][0]
        place_lon_max = bbox[2][1]
    else:
        place_lat_min = None
        place_lon_min = None
        place_lat_max = None
        place_lon_max = None
    print(text)
    tweets.append([text, place_lat_min, place_lon_min, place_lat_max, place_lon_max])
    print(tweet.text)

df = pd.DataFrame(tweets, columns=['id', 'text', 'place_lat_min', 'place_lon_min', 'place_lat_max', 'place_lon_max'])
df.to_csv('tweets.csv')
