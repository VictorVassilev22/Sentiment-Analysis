import tweepy

search_rules = [tweepy.StreamRule('musk lang:en -is:retweet')]
# tweepy.StreamRule('(trump OR musk) lang:en') -is:reply -is:retweet
topics = ['TWITTER', 'NEWS']
bootstrap_servers = ['localhost:9092']
