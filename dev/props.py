import tweepy

search_rules = [tweepy.StreamRule('(intel OR amd) lang:en -is:retweet -is:reply')]
# tweepy.StreamRule('(trump OR musk) lang:en') -is:reply -is:retweet
topics = ['TW_ANALYSIS']
bootstrap_servers = ['localhost:9092']
