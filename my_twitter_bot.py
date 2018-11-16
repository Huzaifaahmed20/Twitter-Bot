import tweepy
import time
print('Py is running')

API_KEY = 'Zoysn4jJxOb9SFcbxw0mLCGYc'
API_SECRET = 'Bzr3I0OMB2R1U7kdxpDfnTrYa7tQzEnYMroM1mUvGtNrQBa48w'
ACCESS_TOKEN = '739473272295821312-p8H7qHU0rT9Vx99WJIaGSQYdoE1HcwP'
ACCESS_TOKEN_SECRET = '2HzYLgcEEbTgtDJ9A44YNDyZLOShsMtJngTbUg9zDzPjZ'


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
trends = api.trends_place(1)
data = trends[0]

# mentions = api.mentions_timeline()

# print type(trends)



def retrieve_last_seen(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print 'replying to tweets'
    last_seen_id = retrieve_last_seen(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended'
    )

    # 1062064370828615682
    for mention in mentions:
        print(str(mention.id)+'----'+mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        for trendName in data['trends']:
            print '-------  '+trendName['name'].encode('utf8')

            # reply to #helloworld
            if '#helloworld' in mention.full_text: 
            # reply to top 10 trending hastags
            # if trendName['name'].encode('utf8') in mention.full_text:
                print('found helloworld')
                print('responding back ...')
                api.update_status('@'+mention.user.screen_name +
                ' hey responding '+trendName['name'].encode('utf8')+  
                ' back to you', mention.id)


while True:
    reply_to_tweets()
    time.sleep(5)
