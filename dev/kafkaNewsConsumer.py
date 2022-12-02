from kafka import KafkaConsumer
import props
import json

consumer_news = KafkaConsumer(props.topics[1],
                              bootstrap_servers=props.bootstrap_servers,
                              value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer_news:
    tweets = json.loads(json.dumps(message.value))
    print(tweets)
