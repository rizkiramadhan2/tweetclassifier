import tweepy
class tweet:
	"""docstring for ClassName"""


	def get_tweet(url):
		

		consumer_key = "MwH6P6BcYz7OMBnmVzntG3LkK"
		consumer_secret = "kt4Grik27jz8ijqr1s5Qy3XSX7wvva8eSLG5NcdND9qqucesRq"
		access_token = "99431125-OM7FT50GuvMM38BMvdeJEnAhJm147wh0W2EQj78Vf"
		access_token_secret = "H4gFcKdNGbjjX0BomIYzf8InJwbGVT86qZhKdSGzfAAcK"

		# Creating the authentication object
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		# Setting your access token and secret
		auth.set_access_token(access_token, access_token_secret)
		# Creating the API object while passing in auth information
		# Creating the API object while passing in auth information
		#url = 'https://twitter.com/swinginthegardn/status/1029598888414461952'
		tweet_id = url.split('/')[-1]
		api = tweepy.API(auth)
		return api.get_status(tweet_id, tweet_mode='extended')._json['full_text']
		
		