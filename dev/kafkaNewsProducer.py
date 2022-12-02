import logging
from kafka import KafkaProducer
import props
import auth
import json
import time
from datetime import datetime
from datetime import timedelta

producer = KafkaProducer(bootstrap_servers=props.bootstrap_servers, value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))


class NewsStream:
    def __init__(self, api):
        self.api = api

    def get_news(self, rule, hr_offset, min_offset):
        now = datetime.utcnow() - timedelta(hours=hr_offset, minutes=min_offset)
        now_iso = now.isoformat(timespec="seconds")
        return self.api.get_everything(q=rule, from_param=now_iso, language='en')

    def start(self, rule, consistency):
        while True:
            all_news = self.get_news(rule, 0, consistency)['articles']
            print(len(all_news))
            for new in all_news:
                title = new['title']
                descr = new['description']
                data = title + ' ' + descr
                producer.send(props.topics[1], value=data)
            time.sleep(consistency * 60)


if __name__ == '__main__':
    # Create logging instance
    logging.basicConfig(filename='debug.log', encoding='UTF-8', level=logging.DEBUG)

    stream = NewsStream(auth.news_api)
    try:
        stream.start('elon OR amazon OR trump OR bitcoin OR biden OR european OR putin', 15)
    except Exception as ex:
        print(ex.args)