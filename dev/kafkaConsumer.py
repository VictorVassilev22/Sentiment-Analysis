from kafka import KafkaConsumer
import props
import json

# Create kafka consumer, same conf as producer

consumer = KafkaConsumer(props.topics[0],
                         bootstrap_servers=props.bootstrap_servers,
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    tweets = json.loads(json.dumps(message.value))
    print(tweets)
