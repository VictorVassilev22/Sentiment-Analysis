import tweepy
from newsapi import NewsApiClient

api_key = 'lzpJJaQNYI3N7BWQhB0ewg7KL'
api_secret = 'AtumjQjs7uhirV3v2sawFOM4vE0JdY5ZN11O9Z7uantijQ8RDe'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKerjwEAAAAA0Sdk12hcYpnkg7ShYs3AURbiILA%3DBwcdZrE7XRaxuQAhTM6WEaR1S6OyKUImSANlWizdPMqBG1UESM'
access_token = '1524184142249963521-Ls2vzRA9iKkYHbg3zKfp5MRvnijwLg'
access_secret = 'DW2f8gA1Vo7T18EBqQ7DuEsPVYCG5Rs9eqmrQhxdXEqoj'

newsapi_key = '6390c31de4a84e01b99c196e876fd9c1'

tw_client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_secret)
tw_auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
tw_api = tweepy.API(tw_auth)

news_api = NewsApiClient(api_key=newsapi_key)

