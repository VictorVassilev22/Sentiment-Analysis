from kafka import KafkaConsumer
import props
import json
import auth

# Create kafka consumer, same conf as producer

consumer_tweets = KafkaConsumer(props.topics[0],
                                bootstrap_servers=props.bootstrap_servers,
                                value_deserializer=lambda x: json.loads(x.decode('utf-8')))


def get_retweeters(tweet):
    id = tweet['data']['id']
    return auth.tw_client.get_retweeters(id)


def get_author(tweet):
    tw_id = tweet['data']['id']
    return auth.tw_client.get_tweet(tw_id, expansions='author_id').data.author_id


for message in consumer_tweets:
    tw = json.loads(json.dumps(message.value))
    get_author(tw)
    print(tw)
