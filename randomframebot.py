import os
import random
import tweepy
import time
from datetime import datetime, timedelta

bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

folders = [
    './path/to/your/folders/'
]

print('='*10, " RANDOM FRAME BOT V1 ", '='*10)

def check_recent_tweet(last_tweet_time_str):
    if not last_tweet_time_str:
        return False
    last_tweet_time = datetime.strptime(last_tweet_time_str, '%Y-%m-%d %H:%M:%S')
    current_time = datetime.now()
    time_diff = current_time - last_tweet_time
    return time_diff < timedelta(minutes=50)

def save_last_tweet_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('savestate.txt', 'w') as f:
        f.write(current_time)

while True:
    try:
        now = datetime.now().strftime('%d/%m/%Y | %H:%M:%S')

        last_tweet_time_str = ''
        if os.path.exists('savestate.txt'):
            with open('savestate.txt', 'r') as f:
                last_tweet_time_str = f.read().strip()

        if check_recent_tweet(last_tweet_time_str):
            print("The latest tweet is recent, please wait 5 minutes to try again.")
            time.sleep(300)
            continue

        folder_path = random.choice(folders)
        files = os.listdir(folder_path)
        random_file = random.choice(files)

        media = api.media_upload(filename=os.path.join(folder_path, random_file))
        media_id = media.media_id_string
        base_filename = os.path.splitext(random_file)[0]
        text = base_filename
        client.create_tweet(text=text, media_ids=[media_id])
        save_last_tweet_time()
        print("Tweeted!  --  ", now)

    except tweepy.TweepError as e:
        print("Twitter API error:", e)
        print("Retrying in 10 seconds...")
        time.sleep(10)
    except Exception as e:
        print("Error:", e)
        print("Retrying in 10 seconds...")
        time.sleep(10)
    finally:
        time.sleep(3600)
